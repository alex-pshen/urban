# Dictionary
my_dict = {0 : 10, 2 : 20, 4 : 30}
print('Dict:', my_dict)
print('Existing value:', my_dict.get(0))
print('Not existing value:', my_dict.get(256))
my_dict.update({3 : 25, 1 : 15})

# for i in range(5):
#     print(my_dict[i], end = ' ') # Access by index ;-)

print('Deleted value:', my_dict.pop(0))
print('Modified dictionary:', my_dict)

# Set
my_set = {'a', 'b', 'c', 1, 2, .1, 'a', 1, .1}
print('Set:', my_set)
my_set.add('d')
my_set.add(3)
my_set.remove(.1)
print('Modified set:', my_set)