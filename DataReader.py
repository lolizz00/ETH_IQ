from threading import Thread
from IQ import IQ
import struct
from ctypes import *
import math
from PyQt5.QtCore import *
import time
import platform


# Общая схема такова:
#       1. В класс DataReader пишем, что и в каком формате мы хотим считать
#       2. DataReader запускаем DLL, которая читает данные
#       3. DataReader создает для каждого канала свой поток(DataReaderMin), который переводит данные из файла в нужный вид
#       4. DataReader соединяет данные


# класс для считывания данных с Этажерки
class DataReader(QObject):

    # данные сначала сохраняются в файл
    NAME = 'data'
    FORMAT = '.pcm'
    FOLDER = 'data\\'


    REALTIME_FLG = True

    # запись в лог в GUI
    log_signal = pyqtSignal(str, bool)


    # перевод количетсва точек в количество посылок
    def pointToPos(self, cnt):
        k = 2048

        res = cnt / k
        res = math.ceil(res)
        res = int(res)

        return res


    def setChanN(self, chan_n):
        self.CHAN_N = chan_n

    def __init__(self):
        super(DataReader, self).__init__()

        self.THREAD_N = 0
        self.POS_N = 0
        self.CHAN_N = 0
        self.data = []
        self.th = []

    def initDLL(self):
        self.initDLL()


    # запись в лог
    def log(self, msg, showErr=False):
        msg = 'Datareader: ' + msg
        self.log_signal.emit(msg, showErr)
        print(msg)

    # загрузка библиотеки
    def initDLL(self):

        try:



            # автоматический выбор версии DLL
            if platform.architecture()[0] == '64bit':
                self.dll = cdll.LoadLibrary('UDP_reader_x64.dll')
            else:
                self.dll = cdll.LoadLibrary('UDP_reader_x32.dll')

            # тип аргументов
            self.read = self.dll.READER_read
            self.read.argtypes = [c_int, c_char_p]
            self.read.restype = c_int

            self.log('Библиотека успешно инициализирована')
        except:
            self.log('Ошибка инициализации библиотеки!')
            raise

    # считывание одного файла
    def readFile(self, name):
        self.th = []
        self.data =  []
        self.th.append(DataReaderMin(0))
        self.th[0].setFile(name)
        self.th[0].setChanN(self.CHAN_N)
        self.th[0].setFs(self.fs)
        self.th[0].start()
        self.th[0].join()

        if self.th[0].ERR_FLG:
            self.log('Неверный файл!')
            return False

        self.data.append(self.th[0].data)

        return  True

    # инициализация перед запуском
    def initReader(self, fs, chans, point_cnt=50, addr=""):
        self.THREAD_N = chans # для каждого канала свой поток
        self.POS_N = point_cnt

        self.th = []

        # выбираем адрес
        self.addr = addr
        self.addr = addr

        sch = 0
        for n in self.THREAD_N:
            # формируем имя 'data0.pcm' в зависимости от канала
            name = self.NAME + str(n) + self.FORMAT


            if self.FOLDER:
                name = self.FOLDER + name

            # инициализируем чтение данных с канала в отдельном потоке
            self.th.append(DataReaderMin(n))
            self.th[sch].setFile(name) # имя файла
            self.th[sch].setChanN(self.CHAN_N)  # I+Q или I
            self.th[sch].setFs(fs)
            self.th[sch].setChanNumber(n)
            sch = sch + 1

        #self.log('Инициализация успешна')

    # запуск чтения
    def run(self):

        #self.log('Запуск...')

        self.data = {}

        t0 = time.time()

        # если чтенние в реальном времени
        if self.REALTIME_FLG:

            try:
                # пробуем считать, запуск DLL
                if self.read(self.POS_N,c_char_p (self.addr.encode ('utf-8'))) != 0:
                    raise
            except:
                self.log('Устройство не подключено! Отображаем старые данные', True)
                #self.log('Пробуем считать старые данные...')



        time.sleep(0.3)


        # запускаем потоки для каждого канала
        #self.log('Запускаем потоки...')
        for th in self.th:
            th.start()

        #self.log('Ждем окончание работы потоков...')
        # ждем окончания работы всех потоков
        for th in self.th:
            th.join()

        #self.log('Собираем данные...')
        # соеднияем данные
        for th in self.th:
            n = th.getChanNumber()
            self.data[n] = th.data

        for th in self.th:
            if th.ERR_FLG:
                self.log('Ошибка!')
                return  False

        return True

        #self.log('Успешно!')

class DataReaderMin(Thread):

    ERR_FLG  = False

    # тут все понятно
    def __init__(self, _id):
        super(DataReaderMin, self).__init__()
        self.data = IQ()
        self.file = ""
        self.id = _id
        self.chanN = 1

    def getChanNumber(self):
        return self.n

    def setChanNumber(self, n):
        self.n = n

    def setFs(self, Fs):
        self.fs = Fs

    # считаем, один каанал или несколько
    def setChanN(self, n):
        self.chanN = n

    # перекидываем наверх слоги
    def log(self, msg):
        msg = 'Канал #' + str(self.id + 1) + ' :: ' + msg
        print(msg)

    # выбираем номер канала из которого читаем
    def setFile(self, _file):
        self.file = _file


    # основная функция
    def procces(self):

        #self.log('Переводим данные в нужный формат...')

        # открываем считанный DLL-ем файл
        bts = open(self.file, "rb").read()


        # переводим байты из файла в отсчеты
        stream_len = len(bts) / 2 # количество отсчетов
        frmt = str(int(stream_len)) + 'h' # указываем сколько 16-битных чисел мы можем взять
        val = list(struct.unpack(frmt, bts)) # извлекаем


        if self.chanN == 1: # если считаем, что один канал (все данные это I)
            self.data.addIQ(val) # просто сохраняем
        elif self.chanN == 2: # если считаем что это I и Q
            I = val[0::2] # а они чередуются
            Q = val[1::2]
            self.data.addIQ(I, Q) # тоже просто сохраняем



        self.data.generateA(self.fs)  # считаем амплитуду в зависимости от I+Q или I
        self.data.genreateX() # создаем отсчеты для абсциссы - целые числа с 0 до длинны
        #self.log('Готово!')

    # запуск в потоке
    def run(self):
        self.ERR_FLG = False
        #self.log('Запуск...')
        try:
            self.procces()
        except:
            self.ERR_FLG = True
            raise





