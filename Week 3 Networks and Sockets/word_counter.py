counts = {}

file = open('sample text.txt')

for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

file.close()
