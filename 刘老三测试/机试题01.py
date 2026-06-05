'''
机试题一：
1.  通过硅基流动或者其他任意平台对接大语言模型（LLM）
2.  通过异步非流式的方式让AI写歌
3.  最后统计Token消耗并输出
4.  将源代码上传到GitHub仓库
5.  运行结果截图发群里
'''

import os
import dotenv
from langchain_siliconflow import ChatSiliconFlow
import asyncio

from langchain_core.callbacks import get_usage_metadata_callback

dotenv.load_dotenv()

llm = ChatSiliconFlow(
    model='deepseek-ai/DeepSeek-V4-Pro',
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL'),
)


async def test_ainvoke():
    with get_usage_metadata_callback() as cb:
        response = await llm.ainvoke('帮我简短写一首歌')
        print(response.content)
        print(f'token消耗详情:{cb.usage_metadata}')


if __name__ == '__main__':
    asyncio.run(test_ainvoke())
