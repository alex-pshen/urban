def check_frozen(is_frozen):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if is_frozen:
                print("Тесты в этом кейсе заморожены")
            else:
                func(*args, **kwargs)

        return wrapper

    return decorator
