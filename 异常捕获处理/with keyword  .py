# with 关键字
class Message: # 消息处理类
    class Connect: # 连接管理类
        def build(self): # 建立网络连接
            print('【网络连接】建立专属网络通道。')
            return True
        def close(self):
            print('【网络连接】关闭网络通道。')
    def echo(self, msg): # 消息处理
        connect = Message.Connect() # 消息连接
        if connect.build():
            content = '【ECHO】' + msg # 消息处理
            connect.close() # 关闭连接
            return content
        else:
            return None
def main(): # 主函数
    message = Message()
    print(message.echo('Python开发实战'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/异常捕获处理/with keyword  .py"
# 【网络连接】建立专属网络通道。
# 【网络连接】关闭网络通道。
# 【ECHO】Python开发实战


class Message: # 消息处理类
    class Connect: # 连接管理类
        def build(self): # 建立网络连接
            print('【网络连接】建立专属网络通道。')
            return True
        def close(self):
            print('【网络连接】关闭网络通道。')
    def echo(self, msg): # 消息处理
        connect = Message.Connect() # 消息连接
        if connect.build():
            content = '【ECHO】' + msg # 消息处理
            connect.close() # 关闭连接
            return content
        else:
            return None
    def __enter__(self): # 进入上下文操作
        print('【__enter__】上下文初始化')
    def __exit__(self, exc_type, exc_val, exc_tb): # 上下文关闭
        print('【__exit__】上下文销毁，异常类型：%s、异常内容：%s、异常跟踪：%s' % (exc_type, exc_val, exc_tb))
def main(): # 主函数
    with Message() as message: # 自动开启了上下文
        # print(message.echo('Python开发实战'))
        pass
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【__enter__】上下文初始化
# 【__exit__】上下文销毁，异常类型：None、异常内容：None、异常跟踪：None

class Message: # 消息处理类
    class Connect: # 连接管理类
        def build(self): # 建立网络连接
            print('【网络连接】建立专属网络通道。')
            return True
        def close(self):
            print('【网络连接】关闭网络通道。')
    def echo(self, msg): # 消息处理
        return '【ECHO】' + msg # 消息处理
    def __enter__(self): # 进入上下文操作
        self.__connect = Message.Connect() # 创建连接对象
        if self.__connect.build(): # 连接建立成功
            print('【消息处理】网络通道创建成功，可以实现消息处理机制。')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): # 上下文关闭
        print('【__exit__】上下文销毁，异常类型：%s、异常内容：%s、异常跟踪：%s' % (exc_type, exc_val, exc_tb))
        self.__connect.close() # 关闭网络连接
        # 返回True表示当前的程序已经全部正确的处理完毕（异常都已经处理了）
        # 返回False表示当前的程序没有处理异常，交给调用处来进行异常处理
        return True
def main(): # 主函数
    with Message() as message: # 自动开启了上下文
        print(message.echo('Python开发实战'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【网络连接】建立专属网络通道。
# 【消息处理】网络通道创建成功，可以实现消息处理机制。
# 【ECHO】Python开发实战
# 【__exit__】上下文销毁，异常类型：None、异常内容：None、异常跟踪：None
# 【网络连接】关闭网络通道。


########################################
# 如果连接失败，返回False，他的结果
class Message: # 消息处理类
    class Connect: # 连接管理类
        def build(self): # 建立网络连接
            print('【网络连接】建立专属网络通道。')
            return False
        def close(self):
            print('【网络连接】关闭网络通道。')
    def echo(self, msg): # 消息处理
        return '【ECHO】' + msg # 消息处理
    def __enter__(self): # 进入上下文操作
        self.__connect = Message.Connect() # 创建连接对象
        if self.__connect.build(): # 连接建立成功
            print('【消息处理】网络通道创建成功，可以实现消息处理机制。')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): # 上下文关闭
        print('【__exit__】上下文销毁，异常类型：%s、异常内容：%s、异常跟踪：%s' % (exc_type, exc_val, exc_tb))
        self.__connect.close() # 关闭网络连接
        # 返回True表示当前的程序已经全部正确的处理完毕（异常都已经处理了）
        # 返回False表示当前的程序没有处理异常，交给调用处来进行异常处理
        return True
def main(): # 主函数
    with Message() as message: # 自动开启了上下文
        print(message.echo('Python开发实战'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【网络连接】建立专属网络通道。
# 【ECHO】Python开发实战
# 【__exit__】上下文销毁，异常类型：None、异常内容：None、异常跟踪：None
# 【网络连接】关闭网络通道。

########################################

class NotSupportException(Exception): # 自定义异常类型
    def __init__(self, **kwargs):
        self.__msg = kwargs.get('msg')
    def __str__(self):
        return self.__msg
class Message: # 消息处理类
    class Connect: # 连接管理类
        def build(self): # 建立网络连接
            print('【网络连接】建立专属网络通道。')
            return True
        def close(self):
            print('【网络连接】关闭网络通道。')
    def echo(self, msg): # 消息处理
        return '【ECHO】' + msg # 消息处理
    def __enter__(self): # 进入上下文操作
        self.__connect = Message.Connect() # 创建连接对象
        if self.__connect.build(): # 连接建立成功
            print('【消息处理】网络通道创建成功，可以实现消息处理机制。')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): # 上下文关闭
        print('【__exit__】上下文销毁，异常类型：%s、异常内容：%s、异常跟踪：%s' % (exc_type, exc_val, exc_tb))
        self.__connect.close() # 关闭网络连接
        # 返回True表示当前的程序已经全部正确的处理完毕（异常都已经处理了）
        # 返回False表示当前的程序没有处理异常，交给调用处来进行异常处理
        return True
def main(): # 主函数
    with Message() as message: # 自动开启了上下文
        print(message.echo('Python开发实战'))
        raise NotSupportException(msg='网络通道建立失败，无法进行消息处理。')
         # 下面这个无法被执行到
        print(message.echo('Redis开发实战'))
    print('【完结】网络消息处理完成。')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【网络连接】建立专属网络通道。
# 【消息处理】网络通道创建成功，可以实现消息处理机制。
# 【ECHO】Python开发实战
# 【__exit__】上下文销毁，异常类型：<class '__main__.NotSupportException'>、异常内容：网络通道建立失败，无法进行消息处理。、异常跟踪：<traceback object at 0x000002794C03FC40>
# 【网络连接】关闭网络通道。
# 【完结】网络消息处理完成。

###################################

# 如果改为flase，那么就会抛出异常，然后结束程序

class NotSupportException(Exception): # 自定义异常类型
    def __init__(self, **kwargs):
        self.__msg = kwargs.get('msg')
    def __str__(self):
        return self.__msg
class Message: # 消息处理类
    class Connect: # 连接管理类
        def build(self): # 建立网络连接
            print('【网络连接】建立专属网络通道。')
            return True
        def close(self):
            print('【网络连接】关闭网络通道。')
    def echo(self, msg): # 消息处理
        return '【ECHO】' + msg # 消息处理
    def __enter__(self): # 进入上下文操作
        self.__connect = Message.Connect() # 创建连接对象
        if self.__connect.build(): # 连接建立成功
            print('【消息处理】网络通道创建成功，可以实现消息处理机制。')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): # 上下文关闭
        print('【__exit__】上下文销毁，异常类型：%s、异常内容：%s、异常跟踪：%s' % (exc_type, exc_val, exc_tb))
        self.__connect.close() # 关闭网络连接
        # 返回True表示当前的程序已经全部正确的处理完毕（异常都已经处理了）
        # 返回False表示当前的程序没有处理异常，交给调用处来进行异常处理
        return False
def main(): # 主函数
    with Message() as message: # 自动开启了上下文
        print(message.echo('Python开发实战'))
        raise NotSupportException(msg='网络通道建立失败，无法进行消息处理。')
        # 下面这个无法被执行到
        print(message.echo('Redis开发实战'))
    print('【完结】网络消息处理完成。')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【网络连接】建立专属网络通道。
# 【消息处理】网络通道创建成功，可以实现消息处理机制。
# 【ECHO】Python开发实战
# 【__exit__】上下文销毁，异常类型：<class '__main__.NotSupportException'>、异常内容：网络通道建立失败，无法进行消息处理。、异常跟踪：<traceback object at 0x000001966352FC80>
# 【网络连接】关闭网络通道。
# Traceback (most recent call last):
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 35, in <module>
#     main() # 调用主函数
#     ^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 30, in main
#     raise NotSupportException(msg='网络通道建立失败，无法进行消息处理。')
# NotSupportException: 网络通道建立失败，无法进行消息处理。
# PS E:\summer_study\python开发\programe\pythonProject>


############################

class NotSupportException(Exception): # 自定义异常类型
    def __init__(self, **kwargs):
        self.__msg = kwargs.get('msg')
    def __str__(self):
        return self.__msg
class Message: # 消息处理类
    class Connect: # 连接管理类
        def build(self): # 建立网络连接
            print('【网络连接】建立专属网络通道。')
            return True
        def close(self):
            print('【网络连接】关闭网络通道。')
    def echo(self, msg): # 消息处理
        return '【ECHO】' + msg # 消息处理
    def __enter__(self): # 进入上下文操作
        self.__connect = Message.Connect() # 创建连接对象
        if not self.__connect.build(): # 连接没有建立成功
            raise NotSupportException(msg='网络通道建立失败，无法进行消息处理。')
        if self.__connect.build():
            print('【消息处理】网络通道创建成功，可以实现消息处理机制。')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): # 上下文关闭
        print('【__exit__】上下文销毁，异常类型：%s、异常内容：%s、异常跟踪：%s' % (exc_type, exc_val, exc_tb))
        self.__connect.close() # 关闭网络连接
        # 返回True表示当前的程序已经全部正确的处理完毕（异常都已经处理了）
        # 返回False表示当前的程序没有处理异常，交给调用处来进行异常处理
        return True
def main(): # 主函数
    with Message() as message: # 自动开启了上下文
        print(message.echo('Python开发实战'))
        print(message.echo('Redis开发实战'))
    print('【完结】网络消息处理完成。')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【网络连接】建立专属网络通道。
# 【ECHO】Python开发实战
# 【ECHO】Redis开发实战
# 【__exit__】上下文销毁，异常类型：None、异常内容：None、异常跟踪：None
# 【网络连接】关闭网络通道。
# 【完结】网络消息处理完成。

class NotSupportException(Exception): # 自定义异常类型
    def __init__(self, **kwargs):
        self.__msg = kwargs.get('msg')
    def __str__(self):
        return self.__msg
class Message: # 消息处理类
    class Connect: # 连接管理类
        def build(self): # 建立网络连接
            print('【网络连接】建立专属网络通道。')
            return False
        def close(self):
            print('【网络连接】关闭网络通道。')
    def echo(self, msg): # 消息处理
        return '【ECHO】' + msg # 消息处理
    def __enter__(self): # 进入上下文操作
        self.__connect = Message.Connect() # 创建连接对象
        if not self.__connect.build(): # 连接没有建立成功
            raise NotSupportException(msg='网络通道建立失败，无法进行消息处理。')
        if self.__connect.build():
            print('【消息处理】网络通道创建成功，可以实现消息处理机制。')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): # 上下文关闭
        print('【__exit__】上下文销毁，异常类型：%s、异常内容：%s、异常跟踪：%s' % (exc_type, exc_val, exc_tb))
        self.__connect.close() # 关闭网络连接
        # 返回True表示当前的程序已经全部正确的处理完毕（异常都已经处理了）
        # 返回False表示当前的程序没有处理异常，交给调用处来进行异常处理
        return True
def main(): # 主函数
    with Message() as message: # 自动开启了上下文
        print(message.echo('Python开发实战'))
        print(message.echo('Redis开发实战'))
    print('【完结】网络消息处理完成。')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【网络连接】建立专属网络通道。
# Traceback (most recent call last):
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 34, in <module>
#     main() # 调用主函数
#     ^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 29, in main
#     with Message() as message: # 自动开启了上下文
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 18, in __enter__
#     raise NotSupportException(msg='网络通道建立失败，无法进行消息处理。')
# NotSupportException: 网络通道建立失败，无法进行消息处理。
# PS E:\summer_study\python开发\programe\pythonProject>