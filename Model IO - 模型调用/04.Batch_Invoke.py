#批次调用   并行处理多个独立请求

import os
import dotenv
from langchain_siliconflow import ChatSiliconFlow

dotenv.load_dotenv()

llm = ChatSiliconFlow(
    model='Qwen/Qwen3.5-122B-A10B',
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL'),
)

prompts = [
    '用一句话介绍北京',
    '用一句话介绍南京',
    '用一句话介绍西安',
]

responses = llm.batch(prompts)
# zip 把多个列表 / 序列，按位置一一配对打包，像拉链一样对齐组合
for p,r in zip(prompts, responses):
    print(f'P:{p}')
    print(f'R:{r.content}')