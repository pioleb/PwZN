from ascii_graph import Pyasciigraph
from collections import Counter

words = []

file_name = input("Podaj nazwe pliku:")

with open('c:/Users/Piotr/Desktop/python/Lab/Lab1/'+file_name, 'r', encoding="utf8") as f:
    for line in f:
        #print(line.strip().split(' '))
        words.append(line.strip().split(' '))

words = sum(words, [])
words = list(filter(None, words))

#leaving letters only
letters_strings = []

for string in words:
    other = ''
    for char in string:
        if char.isalpha():
            other += char
    letters_strings.append(other)


#removing elements shorter than x
min = 5
new_strings = []
for i in letters_strings:
    if len(i) >=min:
        new_strings.append(i)



data = dict(Counter(new_strings))
data_sorted = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

#histogram size
size = 10
data_limited = dict(list(data_sorted.items())[:size])

graph = Pyasciigraph()
for line in graph.graph('Histogram of Data', data_limited.items()):
    print(line)