# 多协程编程简介
##################################
# 原始的版本
import time # 让程序执行慢一点
def message_producer(author, book, consumer): # 消息生产者
    message = None # 空消息
    # 在使用yield进行手工协程实现的时候，一定要首先发送一个空消息
    consumer.send(message) # 在进行处理之前首先要发送一个空消息
    for num in range(3): # 循环数据生产
        message = f'《{book}》，图书作者：YOOTK - {author}' # 消息内容
        time.sleep(1) # 人为的延迟
        print('【生产者】%s' % message) # 信息输出
        # consumer 是一个协程（coroutine）对象，它通过 send() 方法接收来自 message_producer 的消息。
        consumer.send(message) # 消息输出
def message_consumer(): # 消息消费者
    while True: # 持续循环
        result = yield  # 等待数据返回
        print('【消费者】%s' % result)
def main(): # 主函数
    consumer = message_consumer() # 获取函数引用
    message_producer('李兴华', 'Python开发实战', consumer) # 数据生产
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# yield 是 Python 中的一个关键字，用于定义生成器函数（Generator Function）或协程（Coroutine）。它的作用类似于 return，但不同之处在于：

# return：函数执行到 return 时会立即终止，并返回一个值，之后函数调用结束。

# yield：函数执行到 yield 时会暂停，并返回一个值，但函数的状态会被保存，下次调用时可以从 yield 处继续执行。


###################################
# 原使
import time # 让程序执行慢一点
import gevent # pip install gevent
# 不管是多进程启动的协程还是多线程启动的协程，都可以共享进程和线程之间的数据
message = None # 保存公共数据，全局变量
def message_producer(author, book): # 消息生产者
    global message # 使用全局变量
    for num in range(3): # 循环数据生产
        message = f'《{book}》，图书作者：YOOTK - {author}' # 消息内容
        time.sleep(1) # 人为的延迟
        print('【生产者】%s' % message) # 信息输出
        gevent.sleep(1) # 协程切换延迟
def message_consumer(): # 消息消费者
    while True: # 持续循环
        print('【消费者】%s' % message) # 输出全局变量的数据
        gevent.sleep(1) # 协程切换延迟
def main(): # 主函数
    producer_gevent = gevent.spawn(message_producer, '李兴华', 'Python开发实战')
    consumer_gevent = gevent.spawn(message_consumer)
    producer_gevent.join() # 协程强制运行
    consumer_gevent.join() # 协程强制运行
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【生产者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【消费者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【生产者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【消费者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【生产者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【消费者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【消费者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【消费者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【消费者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【消费者】《Python开发实战》，图书作者：YOOTK - 李兴华
# 【消费者】《Python开发实战》，图书作者：YOOTK - 李兴华
