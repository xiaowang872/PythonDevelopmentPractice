# process 实现多进程编程

import multiprocessing # 多进程的开发模块
import time # 时间模块，用于执行延迟操作
def process_core(delay, count): # 进程业务处理函数
    for num in range(count): # 循环执行
        print('【count = %d】进程ID：%s、进程名称：%s' %
              (num, multiprocessing.current_process().pid, # 获取进程编号
               multiprocessing.current_process().name)) # 获取进程的名称
        time.sleep(delay) # 进程调度延迟
def main(): # 主函数
    for item in range(3): # 循环3次，创建3个进程
        process = multiprocessing.Process(
            target=process_core,  # 定义进程执行的核心业务逻辑
            args=(1, 60, ), # 配置业务函数的参数内容
            name=f'YOOTK业务处理进程 - {item}') # 进程名称
        process.start() # 进程启动
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/多进程编程/process Implement multi-process programming.py"
# 【count = 0】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 0】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 0】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 1】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 1】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 1】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 2】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 2】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 2】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 3】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 3】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 3】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 4】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 4】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 4】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 5】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 5】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 5】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 6】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 6】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 6】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 7】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 7】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 7】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 8】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 8】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 8】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 9】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 9】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 9】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 10】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 10】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 10】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 11】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 11】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 11】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 12】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 12】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 12】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 13】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 13】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 13】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 14】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 14】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 14】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 15】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 15】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 15】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 16】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 16】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 16】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 17】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 17】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 17】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 18】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 18】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 18】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 19】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 19】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 19】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 20】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 20】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 20】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 21】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 21】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 21】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 22】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 22】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 22】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 23】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 23】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 23】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 24】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 24】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 24】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 25】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 25】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 25】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 26】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 26】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 26】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 27】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 27】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 27】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 28】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 28】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 28】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 29】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 29】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 29】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 30】进程ID：14156、进程名称：YOOTK业务处理进程 - 0
# 【count = 30】进程ID：31180、进程名称：YOOTK业务处理进程 - 1
# 【count = 30】进程ID：27560、进程名称：YOOTK业务处理进程 - 2
# 【count = 31】进程ID：14156、进程名称：YOOTK业务处理进程 - 0

##################################################################
import multiprocessing # 多进程的开发模块
def main(): # 主函数
    print('进程ID：%s、进程名称：%s' % (
        multiprocessing.current_process().pid, multiprocessing.current_process().name))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 进程ID：4080、进程名称：MainProcess
# PS E:\summer_study\python开发\programe\pythonProject> 


########################################
# 上面是通过面向过程的方式实现多进程
# 下面通过面向对象的方式实现多进程（不建议，有点烦）
import multiprocessing # 多进程的开发模块
import time # 时间模块，用于执行延迟操作
class ProcessCore(multiprocessing.Process): # 定义进程的核心逻辑
    def __init__(self, **kwargs):
        super().__init__(name=kwargs.get('name')) # 设置进程名称
        self.__delay = kwargs.get('delay') # 进程延迟时间
        self.__count = kwargs.get('count') # 循环执行次数
    # 所有的Python程序都是由主函数运行的，因此主函数是Python的起点
    # 而所有的进程也都有一个运行的起点，而这个起点是run()方法
    def run(self): # 进程起点方法，相当于进程中的主函数
        for num in range(self.__count): # 循环执行
            print('【count = %d】进程ID：%s、进程名称：%s' % (num,
                multiprocessing.current_process().pid,
                multiprocessing.current_process().name))
            time.sleep(self.__delay) # 进程延迟
def main(): # 主函数
    for item in range(3): # 循环3次，创建3个进程
        process = ProcessCore(name=f'YOOTK业务处理进程 - {item}', delay=1, count=5)
        # 不能直接调用类中的run()方法，因为run()方法只是定义了进程的执行业务逻辑，并不包含底层启动逻辑
        # Python之中的进程启动依靠Python虚拟机与操作系统交互而实现，而start()实现的就是这样的交互
        # start()方法与操作系统调用完成之后，会自动调用run()方法
        process.start() # 进程启动
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数



# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【count = 0】进程ID：11452、进程名称：YOOTK业务处理进程 - 0
# 【count = 0】进程ID：31128、进程名称：YOOTK业务处理进程 - 1
# 【count = 1】进程ID：11452、进程名称：YOOTK业务处理进程 - 0
# 【count = 0】进程ID：26892、进程名称：YOOTK业务处理进程 - 2
# 【count = 1】进程ID：31128、进程名称：YOOTK业务处理进程 - 1
# 【count = 2】进程ID：11452、进程名称：YOOTK业务处理进程 - 0
# 【count = 1】进程ID：26892、进程名称：YOOTK业务处理进程 - 2
# 【count = 2】进程ID：31128、进程名称：YOOTK业务处理进程 - 1
# 【count = 3】进程ID：11452、进程名称：YOOTK业务处理进程 - 0
# 【count = 2】进程ID：26892、进程名称：YOOTK业务处理进程 - 2
# 【count = 3】进程ID：31128、进程名称：YOOTK业务处理进程 - 1
# 【count = 4】进程ID：11452、进程名称：YOOTK业务处理进程 - 0
# 【count = 3】进程ID：26892、进程名称：YOOTK业务处理进程 - 2
# 【count = 4】进程ID：31128、进程名称：YOOTK业务处理进程 - 1
# 【count = 4】进程ID：26892、进程名称：YOOTK业务处理进程 - 2
# PS E:\summer_study\python开发\programe\pythonProject> 
