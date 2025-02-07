# 成績登記系統，key是學生的名字，value是學生的成績，每個科目有三個成績
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 90, 100], "英文": [70, 60, 50]},
    "小美": {"國文": [80, 70, 60], "數學": [90, 80, 70], "英文": [60, 50, 40]},
    "小華": {"國文": [70, 60, 50], "數學": [80, 70, 60], "英文": [50, 40, 30]},
}

# 取得小明的數學成績
print(grade["小明"]["數學"])  # [85,90,100]
# 取得小美的第一次英文成績
print(grade["小美"]["英文"][0])  # 60
# 取得小華的第二次國文成績
print(grade["小華"]["國文"][1])  # 60
# 印出每一位同學的國文段考平均成績
for name, subject in grade.items():
    avg = sum(subject["國文"]) / len(subject["國文"])
    print(f"{name}的國文成績平均數是{avg}")
# 印出每一位同學的總平均成績
for name, subject in grade.items():
    total = 0
    for score in subject.values():
        total += sum(score)
    avg = total / 9
    print(f"{name}的總平均成績是{avg:.2f}")

# 整理全校各科目的平均成績
# 1. 先找出所有的科目列表
subjects = grade["小明"].keys()
print(subjects)  # ['國文', '數學', '英文']

# 2.建立一個dict用來存放每一個科目的成績
avg_grade = {"國文": [], "數學": [], "英文": []}

# 3.逐一取得每一位同學的成績，並加總到對應的科目
for subject in subjects:  # 第一回sudjects = "國文"
    for name, score in grade.items():  # 第一回合每個人的"國文"成績串接
        avg_grade[subject] += score[subject]

# 4.計算各科目的平均成績
for subject, scores in avg_grade.items():
    avg = sum(scores) / len(scores)
    print(f"{subject}的平均成績是:{avg:.2f}")


from openai import OpenAI
import dotenv  # pip install python-dotenv -U
import os

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "developer",
            "content": "你是一個小幫手，只能用繁體中文和日文回應後續對話",
        },
        {"role": "user", "content": "你好(こんにちは)!"},
    ],
)

print(completion.choices[0].message.content)
