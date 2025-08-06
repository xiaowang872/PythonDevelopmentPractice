# asyncio编程

import asyncio # 直接导入该模块
async def message(): # 多协程处理函数
    print('沐言科技 —— 原创编程技术图书')
    await asyncio.sleep(1) # 等待1秒执行
    print('李兴华，《Python开发实战》')
def main(): # 主函数
    asyncio.run(message()) # 协程启动
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# 让当前协程（message()）暂停 1 秒，但不阻塞整个程序。

# 在这 1 秒内，事件循环（Event Loop）可以执行其他协程任务（如果有的话）。

# 1 秒后，该协程恢复执行，继续运行后面的代码。

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/多协程编程/asyncio programming.py"
# 沐言科技 —— 原创编程技术图书
# 李兴华，《Python开发实战》





import asyncio # 直接导入该模块
async def coroutine_task(author, book): # 任务处理函数
    await asyncio.sleep(2) # 休眠处理
    return f'【图书】名称：《{book}》、作者：{author}' # 任务的返回结果
async def coroutine_start(): # 多协程处理函数
    task_python = asyncio.create_task(
        coroutine_task('李兴华', 'Python开发实战'), name='YootkCoroutineTask - Python')
    task_java = asyncio.create_task(
        coroutine_task('李兴华', 'Java程序设计开发实战'), name='YootkCoroutineTask - Java')
    print(await task_python) # 等待任务执行
    print(await task_java) # 等待任务执行
def main(): # 主函数
    # 当前如果直接编写就在进程中启动多协程了，也可以先启动线程，在线程里面去启动多协程
    asyncio.run(coroutine_start()) # 协程启动
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【图书】名称：《Python开发实战》、作者：李兴华
# 【图书】名称：《Java程序设计开发实战》、作者：李兴华
# PS E:\summer_study\python开发\programe\pythonProject> 



import asyncio # 直接导入该模块
async def coroutine_task(author, book): # 任务处理函数
    for item in range(10): # 循环执行
        print('【%s】图书作者：%s、图书名称：《%s》' %
              (asyncio.current_task().get_name(), author, book))
        await asyncio.sleep(1) # 延迟1秒执行
async def coroutine_start(): # 协程启动
    tasks = [
        asyncio.create_task(coroutine_task(
            '李兴华', 'Python开发实战'), name='YootkCoroutineTask - Python'),
        asyncio.create_task(coroutine_task(
            '李兴华', 'Java程序设计开发实战'), name='YootkCoroutineTask - Java'),
        asyncio.create_task(coroutine_task(
            '李兴华', 'Go开发实战'), name='YootkCoroutineTask - Go'),
        asyncio.create_task(coroutine_task(
            '李兴华', 'MySQL开发实战'), name='YootkCoroutineTask - MySQL')]
    await asyncio.gather(*tasks) # 启动协程任务列表
def main(): # 主函数
    # 当前如果直接编写就在进程中启动多协程了，也可以先启动线程，在线程里面去启动多协程
    asyncio.run(coroutine_start()) # 协程启动
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# 【YootkCoroutineTask - Python】图书作者：李兴华、图书名称：《Python开发实战》
# 【YootkCoroutineTask - Go】图书作者：李兴华、图书名称：《Go开发实战》
# 【YootkCoroutineTask - Java】图书作者：李兴华、图书名称：《Java程序设计开发实战》
# 【YootkCoroutineTask - MySQL】图书作者：李兴华、图书名称：《MySQL开发实战》
# PS E:\summer_study\python开发\programe\pythonProject> 