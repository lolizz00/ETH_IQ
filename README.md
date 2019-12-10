### Запуск: start.py

## Установка Python (чистая)

- Версия Python: 3.7 
- Скачать можно с https://www.python.org/downloads/release/python-375/ (Windows x86-64 executable installer)
- При установке:
    - Выберите `Customize installation`
    - `Next`
    - Измените путь на более короткий(необязательно, для удобства). Например `C:\Python37\`.
    - Поставьте галочки в `Install for all users ` и `Add Python to environment ....`. 
    - Остальные оставьте без изменений.

## Список необходимых пакетов


- PyQt5
- numpy
- scipy
- pyqtgraph

#### Установка пакетов: `python -m pip install [имя пакета]`. Например: `python -m pip install numpy`. 
#### Если Python не был добавлен в переменные среды, то используйте синтаксис `[папка установки]\python.exe -m pip install [имя пакета]`. Например: `C:\Python37\python.exe -m pip install numpy`.



## Возможные ошибки
- Устройтсво не подключено или `Timeout!`
    - Проверьте IP адрес
    - Проверьте настройки адаптера
    - В диспетчере задач->Подробно->Сеть проверьте, идут ли данные от Этажерки
- Не является приложением Win32(актуально только для старых версий)
    - В папке проекта  удалите файл `UDP_reader.dll` и   переименуйте файл  `UDP_reader_x32.dll` в `UDP_reader.dll`
- `Verr --- ERR` 
    - Программе не удается считать подряд идущие пакеты.   

## Настройки адаптера

- Link Speed:   10G
- Jumbo Packet: 9014
- Maximum Number of RRS Queues: 4 Queues 
- Performance Options
    - Flow Control:  TX & RX Enabled
    - Receive Buffers: 4096
    - Transmit Buffers:  4096



