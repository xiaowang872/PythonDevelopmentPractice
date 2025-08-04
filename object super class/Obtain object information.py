# 获取对象信息
# class Book: # 定义图书类
#     def __init__(self, **kwargs): # 构造方法
#         self.__name = kwargs.get('name')
#         self.__author = kwargs.get('author')
# def main(): # 主函数
#     # 创建两个不同的对象，随后观察两个对象的内容都是相同的
#     book = Book(author='李兴华', name='Python开发实战')
#     print(book)
#     print(book.__str__())
#     print(str(book))


# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/object super class/Obtain object information.py"
# <__main__.Book object at 0x0000013EB6D6DB10>
# <__main__.Book object at 0x0000021C0129DB10>
# <__main__.Book object at 0x0000021C0129DB10>
# 打印的是当前对象对应的内存地址的信息编码
######################################################################

# 自定义对象获取
class Book: # 定义图书类
    def __init__(self, **kwargs): # 构造方法
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
    def __str__(self): # 方法覆写
        return f'【图书】名称：{self.__name}、作者：{self.__author}'
def main(): # 主函数
    book = Book(author='李兴华', name='Python开发实战')
    print(book)
    print(book.__str__())
    print(str(book))

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
# 此时实例化的book对象，在进行对象转字符串操作的时候，所\
# 调用的就是book类中已经覆写过得__str__()方法


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/object super class/Obtain object information.py"
# 【图书】名称：Python开发实战、作者：李兴华
# 【图书】名称：Python开发实战、作者：李兴华
# 【图书】名称：Python开发实战、作者：李兴华
######################################################################
# __str__()和__repr__()方法覆写

class Book: # 定义图书类
    def __init__(self, **kwargs): # 构造方法
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
    def __repr__(self): # 方法覆写
        return f'【图书 - __repr__()】名称：{self.__name}、作者：{self.__author}'
    def __str__(self): # 方法覆写
        return f'【图书 - __str__()】名称：{self.__name}、作者：{self.__author}'
def main(): # 主函数
    book = Book(author='李兴华', name='Python开发实战')
    print(book) # 默认调用__str__()方法
    print(str(book)) # 调用__str__()方法
    print(repr(book)) # 调用__repr__()方法

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# /python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/object super class/Obtain object information.py"
# 【图书】名称：Python开发实战、作者：李兴华
# 【图书】名称：Python开发实战、作者：李兴华
# 【图书】名称：Python开发实战、作者：李兴华
# 【图书 - __str__()】名称：Python开发实战、作者：李兴华    
# 【图书 - __str__()】名称：Python开发实战、作者：李兴华    
# 【图书 - __repr__()】名称：Python开发实战、作者：李兴华   

###############################################


# __str__()方法和__repr__()方法的区别
# __str__()正常场景下使用的会更多
# __repr__()方法在可交互上更多
# 更多情况下的代码：
#     def __repr__(self): # 方法覆写
    #     return self.__str__()
    # def __str__(self): # 方法覆写
    #     return f'【图书 - __str__()】名称：{self.__name}、作者：{self.__author}'
