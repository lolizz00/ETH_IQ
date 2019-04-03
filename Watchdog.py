from threading import Timer

class Watchdog:

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.timer.cancel()


    def __init__(self, timeout, userHandler=None):  # timeout in seconds
        self.timeout = timeout
        self.handler = userHandler if userHandler is not None else self.defaultHandler
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def reset(self):
        self.timer.cancel()
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def stop(self):
        self.timer.cancel()

    def defaultHandler(self):
        self.timer.cancel()
        raise Exception