import argparse

parser = argparse.ArgumentParser(description="统计文本词频")
parser.add_argument("--file", default="Data/sample.txt", help="要统计的文件路径")
parser.add_argument("--top", type=int, default=10, help="显示前几名")


args = parser.parse_args()


try:
    with open(args.file, encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"文件不存在：{args.file}")
    raise SystemExit(1)



print(len(text))
words = text.split()
print(len(words))
print(words[:10])


counts = {}
stop_words = {"the", "a", "an", "and", "or", "of", "to", "in", "is", "we", "our", "that", "it", "for"}


for word in words:
    word = word.lower()
    word = word.strip(".,;:?!#\"'()")
    if word == "" or word in stop_words:
        continue
    counts[word] = counts.get(word, 0) + 1


print(counts)
top10 = sorted(counts.items(),key = lambda x: x[1], reverse = True)[:args.top]
print(top10[:3])

for i, (word, count) in enumerate(top10,1):
    print(i, word, count)

    