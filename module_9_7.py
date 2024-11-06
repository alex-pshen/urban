def check_prime(n):
    if n < 2:
        raise ValueError("Для чисел меньше 2, простота не определена")
    for d in range(2, n // 2 + 1):
        if not n % d:
            return False
    return True


def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if check_prime(n):
            print("Простое")
        else:
            print("Составное")
        return n

    return wrapper


def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)

    return wrapper


@print_result
@is_prime
def sum_three(a, b, c):
    return a + b + c


sum_three(2, 3, 6)
sum_three(3, 3, 6)
sum_three(1, 1, 2)
sum_three(1, 1, 0)
sum_three(1, 0, 0)
