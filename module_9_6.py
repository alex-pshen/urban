def all_variants(text):
    for size in range(1, len(text) + 1):
        for beg in range(len(text) - size + 1):
            yield text[beg : beg + size]


a = all_variants("abcd")
for i in a:
    print(i)
