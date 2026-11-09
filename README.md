# 小工具箱（Streamlit 最小可用应用）

一个最小可用的 Streamlit 应用：字数统计 + 随机数据折线图。
建这个仓库的目的是在 Streamlit Community Cloud 上有一个可部署的应用，
用来申请 Snowflake Cortex Code 免费 12 个月（申请截止 2026-11-30）。

## 部署到 Streamlit Community Cloud

1. 在 GitHub 新建一个**公开**仓库，把 `app.py` 和 `requirements.txt` 传上去。
2. 打开 https://share.streamlit.io ，用 GitHub 账号登录。
3. 点 **New app**，选刚建的仓库和分支，主文件填 `app.py`，点 **Deploy**。
4. 等几分钟，部署成功后会得到一个 `https://xxx.streamlit.app` 的地址。

## 申请 Cortex Code 免费 12 个月

部署成功后去 https://streamlit.io/coco-offer 点 **Apply now** 填表（约 2 分钟），
审核通过后会邮件发来专属注册链接。申请截止 2026-11-30，先到先审。
