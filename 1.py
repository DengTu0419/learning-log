with open("Data/sample.txt",encoding = "utf-8") as f:
    text = f.read()
#print (text)
words = text.split()
#print(words[:10])

counts = {}
stop_words = {"the", "a", "an", "and", "or", "of", "to", "in", "is", "we", "our", "that", "it", "for"}
for word in words:
    word = word.lower()
    word = word.strip(".,/\"!")
    if word == "" or word in stop_words:
        continue
    counts[word] = counts.get(word, 0) + 1

#print(counts)

top_words = sorted(counts.items(), key = lambda x : x[1], reverse = True)[:10]

#print (top_words)

for i , (word, count) in enumerate(top_words, 1):
    print (i, word, count)