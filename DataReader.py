from threading import Thread
from IQ import IQ
import struct
from ctypes import *
import math
from PyQt5.QtCore import *
import time
from Watchdog import Watchdog


class DataReader(QObject):

    NAME = 'data'
    FORMAT = '.pcm'

    FOLDER = 'data\\'

    REALTIME_FLG = True


    log_signal =  pyqtSignal(str)



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
        self.initDLL()

    def log(self, msg):
        msg = 'Datareader :: ' + msg
        self.log_signal.emit(msg)

    def initDLL(self):

        try:
            self.dll = cdll.LoadLibrary('UDP_reader.dll')

            self.read = self.dll.READER_read
            self.read.argtypes = [c_int]

            self.wait = self.dll.READER_wait
            self.read.restype = c_int

            self.log('Библиотека успешно инициализирована')
        except:
            self.log('Ошибка инициализации библиотеки!')


    def readFile(self, name):
        self.th = []
        self.th.append(DataReaderMin(0))
        self.th[0].setFile(name)
        self.th[0].setChanN(self.CHAN_N)
        self.th[0].start()
        self.th[0].join()
        self.data.append(self.th[0].data)

    def initReader(self, chans, point_cnt=50):
        self.THREAD_N = chans
        self.POS_N = point_cnt

        self.th = []

        sch = 0
        for n in self.THREAD_N:
            name = self.NAME + str(n) + self.FORMAT


            if self.FOLDER:
                name = self.FOLDER + name

            self.th.append(DataReaderMin(n))
            self.th[sch].setFile(name)
            self.th[sch].setChanN(self.CHAN_N)
            sch = sch + 1

        #self.log('Инициализация успешна')

    def run(self):

        #self.log('Запуск...')

        self.data = []

        t0 = time.time()
        if self.REALTIME_FLG:

            try:
                with Watchdog(1):
                    self.read(self.POS_N)
            except Watchdog:
                self.log('Устройство не подключено!')
                return



        time.sleep(0.3)

        for th in self.th:
            th.start()

        for th in self.th:
            th.join()

        for th in self.th:
            self.data.append(th.data)

        self.log('Успешно!')

class DataReaderMin(Thread):
    def __init__(self, _id):
        super(DataReaderMin, self).__init__()
        self.data = IQ()
        self.file = ""
        self.id = _id
        self.chanN = 1

    def setChanN(self, n):
        self.chanN = n

    def log(self, msg):
        msg = 'DatareaderMin' + str(self.id) + ' :: ' + msg
        print(msg)

    def setFile(self, _file):
        self.file = _file

    def run(self):
        self.log('Запуск')
        bts = open(self.file, "rb").read()
        self.log('Байты прочитаны')
        stream_len = len(bts) / 2
        frmt = str(int(stream_len)) + 'h'
        val = list(struct.unpack(frmt, bts))
        self.log('Байты переведены')

        #val = val[:-2]

        if self.chanN == 1:
           self.data.addIQ(val)
        elif self.chanN == 2:
            I = val[0::2]
            Q = val[1::2]
            self.data.addIQ(I, Q)

        self.log('Байты разбиты')

        self.data.generateA()
        self.data.genreateX()
        self.log('Остановка')




