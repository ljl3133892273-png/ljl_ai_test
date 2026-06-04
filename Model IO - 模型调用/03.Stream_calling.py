# 流式调用 stream
import os
import dotenv
import time
import asyncio
from langchain_siliconflow import ChatSiliconFlow


dotenv.load_dotenv()

llm = ChatSiliconFlow(
    model='Qwen/Qwen3.5-122B-A10B',
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL'),
    temperature=0.5     #温度
)

print('AI....回答:')
full_msg = None     #存放模型返回的消息
for chunk in llm.stream('请简短的介绍一下郑州这座城市'):
    #三元表达式  如果是空 返回第一个字
    full_msg = chunk if full_msg is None else full_msg + chunk
    #end 不换行 ；flush 强制立即打印输出，不缓存、不等待 流式输出必加参数
    print(chunk.content,end='',flush=True)
    time.sleep(0.05)

print('\n----------------------')
print(f'完整消息:{full_msg.content}')

