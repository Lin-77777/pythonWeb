**Python 課程筆記**

---

### **1. 成績登記系統**
這個系統使用字典（dict）來儲存學生的成績，學生姓名為 key，每位學生的成績以科目為分類，並包含三次考試的成績。

#### **程式碼與解釋**
```python
# 成績登記系統，key是學生的名字，value是學生的成績，每個科目有三個成績
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 90, 100], "英文": [70, 60, 50]},
    "小美": {"國文": [80, 70, 60], "數學": [90, 80, 70], "英文": [60, 50, 40]},
    "小華": {"國文": [70, 60, 50], "數學": [80, 70, 60], "英文": [50, 40, 30]},
}
```

#### **(1) 取得特定學生的成績**
```python
# 取得小明的數學成績
print(grade["小明"]["數學"])  # [85, 90, 100]

# 取得小美的第一次英文成績
print(grade["小美"]["英文"][0])  # 60

# 取得小華的第二次國文成績
print(grade["小華"]["國文"][1])  # 60
```

#### **(2) 計算每位學生的國文平均成績**
```python
for name, subject in grade.items():
    avg = sum(subject["國文"]) / len(subject["國文"])
    print(f"{name}的國文成績平均數是{avg}")
```

#### **(3) 計算每位學生的總平均成績**
```python
for name, subject in grade.items():
    total = 0
    for score in subject.values():
        total += sum(score)
    avg = total / 9
    print(f"{name}的總平均成績是{avg:.2f}")
```

#### **(4) 計算全校各科目的平均成績**
```python
# 1. 先找出所有的科目列表
subjects = grade["小明"].keys()
print(subjects)  # ['國文', '數學', '英文']

# 2. 建立一個字典用來存放每一個科目的成績
avg_grade = {"國文": [], "數學": [], "英文": []}

# 3. 逐一取得每一位同學的成績，並加總到對應的科目
for subject in subjects:
    for name, score in grade.items():
        avg_grade[subject] += score[subject]

# 4. 計算各科目的平均成績
for subject, scores in avg_grade.items():
    avg = sum(scores) / len(scores)
    print(f"{subject}的平均成績是:{avg:.2f}")
```

---

### **2. OpenAI API 應用**
使用 OpenAI API 進行對話，並設置特定的語言回應（繁體中文與日文）。

```python
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
```

---

### **3. Streamlit 應用 - 聊天 AI**
這個應用程式使用 Streamlit 建立簡單的 AI 聊天機器人。

```python
import streamlit as st
from openai import OpenAI
import dotenv  # pip install python-dotenv -U
import os
import menu

menu.menu()
dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("聊天AI")
if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入文字")

if message:
    st.session_state.history.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "developer",
                "content": "你是一個小幫手，只能用繁體中文(#zh-TW)和日文(#ja-JP)回應後續對話",
            }
        ]
        + st.session_state.history,
    )
    st.session_state.history.append(
        {"role": "assistant", "content": completion.choices[0].message.content}
    )
    st.rerun()  # 重新整理頁面
```

---

### **4. Streamlit 應用 - 猜謎遊戲**
這個應用建立了一個簡單的猜謎遊戲，使用者可以與 AI 互動。

```python
import streamlit as st
from openai import OpenAI
import dotenv  # pip install python-dotenv -U
import os
import menu

menu.menu()
dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tempereature = 1  # 調整自由度0最不自由，1最自由

st.title("猜謎遊戲")
if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入文字")

if message:
    st.session_state.history.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        messages=[
            {
                "role": "developer",
                "content": "請跟使用者玩一場猜謎遊戲，你需要先描述題目，接下來依照使用者回應的猜測給予提示。提示只能說[是]與[否]，不可以提供太多資訊。",
            }
        ]
        + st.session_state.history,
    )
    st.session_state.history.append(
        {"role": "assistant", "content": completion.choices[0].message.content}
    )
    st.rerun()  # 重新整理頁面
```

