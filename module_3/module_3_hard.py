numeric_types = int, float, complex
collections = set, list, tuple, range

def calculate_structure_sum(*data):
    res = 0
    for elem in data:
        if isinstance(elem, str):
            res += len(elem)
        elif type(elem) in numeric_types:
            res += elem
        elif isinstance(elem, bool):
            res += int(elem)
        elif isinstance(elem, dict):
            res += calculate_structure_sum(*elem.items())
        elif type(elem) in collections:
            res += calculate_structure_sum(*elem)
    return res

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)