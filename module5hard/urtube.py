import time
from video import Video
from user import User


class UrTube:
    AGE_RESTRICTION = 18  # 18+

    def __init__(self) -> None:
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str) -> bool:
        for user in self.users:
            if user.nickname() == nickname and user.validate_password(password):
                self.current_user = user
                return True
        return False

    def register(self, nickname: str, password: str, age: int) -> None:
        if True in [usr.nickname() == nickname for usr in self.users]:
            print(f"Пользователь {nickname} уже существует")
        else:
            usr = User(nickname, password, age)
            self.users.append(usr)
            self.current_user = usr

    def log_out(self):
        self.current_user = None

    def all_titles(self):
        return [v.title() for v in self.videos]

    def add(self, *args: Video):

        # print(self.all_titles())
        if False in [isinstance(v, Video) for v in args]:
            raise ValueError("Все аргументы должны быть типа Video")

        for v in args:
            if v.title() not in self.all_titles():
                self.videos.append(v)

        # print(self.all_titles())

    def get_videos(self, subtitle: str):
        return [t for t in self.all_titles() if subtitle.lower() in t.lower()]

    def find_video(self, title):
        return next((v for v in self.videos if title == v.title()), None)

    def watch_video(self, title) -> None:
        video = self.find_video(title)
        if video == None:
            return

        if type(self.current_user) == type(None):
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif video.adult_mode() and self.current_user.age() < self.AGE_RESTRICTION:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            while video.next():
                print(video.current_time(), end=" ", flush=True)
            print("Конец видео")
