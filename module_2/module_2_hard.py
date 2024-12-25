import random

low = 3
high = 20
n = random.randint(low, high)
result = ''

for a in range(1, high // 2 + 1):
    for b in range(a + 1, high):
        if n % (a + b) == 0:
            result += str(a) + str(b)

print(result)