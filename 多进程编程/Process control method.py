# 进程控制方法

import multiprocessing, time
def process_core(): # 进程业务处理函数
    time.sleep(5) # 进程休眠5秒
    print('【业务处理】进程ID：%s、进程名称：%s' %
          (multiprocessing.current_process().pid,  # 获取进程编号
           multiprocessing.current_process().name))  # 获取进程的名称
def main(): # 主函数
    # 每一个Python应用都会提供有一个主进程
    process = multiprocessing.Process(target=process_core,name='YootkProcess') # 创建子进程
    process.start() # 进程启动
    # process.join() # 子进程强制执行
    print('【%s】YOOTK业务处理完毕，应用进程结束！' % multiprocessing.current_process().name)
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/多进程编程/Process control method.py"
# 【MainProcess】YOOTK业务处理完毕，应用进程结束！
# 【业务处理】进程ID：27988、进程名称：YootkProcess
# PS E:\summer_study\python开发\programe\pythonProject> 


##################################################


import multiprocessing, time
def process_core(): # 进程业务处理函数
    time.sleep(5) # 进程休眠5秒
    print('【业务处理】进程ID：%s、进程名称：%s' %
          (multiprocessing.current_process().pid,  # 获取进程编号
           multiprocessing.current_process().name))  # 获取进程的名称
def main(): # 主函数
    # 每一个Python应用都会提供有一个主进程
    process = multiprocessing.Process(target=process_core,name='YootkProcess') # 创建子进程
    process.start() # 进程启动
    process.join() # 子进程强制执行
    print('【%s】YOOTK业务处理完毕，应用进程结束！' % multiprocessing.current_process().name)
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【业务处理】进程ID：25428、进程名称：YootkProcess
# 【MainProcess】YOOTK业务处理完毕，应用进程结束！



import multiprocessing, time
def process_core(): # 进程业务处理函数
    time.sleep(5) # 进程休眠5秒
    print('【业务处理】进程ID：%s、进程名称：%s' %
          (multiprocessing.current_process().pid,  # 获取进程编号
           multiprocessing.current_process().name))  # 获取进程的名称
def main(): # 主函数
    # 每一个Python应用都会提供有一个主进程
    process = multiprocessing.Process(target=process_core,name='YootkProcess') # 创建子进程
    process.start() # 子进程启动
    time.sleep(2) # 活个2秒
    if process.is_alive():# 进程还活着？
        process.terminate() # 主进程关闭子进程
        print('【%s】进程执行中断运行。' % process.name)
    print('【%s】YOOTK业务处理完毕，应用进程结束！' % multiprocessing.current_process().name)
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【YootkProcess】进程执行中断运行。
# 【MainProcess】YOOTK业务处理完毕，应用进程结束！
# PS E:\summer_study\python开发\programe\pythonProject> 