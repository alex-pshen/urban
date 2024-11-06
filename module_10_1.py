import threading as th
import time
import datetime as dt


def write_words(word_count, file_name):
    with open(file_name, "w") as file:
        for i in range(word_count):
            time.sleep(0.1)
            file.write(f"Какое-то слово № {i}\n")
    print(f"Завершилась запись в файл {file_name}")


start = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
stop = time.time()
print(f"Работа потоков {stop-start}")

t1 = th.Thread(target=write_words, args=(10, "example5.txt"))
t2 = th.Thread(target=write_words, args=(30, "example6.txt"))
t3 = th.Thread(target=write_words, args=(200, "example7.txt"))
t4 = th.Thread(target=write_words, args=(100, "example8.txt"))

start = time.time()

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

stop = time.time()
print(f"Работа потоков {stop-start}")
