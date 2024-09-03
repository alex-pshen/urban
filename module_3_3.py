def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(10)
print_params(10, 2)
print_params(10, 2, 3)

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['a', False, 0.1]
values_dict = {'a' : False, 'b' : 1., 'c' : 'qwerty'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)