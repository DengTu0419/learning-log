with open("learning-log/Data/sample.txt", encoding = "utf-8") as f:
    text = f.read()

print(len(text))

words = text.split()
print(len(words))
print(words[:10])

counts = {}

for word in words:
    word = word.lower()
    word = word.strip(".,;:?!#\"'()")
    if word == "":
        continue
    counts[word] = counts.get(word, 0) + 1

print(counts)

top10 = sorted(counts.items(),key = lambda x: x[1], reverse = True)[:10]

for i, (word, count) in enumerate(top10,1):
    print(i, word, count)

    