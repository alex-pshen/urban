import requests
import pandas
import numpy
import matplotlib.pyplot as plt

resp = requests.get("https://urban-university.ru")
print(resp.text)

data = pandas.read_csv("foo.csv")
res = data.groupby("gender").sum()
print(res)

a = numpy.arange(6).reshape(2, 3)
b = numpy.arange(4, 10).reshape(2, 3)
c = a + b
print(c)

keys = ["a", "b", "c"]
values = [65, 54, 43]
plt.bar(keys, values, color="maroon", width=0.4)
plt.show()
