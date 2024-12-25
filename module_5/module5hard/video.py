import time


class Video:
    TIMEOUT = 1  # in seconds

    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False) -> None:
        self.__title = title
        self.__duration = duration
        self.__time_now = time_now
        self.__adult_mode = adult_mode

    def title(self):
        return self.__title

    def duration(self):
        return self.__duration

    def adult_mode(self):
        return self.__adult_mode

    def current_time(self):
        return self.__time_now

    def next(self) -> bool:
        if self.current_time() >= self.duration():
            self.__time_now = 0
            return False

        time.sleep(self.TIMEOUT)
        self.__time_now += 1
        return True
