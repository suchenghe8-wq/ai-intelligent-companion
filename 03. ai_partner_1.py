import streamlit as st
import os
from openai import OpenAI

print("----------> 重新执行此文件 , 渲染展示页面")

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能朋朋",
    page_icon="👺",
    # 布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI智能某朋朋")

# Logo
st.logo("resources/logo.png")

# 系统提示词
system_prompt = "你是一名非常nice的AI助理，你的名字叫某朋朋，请你用温柔的语气回答用户的问题"

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 展示聊天信息
for message in st.session_state.messages: # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])


# 创建与AI大模型交互的客户端对象 (DEEPSEEK_API_KEY 环境变量的名字, 值就是DeepSeek的API_KEY的)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 消息输入框
prompt = st.chat_input("请输入您要问智能朋朋的问题")
if prompt: # 字符串会自动转换为布尔值, 如果字符串非空, 则为True; ""否则为False   要是不是user，前端展示的头像不同
    st.chat_message("user").write(prompt)
    print("----------> 调用AI大模型, 提示词: ", prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与AI大模型进行交互（参数）
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system",
             "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("<------------大模型返回的结果：",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})