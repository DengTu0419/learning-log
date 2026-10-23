from fastapi import FastAPI  # 导入 FastAPI 类
from fastapi.responses import FileResponse  # 导入 FileResponse：用来把文件原样返回给浏览器
app = FastAPI()  # 创建应用实例

STOP_WORDS = {"the", "a", "an", "and", "or", "of", "to", "in", "is", "we", "our", "that", "it", "for"}
def count_words(text):
    words = text.split()
    counts = {}
    for word in words:
        word = word.lower()
        word = word.strip(".,;:?!#\"'()")
        if word == "" or word in STOP_WORDS:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


@app.get("/")  # 访问根路径 / 时，返回页面文件
def index():
    return FileResponse("index.html")  # 返回当前目录下的 index.html；浏览器收到后渲染成网页

@app.get("/stats")
def stats(text : str = ""):
    counts = count_words(text)
    top = sorted(counts.items(), key = lambda x:x[1] , reverse = True)[:10]
    result = []
    for word , count in top:
        result.append({"word" : word , "count" : count})
    return {"top" : result }
    
