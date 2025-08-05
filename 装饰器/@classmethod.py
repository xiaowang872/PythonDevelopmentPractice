class Book: # 自定义图书类
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
    def __str__(self):
        return f'【图书】名称：{self.__name}、作者：{self.__author}'
    @classmethod
    def get_instance(clazz, data): # 会默认传递一个实例类型
        print('【类型】类名称：%s' % (clazz.__name__)) # 获取类名称的信息
        # 需要将实例化一个对象的所有的数据使用“;”进行分割定义
        result = data.split(';') # 字符串拆分
        return clazz(name=result[0], author=result[1]) # 对象实例化
def main(): # 主函数
    # get_instance()方法定义在Book类里面，因此这个时候要通过“Book.get_instance()”的形式调用
    # 这样一来该方法上就可以使用clazz接收其对应的类型（@classmethod）
    book = Book.get_instance('Python开发实战;李兴华')
    print(book)
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# ython.exe e:/summer_study/python开发/programe/pythonProject/装饰器/metaclass.py
# 【类型】类名称：Book
# 【图书】名称：Python开发实战、作者：李兴华


############################################
import inspect # 导入一个操作模块
class Book: # 自定义图书类
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
    def __str__(self):
        return f'【图书】名称：{self.__name}、作者：{self.__author}'
    @classmethod
    def get_instance(clazz, data): # 会默认传递一个实例类型
        print(inspect.stack())
        print('【类型】类名称：%s' % (clazz.__name__)) # 获取类名称的信息
        # 需要将实例化一个对象的所有的数据使用“;”进行分割定义
        result = data.split(';') # 字符串拆分
        return clazz(name=result[0], author=result[1]) # 对象实例化
def main(): # 主函数
    # get_instance()方法定义在Book类里面，因此这个时候要通过“Book.get_instance()”的形式调用
    # 这样一来该方法上就可以使用clazz接收其对应的类型（@classmethod）
    Book.get_instance('Python开发实战;李兴华')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数




# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# [FrameInfo(frame=<frame at 0x000002590D72C860, file 'e:\\summer_study\\python开 发\\programe\\pythonProject\\tmp\\abc.py', line 10, code get_instance>, filename='e:\\summer_study\\python开发\\programe\\pythonProject\\tmp\\abc.py', lineno=10, function='get_instance', code_context=['        print(inspect.stack())\n'], index=0, positions=Positions(lineno=10, end_lineno=10, col_offset=14, end_col_offset=29)), FrameInfo(frame=<frame at 0x000002590DB03600, file 'e:\\summer_study\\python开发\\programe\\pythonProject\\tmp\\abc.py', line 18, code main>, filename='e:\\summer_study\\python开发\\programe\\pythonProject\\tmp\\abc.py', lineno=18, function='main', code_context=["    Book.get_instance('Python开发实战;李兴华')\n"], index=0, positions=Positions(lineno=18, end_lineno=18, col_offset=4, end_col_offset=53)), FrameInfo(frame=<frame at 0x000002590DAB4A90, file 'e:\\summer_study\\python开发\\programe\\pythonProject\\tmp\\abc.py', line 20, code <module>>, filename='e:\\summer_study\\pyttext=['    main() # 调用主函数\n'], index=0, positions=Positions(lineno=20, end_lineno=20, col_offset=4, end_col_offset=10))]
# 【类型】类名称：Book
# PS E:\summer_study\python开发\programe\pythonProject>

# 创建抽象方法
import abc # Python内置模块
class Book(object, metaclass=abc.ABCMeta): # 自定义图书类
    @abc.abstractmethod # 抽象方法定义
    def create(self): # 抽象方法
        pass # 方法体为空
def main(): # 主函数
    book = Book()
    print(book.create())
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# Traceback (most recent call last):
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 10, in <module>
#     main() # 调用主函数
#     ^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 7, in main
#     book = Book()
#            ^^^^^^
# TypeError: Can't instantiate abstract class Book with abstract method create

import abc # Python内置模块
class Book(object, metaclass=abc.ABCMeta): # 自定义图书类
    @abc.abstractmethod # 抽象方法定义
    def create(self): # 抽象方法
        pass # 方法体为空
class ProgramBook(Book): # 图书子类
    def create(self): # 覆写方法
        return '【编程图书】《Python开发实战》图书创作，用朴实的文字和细致的图示完美解释Python编程开发技术。'
def main(): # 主函数
    book = ProgramBook() # 实例化子类对象
    print(book.create())
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【编程图书】《Python开发实战》图书创作，用朴实的文字和细致的图示完美解释Python编程开发技术。
# PS E:\summer_study\python开发\programe\pythonProject> 