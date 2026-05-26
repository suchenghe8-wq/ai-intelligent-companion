import streamlit as st

st.set_page_config(page_title="测试", initial_sidebar_state="expanded")

st.title("侧边栏测试")

with st.sidebar:
    st.subheader("测试侧边栏")
    st.write("如果看到这个，说明侧边栏正常")

st.write("主内容区")
