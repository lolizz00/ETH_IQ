#include "UDP_reader.h"

#include <iostream>


using namespace std;

int TOUT_FLG = 0;


char* ADDR;

#define PNT_PER_POS 2048
int POS_N = 0;
int POS_N_WRITE = 0;
#define PORT_N 8

#define POS_OFFS 8

int FLG = 0;

#define POS_SIZE 8196

int READY_FLG = 0;

WSASession Session;
vector<UDPSocket> sockets;
vector<uint8_t**> buffs;
vector<thread> threads;

int down_offs[PORT_N] = { 0 };
int up_offs[PORT_N] = { 0 };


int min[PORT_N] = { 0 };
int max[PORT_N] = { 0 };


/*
	Проверка, что все позиции идут подряд
*/
int verPos()
{
	int ret = 1;

	for (int j = 0; j < PORT_N; j++)
	{
		for (int i = 0; i < POS_N - 1; i++)
		{
			uint32_t a = *(uint32_t*)buffs[j][i];
			uint32_t b = *(uint32_t*)buffs[j][i + 1];


			//cout << a <<  " " << b << endl;

			if ((a + 1) != b)
			{
				//break;
				return 0;
				ret = 0;
			}
		}
	}

	return ret;
}


/*
	Запись принятых данных в файл
*/
void writeFile(int n, uint8_t** buff)
{
	FILE *fp;
	string name = "data/data" + to_string(n) + ".pcm";

	_mkdir("data");

	fp = fopen(name.c_str(), "wb");


	int sh = 0;


	//cout << "-----" << endl;
	//cout << "N chan: " << n << endl;

	int sch = 0;


	//cout << "Down offs: " << down_offs[n] << "\tUp offs:" << up_offs[n] << endl;
	for(int i = down_offs[n]; i < POS_N_WRITE - up_offs[n];i++)
	{
		sh++;
		fwrite(buff[i] + 4, POS_SIZE - 4, 1, fp);
		sch = sch + 1;
		i = i + 1;
	}

	//cout << "Data len: " << sh << endl;


	fclose(fp);
}

/*
	Запись всех данных со всех каналов в файл
*/
void save()
{
	for (int i = 0; i < PORT_N; i++)
	{
		writeFile(i, buffs[i]);
	}

}


/*
	Вспомогалка, минимум в массиве
*/
int calcMinArr(int* arr, int n)
{
	int res = INT32_MAX;

	for (int i = 0; i < n; i++)
	{
		if (arr[i] < res)
		{
			res = arr[i];
		}
	}

	return res;
}


/*
	Вспомогалка, максимум в массиве
*/
int calcMaxArr(int* arr, int n)
{
	int res = 0;


	for (int i = 0; i < n; i++)
	{
		if (arr[i] > res)
		{
			res = arr[i];
		}
	}

	return res;
}


/*
	Поиск минимального номера пакета
*/
void calcMin()
{

	for (int i = 0; i < PORT_N; i++)
	{
		min[i] = *(uint32_t*)buffs[i][0];
	}
}

/*
	Поиск максимального номера пакета
*/
void calcMax()
{
	for (int i = 0; i < PORT_N; i++)
	{
		max[i] = *(uint32_t*)buffs[i][POS_N - 1];
	}
}


/*
	Считаем в зависимости от начального и конечного номера пакета, что надо срезать сверху и снизу
*/
void calcOffs()
{
	calcMin();
	calcMax();


	int max_arr_min = calcMinArr(max, PORT_N); /* Находим общее начало и общий конец пакетов */
	int min_arr_max = calcMaxArr(min, PORT_N);

	for (int i = 0; i < PORT_N; i++)
	{
		down_offs[i] = min_arr_max - min[i]; /* Сохраняем, сколько надо съесть, что бы все пакеты на всех каналах были одинаковы */
		up_offs[i] = max[i] - max_arr_min;
	}

}


/*
	Читаем данные
*/
void process(UDPSocket* Socket, uint8_t** buff)
{	

	/*
		Первые пакеты, которые пришли никогда не идут подряд
		Это и фиксим
	*/
	for (int i = 0; i < POS_OFFS; i++)
	{
		int cnt = 0;
		Socket->RecvFrom(buff[i], BUFSIZE, &cnt);
	}

	/*
		А теперь читаем нормально
	*/
	for (int i = 0; i < POS_N; i++)
	{
		int cnt = 0;
		Socket->RecvFrom(buff[i], BUFSIZE, &cnt);

		/*
			Не приняли байтов - ничего нет
		*/
		if (cnt < 0)
		{
			TOUT_FLG = 1;
			return;
		}

	}

	/*WTF ???? */

	/*for (int i = 0; i < POS_N; i++)
	{
		buff[i] = buff[i] + OFFS;
	}*/





}

/*
	Создание буфферов, в которые читаем данные из сокетов и которые пишем в файл
*/
uint8_t** createBuff()
{
	uint8_t** res = NULL;

	res = (uint8_t**)calloc(sizeof(uint8_t*), POS_N);

	for (int i = 0; i < POS_N; i++)
	{
		res[i] = (uint8_t*)calloc(sizeof(uint8_t), (BUFSIZE + 1));
	}


	return res;
}


/*
	Чистим память буферов
*/
void destBuff(uint8_t** buff)
{
	for (int i = 0; i < POS_N; i++)
	{
		free(buff[i]);
	}
	
	free(buff);
}

/*
	Инициализация всего
	Очищаем буфферы
	Очищаем и по новой создает сокеты, включая их
*/
void init()
{
	buffs.clear();
	sockets.clear();

	for (int i = 0; i < PORT_N; i++)
	{
		sockets.emplace_back(UDPSocket());
		sockets[i].Bind(ADDR, PORT + i);

		buffs.push_back(createBuff());
	}
}


/*
	Очистка всего
	Буферы освобождаем
	Чистим сокеты
*/
void dest()
{
	for (int i = 0; i < PORT_N; i++)
	{
		destBuff(buffs[i] /*- OFFS*/);
		sockets[i].close();
	}
}

/*
	Запуск процесса чтения
*/
void run()
{
	threads.clear(); // очищаем потоки

	for (int i = 0; i < PORT_N; i++) // создаем новые и запускаем
	{
		thread thr(process, &sockets[i], buffs[i]);
		threads.emplace_back(std::move(thr));
	}

	for (int i = 0; i < PORT_N; i++) // ждем все потоки
	{
		threads[i].join();
	}


}

/*
	Если очень хочется, можно вывести номера пакетов
*/
void print()
{

	for (int i = 0; i < PORT_N; i++)
	{
		for (int j = down_offs[i]; j < (POS_N - up_offs[i]); j++)
		{
			//cout << *(uint32_t*)buffs[i][j] << " ";
		}

		//cout << endl;
	}

}

#ifdef _DEBUG


/*
	В дебаге запускаем как exe-шник
*/
int main()
{

	for (int i = 0; i < 1; i++)
	{
		READER_read(1);
	}

	system("pause");
	return 0;
}

#else

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
	switch (fdwReason) {
	case DLL_PROCESS_ATTACH:

		break;
	case DLL_THREAD_ATTACH:

		break;
	case DLL_THREAD_DETACH:

		break;
	case DLL_PROCESS_DETACH:

		break;
	}
	return TRUE;
}

#endif // _DEBUG


DLLEXPORT int READER_read(int n, char* _ADDR)
{
	TOUT_FLG = 0;

	ADDR = _ADDR;


	cout << "ADDR: " << ADDR << endl;


	/* Сколько посылок читаем */
	POS_N_WRITE = n;

	/*
		Нельзя меньше минимума 
	*/
	if (n < 70)
	{
		n = 70;
	}

	
	POS_N = n;

	/*
		Инциализируем
	*/
	init();

	int sch = 0;

	do
	{
	
		cout << "Try to read..." << endl;
		sch++;

		run(); /* Пробуем считать */


		/* Считать не удалось - увы, пока */
		if (TOUT_FLG)
		{
			dest();
			cout << "Timeout!" << endl;
			return -1;
		}

		/* Проверяем, что пакеты идут подряд */
		if (verPos())
		{
			cout << "Ver --- OK" << endl;
			break;
		}
		else
		{
			cout << "Verr --- ERR" << endl; /* Пробуем еще раз */
		}

	} while (1);


	/* Срезаем лишние */
	calcOffs();

	/* Сохраняем в файл  */
	save();

	/* Чистим все */
	dest();

	cout << "Finished!" << endl;

	return 0;
}



