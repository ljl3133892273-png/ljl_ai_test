'''
核心参数
llm = ChatOpenAI(
    api_key=os.getenv('API_KEY'),
    base_url=os.getenv('BASE_URL'),
    model="gpt-4o-mini",       # 模型名称（必填）
    temperature=0.7,            # 随机性，0=确定性，1=有创意（默认因模型而异）
    max_tokens=1000,            # 最大输出长度
    timeout=60,                 # 超时时间（秒）
    max_retries=2,              # 失败重试次数
)
'''

'''
消息类型
| 消息类型     | 类名            | 用途                     | 示例                   |
| ------------ | --------------- | ------------------------ | ---------------------- |
| **系统消息** | `SystemMessage` | 设定AI的行为、角色和规则 | "你是一个有帮助的助手" |
| **用户消息** | `HumanMessage`  | 用户的输入               | "帮我解释一下量子计算" |
| **AI消息**   | `AIMessage`     | AI的回复，可用于对话历史 | "量子计算是..."        |
| **工具消息** | `ToolMessage`   | 工具执行返回的结果       | 工具调用的输出         |
系统定规则，用户提问题，AI给回复，工具报结果。
'''

'''
传入方式
| 你的需求                           | 推荐方式     | 代码示例                                              |
| ---------------------------------- | ------------ | ----------------------------------------------------- |
| **简单问答**，不需要上下文         | 直接传字符串 | `llm.invoke("你好")`                                  |
| **需要角色设定**或**对话历史**     | 传消息列表   | `llm.invoke([SystemMessage(...), HumanMessage(...)])` |
| **动态构建**消息，或从其他格式转换 | 用元组/字典  | `llm.invoke([("system", "..."), ("user", "...")])`    |
'''

'''
字符串方式
llm.invoke("你好，介绍一下LangChain")
**适用场景**：
- 单轮问答，不需要上下文
- 不需要设定 AI 的角色或行为规则
- 快速测试或调试
**优势**：代码最简洁，一行搞定
**局限**：无法保留对话历史，无法设定系统提示词
'''

'''
消息列表
llm.invoke([
    SystemMessage(content="你是一个专业的Python编程助手"),
    HumanMessage(content="什么是装饰器？")
])
**适用场景**：
- 需要**设定 AI 角色**（比如"你是一个翻译助手"）
- 需要**保留对话历史**
- 需要**区分**系统指令/用户输入/AI回复
**实战示例：多轮对话**
'''

'''
使用元组或者字典
元组方式：(角色, 内容)
tuple_messages = [
    ("system", "你是一个专业的Python编程助手"),
    ("user", "什么是装饰器？")
]

# 字典方式：{"role": 角色, "content": 内容}
dict_messages = [
    {"role": "system", "content": "你是一个专业的Python编程助手"},
    {"role": "user", "content": "什么是装饰器？"}
]

print(llm.invoke(tuple_messages))
print(llm.invoke(dict_messages))
**适用场景**：
- 从 API 返回的 JSON 数据直接转成消息列表
- 从配置文件或数据库读取对话模板
- 动态构建消息列表
'''


'''
调用方式:

同步调用 - invoke
适用场景：
- 单次调用，不需要高并发
- 简单问答、文本生成
- 快速原型开发

异步调用 - ainvoke
适用于需要同时处理多个请求的高并发场景

简单的异步调用:
import asyncio
import dotenv
import os
from langchain_siliconflow import ChatSiliconFlow

dotenv.load_dotenv()
llm = ChatSiliconFlow(
    model="deepseek-ai/DeepSeek-V4-Pro",
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL'),
)

async def yibudiaoyong_llm():
    res = await llm.ainvoke('请用一句话介绍你的同行gemini')
    print(res.content)

asyncio.run(yibudiaoyong_llm())
'''

'''
流式调用 stream()   打字机效果
适用场景：
- 聊天机器人、对话系统
- 长文本生成（让用户看到进度）
- 实时交互应用
'''

'''
批次调用 batch() 并行处理多个独立请求
适用场景：
- 批量处理多个独立请求
- 数据分析、批量内容生成
- 不需要按顺序返回结果

批量异步调用 abatch
async def batch_async():
    questions = [
        "什么是LangChain？",
        "LangChain的核心组件有哪些？",
        "如何使用LangChain构建Agent？"
    ]
    responses = await llm.abatch(questions)
    for q, r in zip(questions, responses):
        print(f"Q: {q}\nA: {r.content}\n")

await batch_async()
'''


