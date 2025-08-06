# 异步迭代器

import asyncio # 直接导入该模块
class DistributedTaskManager: # 分布式任务管理
    class Node: # 任务信息节点
        def __init__(self, key):
            self.key = key
            self.next = None # 下个节点的应用
    def __init__(self): # 构造方法
        self.__root = None # 根节点
        self.__last = None # 最后一个节点
    def add_task_key(self, key): # 增加任务KEY
        newNode = DistributedTaskManager.Node(key = key); # 创建任务节点
        if self.__root == None: # 没有根节点
            self.__root = newNode # 设置根节点
            self.__last = newNode # 设置最后一个节点
        else: # 根节点存在
            self.__last.next = newNode
            self.__last = self.__last.next # 徐i该最后一个节点
    def __aiter__(self): # 返回迭代对象
        self.__current = self.__root # 设置当前的输出节点
        return self
    async def __anext__(self): # 下一个数据
        if self.__current == None: # 没有数据
            raise StopAsyncIteration() # 结束异步迭代
        key = self.__current.key # 获取任务KEY
        value = await self.task_server_search(key) # 模拟网络调用
        self.__current = self.__current.next # 修改当前引用
        return key, value
    async def task_server_search(self, task_key): # 消息回应处理
        await asyncio.sleep(2) # 模拟网络延迟
        if task_key == 'java': # 任务信息判断
            return 'Java程序设计开发实战'
        elif task_key == 'python':
            return 'Python开发实战'
        else: # 没有匹配KEY的时候
            return '编程技术开发实战大讲坛（公益活动）'
async def main(): # 主函数
    task_manager = DistributedTaskManager() # 创建分布式任务管理对象
    task_manager.add_task_key('python') # 添加任务KEY
    task_manager.add_task_key('java')
    task_manager.add_task_key('html')
    async for key, value in task_manager: # 异步迭代处理
        print('【任务信息】名称：%s、内容：%s' % (key, value))
if __name__ == '__main__':  # Python程序运行起点
    asyncio.run(main()) # 调用主函数
# 

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/多协程编程/Asynchronous iterator.py"
# 【任务信息】名称：python、内容：Python开发实战
# 【任务信息】名称：java、内容：Java程序设计开发实战
# 【任务信息】名称：html、内容：编程技术开发实战大讲坛（公益活动）