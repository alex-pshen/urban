class WordsFinder:
    punctlist = [",", ".", "=", "!", "?", ";", ":", " - "]

    def __init__(self, *file_names) -> None:
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for fn in self.file_names:
            with open(fn) as file:
                text = file.read().lower()
                for s in self.punctlist:
                    text = text.replace(s, " ")
                words = text.split()
                all_words[fn] = words
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word.lower())

        return result


"""
finder1 = WordsFinder("test_file.txt")
print(finder1.get_all_words())  # Все слова
print(finder1.find("TEXT"))  # 3 слово по счёту
print(finder1.count("teXT"))  # 4 слова teXT в тексте всего

finder2 = WordsFinder(
    "Mother Goose - Monday’s Child.txt",
)
print(finder2.get_all_words())
print(finder2.find("Child"))
print(finder2.count("Child"))

finder3 = WordsFinder(
    "Rudyard Kipling - If.txt",
)

print(finder3.get_all_words())
print(finder3.find("if"))
print(finder3.count("if"))

finder4 = WordsFinder("Walt Whitman - O Captain! My Captain!.txt")
print(finder4.get_all_words())
print(finder4.find("captain"))
print(finder4.count("captain"))
"""
