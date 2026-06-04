'''
性能对比
invoke 与 ainvoke 的测试
'''
import os
import dotenv
import time     #时间模块
import asyncio  #异步编程库 解锁异步并发
from langchain_siliconflow import ChatSiliconFlow

dotenv.load_dotenv()

llm = ChatSiliconFlow(
    model="deepseek-ai/DeepSeek-V4-Pro",
    api_key=os.getenv("GJ_API_KEY"),
    base_url=os.getenv("GJ_BASE_URL"),
)

# 测试问题
prompts = [
    '用一句话介绍北京',
    '用一句话介绍上海',
    '用一句话介绍郑州',
    '用一句话介绍洛阳'
]


# 同步调用 invoke
def test_invoke():
    start = time.time()
    for i, prompt in enumerate(prompts):  # i自动生成的序号/索引从 0 开始：0、1、2.....
        # enumerate() ，作用：遍历列表 / 元组等可迭代对象时，同时获取 → 索引（序号） + 元素本身
        print(f'[同步]正在发送第{i + 1}个请求')
        llm.invoke(prompt)  # 等待上一请求结束 才继续下一请求
    print(f'总耗时:{time.time() - start:.2f}s')


# 异步调用 ainvoke
'''
await 异步等待，等待所有任务完成 才走下面的代码
gather 并发执行多个任务，最后统一收集所有结果     
* 解包运算符 把列表拆分成独立的参数传给 gather
'''


async def test_ainvoke():
    start = time.time()
    print('[异步] 瞬间派发所有请求')

    # 遍历批量提示词 prompts，为每一条提示词创建一个异步调用任务，并把所有任务打包成 tasks 列表。
    tasks = [llm.ainvoke(prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(f'回答:{r.content[:20]}...')  # 只截取回答的前20个字符

    print(f'总耗时:{time.time() - start:.2f}s')


async def main():
    test_invoke()
    await test_ainvoke()


if __name__ == '__main__':
    asyncio.run(main())

'''
[同步]正在发送第1个请求
[同步]正在发送第2个请求
[同步]正在发送第3个请求
[同步]正在发送第4个请求
总耗时:85.83s
[异步] 瞬间派发所有请求
回答:北京是一座将千年古都的沉稳庄重与现代化国...
回答:上海是东方明珠，一座融合外滩万国建筑历史...
回答:**郑州是位于“天地之中”的河南省会，既...
回答:洛阳是一座承载十三朝古都辉煌、绽放国色牡...
总耗时:10.09s
'''
