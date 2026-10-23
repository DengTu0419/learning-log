# 词频统计 wordcount.py
# 作用：读文本文件 → 切分单词 → 去掉停用词 → 统计词频 → 按次数从多到少输出前 N 名
# 用法：python wordcount.py --file Data/sample.txt --top 10

import argparse  # 导入 argparse：Python 标准库里专门解析命令行参数的工具

parser = argparse.ArgumentParser(description="统计文本词频")  # 创建参数解析器；description 是 -h 帮助里的说明

parser.add_argument("--file", default="Data/sample.txt", help="要统计的文件路径")  # 定义 --file 参数，不传时默认读 Data/sample.txt

parser.add_argument("--top", type=int, default=10, help="显示前几名")  # 定义 --top 参数；type=int 会把输入转成整数，不传时默认 10

args = parser.parse_args()  # 真正执行解析，命令行参数存进 args；之后用 args.file / args.top 取值

try:  # try：把可能出错的代码包起来，出错时不会直接崩溃
    with open(args.file, encoding="utf-8") as f:  # with open 打开文件；encoding="utf-8" 指定编码防乱码；with 结束时自动关文件
        text = f.read()  # read() 一次性把整个文件读成一个字符串
except FileNotFoundError:  # 只捕获「文件不存在」这一种错误
    print(f"文件不存在：{args.file}")  # 给出看得懂的提示
    raise SystemExit(1)  # 以返回码 1 退出程序，表示这次执行失败

print(len(text))  # 调试输出：总字符数，确认文件确实读进来了
words = text.split()  # split() 按空格/换行/制表符等空白切分，得到单词列表
print(len(words))  # 调试输出：单词总数
print(words[:10])  # 调试输出：前 10 个单词，检查切分是否正确

counts = {}  # 空字典，键是单词，值是出现次数
stop_words = {"the", "a", "an", "and", "or", "of", "to", "in", "is", "we", "our", "that", "it", "for"}  # 停用词集合：这些高频虚词不计入统计

for word in words:  # 逐个遍历单词列表
    word = word.lower()  # 统一转小写，让 The 和 the 算同一个词
    word = word.strip(".,;:?!#\"'()")  # 去掉单词两端的标点，避免 world 和 world, 被当成两个词（strip 只去两端，不去中间）
    if word == "" or word in stop_words:  # 去标点后可能变成空串；空串或停用词都跳过
        continue  # 跳过这次循环，直接处理下一个单词
    counts[word] = counts.get(word, 0) + 1  # 核心计数：get 取当前次数（没有就当 0），加 1 后存回字典

print(counts)  # 调试输出：完整的词频字典
top_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:args.top]  # 字典转成 (词, 次数) 列表，按次数降序排序，再切片取前 args.top 个
print(top_words[:3])  # 调试输出：先看前 3 名

for i, (word, count) in enumerate(top_words, 1):  # enumerate(..., 1)：边遍历边编号，编号从 1 开始
    print(i, word, count)  # 输出一行：名次 单词 次数
