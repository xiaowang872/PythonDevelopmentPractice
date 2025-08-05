# 进程池,进程一般为cpu核数*2
# 多进程不适合高并发操作，只适合高并发计算操作而不适合IO操作
import multiprocessing, time
def process_task(item): # 进程业务任务
    if item == 2: # 设置一个判断条件
        raise NotImplemented('业务步骤错误，执行中断！')
    time.sleep(1) # 模拟业务的延迟
    return f'“{multiprocessing.current_process().name}”进程，业务处理步骤：{item}'
def process_task_callback(result): # 进程处理的回调操作
    print('【业务回调】%s' % result) # 回调操作输出
def process_task_error(err): # 错误处理
    print('【业务错误】%s' % err)
def main(): # 主函数
    process_pool = multiprocessing.Pool(
        processes=multiprocessing.cpu_count() * 2) # 创建进程池
    # 此时将创建许多的进程，这个进程是通过进程池来进行创建管理的
    for item in range(500): # 循环创建进程
        result = process_pool.apply_async(func=process_task, args=(item,), # 进程任务的配置
                                          callback=process_task_callback, # 业务回调处理（进程执行完之后）
                                          error_callback=process_task_error); # 错误回调处理
        print(result.get()) # 进程执行完成，触发callback()操作
    process_pool.close() # 关闭进程池
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/多进程编程/process pool.py"
# 【业务回调】“SpawnPoolWorker-1”进程，业务处理步骤：0
# “SpawnPoolWorker-1”进程，业务处理步骤：0
# 【业务回调】“SpawnPoolWorker-2”进程，业务处理步骤：1
# “SpawnPoolWorker-2”进程，业务处理步骤：1
# 【业务错误】'NotImplementedType' object is not callable
# multiprocessing.pool.RemoteTraceback: 
# """
# Traceback (most recent call last):
#   File "D:\python_install_file\Lib\multiprocessing\pool.py", line 125, in worker
#     result = (True, func(*args, **kwds))
#                     ^^^^^^^^^^^^^^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\多进程编程\process pool.py", line 5, in process_task
#     raise NotImplemented('业务步骤错误，执行中断！')
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: 'NotImplementedType' object is not callable
# """

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "e:\summer_study\python开发\programe\pythonProject\多进程编程\process pool.py", line 23, in <module>
#     main() # 调用主函数
#     ^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\多进程编程\process pool.py", line 20, in main
#     print(result.get()) # 进程执行完成，触发callback()操作
#           ^^^^^^^^^^^^
#   File "D:\python_install_file\Lib\multiprocessing\pool.py", line 774, in get
#     raise self._value
# TypeError: 'NotImplementedType' object is not callable
# PS E:\summer_study\python开发\programe\pythonProject> 