def is_prime(func):
    def wrapper(a, b, c):
        n = func(a, b, c)
        if n < 2:
            raise ValueError()
        res = True
        for d in range(2, n // 2 + 1):
            if not n % d:
                res = False
                break
        print("Простое" if res else "Составное")
        return n

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
result = sum_three(3, 3, 6)
print(result)
result = sum_three(1, 1, 2)
print(result)
result = sum_three(1, 1, 0)
print(result)
result = sum_three(1, 0, 0)
print(result)
