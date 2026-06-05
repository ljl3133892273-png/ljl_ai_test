'''
机试题三：
1.  通过硅基流动或者其他任意平台对接大语言模型（LLM）
2.  模拟一段历史消息对话包含 人类 AI 系统 三种角色和LLM对话
3.  最后统计Token消耗并输出
4.  将源代码上传到GitHub仓库
5.  运行结果截图发群里
'''
import dotenv
import os
from langchain_siliconflow import ChatSiliconFlow

from langchain_core.callbacks import get_usage_metadata_callback
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

dotenv.load_dotenv()

llm = ChatSiliconFlow(
    model="deepseek-ai/DeepSeek-V4-Pro",
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL'),
)

tasks = [
    SystemMessage(content='你是一个情感专家'),
    HumanMessage(content='你好'),
    AIMessage(content='你好，请问我有什么可以帮助你的？'),
    HumanMessage(content='我应该怎么跟我喜欢人聊天(简短一点)')
]

with get_usage_metadata_callback() as cb:
    res = llm.invoke(tasks)
    print(res.content)
    print(f'token消耗详情:{cb.usage_metadata}')
