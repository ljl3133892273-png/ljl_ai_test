'''
机试题二：
1.  通过硅基流动或者其他任意平台对接大语言模型（LLM）
2.  通过批量调用的方式问任意3个问题
3.  最后统计Token消耗并输出
4.  将源代码上传到GitHub仓库
5.  运行结果截图发群里
'''

import dotenv
import os
from langchain_siliconflow import ChatSiliconFlow
from langchain_core.callbacks import get_usage_metadata_callback

dotenv.load_dotenv()

llm = ChatSiliconFlow(
    model="deepseek-ai/DeepSeek-V4-Pro",
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL'),
)

prompts = [
    '用一句话介绍北京',
    '用一句话介绍郑州',
    '用一句话介绍洛阳'
]
with get_usage_metadata_callback() as cb:
    responses = llm.batch(prompts)
    for q, r in zip(prompts, responses):
        print(f'q:{q}')
        print(f'R:{r.content}')
    print(f'token消耗详情:{cb.usage_metadata}')
