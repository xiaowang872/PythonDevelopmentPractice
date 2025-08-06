# 异步上下文处理

import asyncio # 直接导入该模块
class Message: # 实现网络消息处理
    class Connect: # 网络连接管理
        def build(self): # 建立网络连接
            print('【网络管理】与消息服务器建立网络连接。')
        def close(self): # 关闭网络连接
            print('【网络管理】关闭消息服务器网络连接。')
    def __init__(self): # 构造方法
        self.__result = 'Nothing' # 默认的结果
        self.__connect = Message.Connect() # 网络连接管理
    async def __aenter__(self): # 进入上下文
        self.__connect.build() # 建立网络连接
        return self
    async def __aexit__(self, exc_type, exc_val, exc_tb): # 关闭上下文
        print(self.__result) # 输出执行结果
        self.__connect.close() # 关闭网络连接
    async def message_handler(self, task): # 消息处理
        # 网络消息一定会存在有延迟问题，因此任务有可能不是立即完成的
        while not task.done(): # 任务没有完成
            await asyncio.sleep(1) # 等待任务完成
        else: # while不满足条件的时候执行
            self.__result = task.result() # 获取任务执行结果
async def message_echo(message): # 任务的处理函数
    await asyncio.sleep(2) # 延迟2秒
    return f'【ECHO】{message}' # 返回消息内容
async def main(): # 主函数
    async with Message() as msg: # 异步上下文
        task = asyncio.create_task(message_echo('李兴华，Python开发实战'))
        await msg.message_handler(task) # 消息处理
if __name__ == '__main__':  # Python程序运行起点
    asyncio.run(main()) # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/多协程编程/Asynchronous context processing.py"
# 【网络管理】与消息服务器建立网络连接。
# 【ECHO】李兴华，Python开发实战
# 【网络管理】关闭消息服务器网络连接。