"""小工具箱：一个最小可用的 Streamlit 应用。

功能：
1. 粘贴文字，统计字符数 / 词数 / 行数
2. 滑块控制数据点数，画一条随机数据折线图

部署到 Streamlit Community Cloud 只需要这个文件 + requirements.txt。
"""

import random

import streamlit as st

st.set_page_config(page_title="小工具箱", page_icon="🧰")

st.title("小工具箱")
st.write("一个最小可用的 Streamlit 应用：字数统计 + 随机数据折线图。")

text = st.text_area("粘贴一段文字，统计字数", height=120)
if text:
    chars = len(text)
    words = len(text.split())
    lines = text.count("\n") + 1
    c1, c2, c3 = st.columns(3)
    c1.metric("字符数", chars)
    c2.metric("词数", words)
    c3.metric("行数", lines)

st.divider()
st.subheader("随机数据折线图")
n = st.slider("数据点数", 10, 100, 30)
random.seed(42)
data = [random.randint(0, 100) for _ in range(n)]
st.line_chart(data)
