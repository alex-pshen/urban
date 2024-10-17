class User:
    MIN_NICKNAME_LEN = 4
    MIN_PASSWORD_LEN = 4
    MIN_AGE = 3

    @classmethod
    def is_nickname_valid(cls, nickname: str) -> bool:
        return type(nickname) == str and len(nickname) >= cls.MIN_NICKNAME_LEN

    @classmethod
    def is_password_valid(cls, password: str) -> bool:
        return type(password) == str and len(password) >= cls.MIN_PASSWORD_LEN

    @classmethod
    def is_age_valid(cls, age: int) -> bool:
        return type(age) == int and age >= cls.MIN_AGE

    @classmethod
    def validate_credentials(cls, nickname, password, age) -> bool:
        return (
            cls.is_nickname_valid(nickname)
            and cls.is_password_valid(password)
            and cls.is_age_valid(age)
        )

    def __init__(self, nickname: str, password: str, age: int) -> None:
        if User.validate_credentials(nickname, password, age):
            self.__nickname = nickname
            self.__hashed_password = hash(password)
            self.__age = age
        else:
            raise ValueError(
                f"""Имя пользователя должно быть строкой и состоять не менее, чем из {User.MIN_NICKNAME_LEN} символов
                    пароль быть строкой и состоять не менее, чем из {User.MIN_PASSWORD_LEN} символов
                    пользователи возраста менее {User.MIN_AGE} лет не допускаются"""
            )

    def __eq__(self, other):
        return (
            self != None
            and other != None
            and self.__nickname == other.__nickname
            and self.__hashed_password == other.__hashed_password
        )

    def age(self) -> int:
        return self.__age

    def nickname(self):
        return self.__nickname

    def validate_password(self, password):
        return self.__hashed_password == hash(password)
