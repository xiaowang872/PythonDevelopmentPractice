# raise异常抛出

def main(): # 主函数
    raise ValueError('数据处理错误，无法完成转换操作。')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/异常捕获处理/raise异常抛出.py
# Traceback (most recent call last):
#   File "e:\summer_study\python开发\programe\pythonProject\异常捕获处理\raise异常抛出.py", line 6, in <module>
#     main() # 调用主函数
#     ^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\异常捕获处理\raise异常抛出.py", line 4, in main
#     raise ValueError('数据处理错误，无法完成转换操作。')      
# ValueError: 数据处理错误，无法完成转换操作。

class Connect: # 定义连接类
    def build(self): # 创建连接
        raise NotImplementedError('build()方法未实现，无法使用！')
class NetConnect(Connect): # 定义连接处理子类
    def build(self):
        print('【建立连接】建立互联网通讯通道。')
def main(): # 主函数
    conn = NetConnect() #
    conn.build()
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/异常捕获处理/Exception handling process.py"
# 【建立连接】建立互联网通讯通道。

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【家庭作业】检查当前作业量，数量为：300
# 【家庭作业】收拾书桌，准备明天的学习资料
# 【异常处理】异常类型：<class '__main__.BreakDownException'>、 异常信息：当前作业量为300道系统，超过了我们宝宝承受的压力范围 
# PS E:\summer_study\python开发\programe\pythonProject>

class BreakDownException(Exception): # 自定义崩溃异常
    def __init__(self, **kwargs): # 构造方法
        self.__msg = kwargs.get('msg') # 保存异常信息
    def __str__(self):
        return self.__msg
class Study:
    def homework(self, num): # 作业
        print('【家庭作业】检查当前作业量，数量为：%d' % num)
        try:
            if num > 200: # 业务触发
                raise BreakDownException(
                    msg=f'当前作业量为{num}道系统，超过了我们宝宝承受的压力范围')
        # 没有定义except表示本方法不处理异常，把异常的处理权利交给调用处
        finally: # 产生的异常应该交给调用处处理
            print('【家庭作业】收拾书桌，准备明天的学习资料')
def main(): # 主函数
    try: # 异常捕获
        study = Study()
        study.homework(300)
    except Exception as err: # 异常统一处理
        print('【异常处理】异常类型：%s、异常信息：%s' % (type(err), err))
    print('【程序正常结束】')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【家庭作业】检查当前作业量，数量为：300
# 【家庭作业】收拾书桌，准备明天的学习资料
# 【异常处理】异常类型：<class '__main__.BreakDownException'>、异常信息：当前作业量为300道系统，超过了我们宝宝承受的压力范围
# 【程序正常结束】

