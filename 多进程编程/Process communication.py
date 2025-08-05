# 进程通讯
import multiprocessing, time
def message_send(connect, msg): # 进程消息发送
    # connect表示要发送的管道对象
    connect.send(msg) # 数据发送操作
def message_receive(connect): # 进程消息读取
    print('【数据接收】%s' % connect.recv()) # 输出消息数据
def main(): # 主函数
    # 在创建管道的时候一般会返回两个对象，一个是进行输入管道，另外一个是输出管道
    connect_receive, connect_send = multiprocessing.Pipe() # 创建进程通讯管道
    # 管道创建完成之后，下面就需要根据管道来创建进程，因为每一个进程处理函数之中都需要接收管道对象
    process_send = multiprocessing.Process(target=message_send,
                                           args=(connect_send, ['Python', 'Java', 'Go']))
    # 创建接收进程
    process_receive = multiprocessing.Process(target=message_receive,
                                              args=(connect_receive,))
    process_receive.start() # 启动接收进程
    process_send.start() # 启动发送进程
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/多进程编程/Process communication.py"
# 【数据接收】['Python', 'Java', 'Go']
# PS E:\summer_study\python开发\programe\pythonProject> 




import multiprocessing, time
def process_share(data, key, value): # 进程处理函数
    data.update({key : value}) # 更新字典
def main(): # 主函数
    manager = multiprocessing.Manager() # 创建数据共享管理
    # 这个时候的字段是适合于多进程数据共享操作的字典结构
    process_dict = manager.dict(author='YOOTK - 李兴华') # 创建字典对象
    # 提示：Python之中的字典虽然作为了原始的基础数据类型而提供，但是本质上是属于数据结构的实现
    process_a = multiprocessing.Process(target=process_share,
                                        args=(process_dict, 'python', '《Python开发实战》',))
    process_b = multiprocessing.Process(target=process_share,
                                        args=(process_dict, 'java', '《Java程序设计开发实战》',))
    process_a.start() # 子进程启动
    process_b.start() # 子进程启动
    # 当前的主函数为主进程，此时一共会启动三个进程
    process_a.join() # 子进程强制运行
    process_b.join() # 子进程强制运行
    print('【主进程】观察字典中的数据内容：%s' % process_dict)
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数




# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【主进程】观察字典中的数据内容：{'author': 'YOOTK - 李兴华', 'python': '《Python开发实战》', 'java': '《Java程序设计开发实战》'}
# PS E:\summer_study\python开发\programe\pythonProject> 