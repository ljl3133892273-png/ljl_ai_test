#消息类型
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import dotenv
import os
# 硅基流动
from langchain_siliconflow import ChatSiliconFlow
dotenv.load_dotenv()

'''
基础消息类型
llm = ChatSiliconFlow(
    model="deepseek-ai/DeepSeek-V4-Pro",
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL'),
)
res = llm.invoke([HumanMessage(content='请用一句话介绍豆包')])   #当前角色:用户
print(res.content)
'''

'''
模拟多轮对话
conversation = [
    SystemMessage(content="你是一个有帮助的AI助手"),  #系统消息 定人设
    HumanMessage(content="你好"),   #用户消息
    AIMessage(content="你好！有什么我可以帮助你的吗？"),   #AI消息
    HumanMessage(content="请用一句话帮我介绍你的同行豆包"),    #第二轮对话
]

llm = ChatSiliconFlow(
    model="deepseek-ai/DeepSeek-V4-Pro",
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL'),
)
res = llm.invoke(conversation)  #传入列表
print(res.content)
'''


#   字典类型
# 假设这是从配置文件读取的
prompt_template = [
    {"role": "system", "content": "你是一个{role}"},
    {"role": "user", "content": "请解释{topic}"}
]
# 动态填充
messages = [  # 列表推导式
    {
        "role": t["role"],
        "content": t["content"].format(
            role="翻译助手",
            topic="机器翻译",
        ),
    }
    for t in prompt_template
]

# 生成普通字典列表--->
# messages = [
#     {"role": "system", "content": "你是一个翻译助手"},
#     {"role": "user", "content": "请解释机器翻译"}  # 注意：没有「一下」
# ]

llm = ChatSiliconFlow(
    model="deepseek-ai/DeepSeek-V4-Pro",
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL'),
)
print(llm.invoke(messages).content)
