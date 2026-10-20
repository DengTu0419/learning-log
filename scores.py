names = ["张三","李四","王五","赵六","钱七"]
scores = [85,92,78,95,60]
total = sum(scores)
avg = total / len(scores)
max_scores = max(scores)

record = dict(zip(names,scores))
idx = scores.index(max_scores)
def grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

for name,score in record.items():
    print(name,score,grade(score))
print("平均分：",avg)
print("最高分：",max(record,key = record.get))
