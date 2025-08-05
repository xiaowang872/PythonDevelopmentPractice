# 装饰器的使用

# 一个父类可以被若干个子类所继承，每一个子类可以代表不同的实现
class MessageService: # 消息服务
    # Python之中的面向对象的结构优先，因此按照正常的设计来讲，此时应该通过接口（Python没有）定义
    def echo(self, msg): # 消息处理
        pass # 方法体为空
class NetMessageService(MessageService): # 网络消息
    def echo(self, msg): # 方法覆写
        return '【ECHO】' + msg # 消息处理
class MessageServiceProxy(MessageService): # 代理业务类
    def __init__(self, **kwargs): # 构造方法
        # 代理之中一定要保存有真实的业务对象
        self.__target = kwargs.get('target') # 获取代理的真实主题对象
    def log(self): # 进行日志记录
        print('【日志】调用echo()方法，进行消息处理。') # 辅助操作
    def echo(self, msg): # 代理中的echo()方法覆写
        self.log() # 调用辅助操作
        return self.__target.echo(msg) # 调用真实业务功能
def main(): # 主函数
    message = MessageServiceProxy(target=NetMessageService()) # 创建代理对象
    print(message.echo('YOOTK李兴华，《Python开发实战》'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/装饰器/The use of decorators.py"
# 【日志】调用echo()方法，进行消息处理。
# 【ECHO】YOOTK李兴华，《Python开发实战》


#####################################
# 更加完善

# # 一个父类可以被若干个子类所继承，每一个子类可以代表不同的实现
class MessageService: # 消息服务
    # Python之中的面向对象的结构优先，因此按照正常的设计来讲，此时应该通过接口（Python没有）定义
    def echo(self, msg): # 消息处理
        pass # 方法体为空
class NetMessageService(MessageService): # 网络消息
    def echo(self, msg): # 方法覆写
        return '【ECHO】' + msg # 消息处理
class MessageServiceProxy(MessageService): # 代理业务类
    def __init__(self, **kwargs): # 构造方法
        # 代理之中一定要保存有真实的业务对象
        self.__target = kwargs.get('target') # 获取代理的真实主题对象
    def connect(self): # 连接网络
        print('【连接】连接网络服务器，准备进行消息的发送')
        return True # 告诉连接成功
    def disconnect(self): # 断开网络
        print('【连接】网络消息处理完成，断开网络连接，释放Socket资源')
    def log(self): # 进行日志记录
        print('【日志】调用echo()方法，进行消息处理。') # 辅助操作
    def echo(self, msg): # 代理中的echo()方法覆写
        if self.connect(): # 连接处理
            self.log() # 调用辅助操作
            data = self.__target.echo(msg) # 调用真实业务功能
            self.disconnect() # 断开连接
            return data
def main(): # 主函数
    message = MessageServiceProxy(target=NetMessageService()) # 创建代理对象
    print(message.echo('YOOTK李兴华，《Python开发实战》'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/装饰器/The use of decorators.py"
# 【连接】连接网络服务器，准备进行消息的发送
# 【日志】调用echo()方法，进行消息处理。
# 【连接】网络消息处理完成，断开网络连接，释放Socket资源
# 【ECHO】YOOTK李兴华，《Python开发实战》


#########################################################
# 下面这个才是要学的
# 装饰器
# 所有的日志会存在有一个日志等级的设计，这样做的目的是为了便于日志采集
def log(level='INFO'): # 日志记录操作
    def wrapper(func): # 接收结构的名称
        def inner_wrapper(*args, **kwargs):
            print(f'[在inner_wrapper内部+{func.__name__}] - {level} {args} {kwargs}')
            return func(*args, **kwargs)
        return inner_wrapper # 返回内部函数对象
    return wrapper # 返回外部函数对象
class Message: # 网络消息
    @log(level='DEBUG')  # 装饰器（代理设计）
    def connect(self):  # 方法覆写
        # 此时写在方法里面的代码都属于核心业务功能
        print('【消息】建立网络连接。。。') # 核心功能
        return True
    @log() # 引用装饰器
    def echo(self, msg): # 方法覆写
        return '【ECHO】' + msg # 消息处理

def main(): # 主函数
    message = Message() # 实例化业务对象
    message.connect()
    print('#'*20)
    abc = message.echo('hello world')
    print(abc)
    print('#'*20)
    if message.connect(): # 调用了核心方法
        print(message.echo('YOOTK李兴华，《Python开发实战》'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/装饰器/The use of decorators.py"
# [在inner_wrapper内部+connect] - DEBUG (<__main__.Message object at 0x000002425185DED0>,) {}
# 【消息】建立网络连接。。。
# ####################
# [在inner_wrapper内部+echo] - INFO (<__main__.Message object at 0x000002425185DED0>, 'hello world') {}
# 【ECHO】hello world
# ####################
# [在inner_wrapper内部+connect] - DEBUG (<__main__.Message object at 0x000002425185DED0>,) {}
# 【消息】建立网络连接。。。
# [在inner_wrapper内部+echo] - INFO (<__main__.Message object at 0x000002425185DED0>, 'YOOTK李兴华，《Python开发实战》') {}
# 【ECHO】YOOTK李兴华，《Python开发实战》
##################################################

class Log: # 定义装饰器处理类
    def __init__(self, level='INFO'): # 构造方法接收参数
        self.__level = level # 保存日志级别
    def __call__(self, func): # 可调用对象
        def wrapper(*args, **kwargs): # 装饰器包装
            print(f'[{func.__name__}] - {self.__level} {args} {kwargs}')
            return func(*args, **kwargs)
        return wrapper
class Message: # 网络消息
    @Log(level='DEBUG')  # 装饰器（代理设计）
    def connect(self):  # 方法覆写
        # 此时写在方法里面的代码都属于核心业务功能
        print('【消息】建立网络连接。。。') # 核心功能
        return True
    @Log() # 引用装饰器
    def echo(self, msg): # 方法覆写
        return '【ECHO】' + msg # 消息处理

def main(): # 主函数
    message = Message() # 实例化业务对象
    message.connect()
    print('#'*20)
    abc = message.echo('hello world')
    print(abc)
    print('#'*20)
    if message.connect(): # 调用了核心方法
        print(message.echo('YOOTK李兴华，《Python开发实战》'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/装饰器/The use of decorators.py"
# [connect] - DEBUG (<__main__.Message object at 0x000001560F1EF2D0>,) {}
# 【消息】建立网络连接。。。
# ####################
# [echo] - INFO (<__main__.Message object at 0x000001560F1EF2D0>, 'hello world') {}
# 【ECHO】hello world
# ####################
# [connect] - DEBUG (<__main__.Message object at 0x000001560F1EF2D0>,) {}
# 【消息】建立网络连接。。。
# [echo] - INFO (<__main__.Message object at 0x000001560F1EF2D0>, 'YOOTK李兴华，《Python开发实战》') {}
# 【ECHO】YOOTK李兴华，《Python开发实战》
# PS E:\summer_study\python开发\programe\pythonProject> 