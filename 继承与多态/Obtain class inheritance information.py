# 获取类的继承信息

# class Book: # 定义图书类
#     pass
# class Computer: # 定义计算机类
#     pass
# class ProgramBook(Book, Computer): # 第一个父类是最重要的
#     pass
# class MathBook(Book):
#     pass
# def main(): # 主函数
#     book = Book() # 实例化父类对象
#     # “对象.__class__”和“type(对象)”返回的结果的是相同的
#     print('【类名称】获取实例化对象的类信息：%s、type()：%s' % (book.__class__, type(book)))
#     print('【继承父类】获取ProgramBook所继承的第一个父类：%s' % ProgramBook.__base__)
#     print('【继承父类】获取ProgramBook所继承的全部父类：%s' % ProgramBook.__bases__.__str__())
#     # 在面向对象之中子类也被称为派生类，但是现在是通过父类找到派生类
#     print('【派生类】获取Book全部的子类：%s' % Book.__subclasses__())
#     # 此时连基本的继承的关系都可以直接判断，你应该能感受到Python设计的强大了
#     print('【子类判断】判断MathBook类是否为Book子类：%s' % issubclass(MathBook, Book))
#     # 除了使用类可以直接判断之外，也可以通过实例化对象对应的类型进行子类的判断
#     print('【子类判断】判断MathBook类是否为Book子类：%s' % issubclass(MathBook().__class__, Book))
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
##############################################################
# # 在父类中配置__init_subclass__方法,用来实现子类的记录

# class Book: # 定义图书类
#     def __init_subclass__(cls, **kwargs): # 回调函数
#         print('【子类信息】名称：%s' % cls.__name__)
# class ProgramBook(Book): # 第一个父类是最重要的
#     pass
# class MathBook(Book):
#     pass
# def main(): # 主函数
#     pass
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/继承与多态/Obtain class inheritance information.py"
# 【子类信息】名称：ProgramBook
# 【子类信息】名称：MathBook
###############################################################
# 此外还可以获得命名参数

class Book: # 定义图书类
    def __init_subclass__(cls, **kwargs): # 回调函数
        print('【子类信息】名称：%s、参数：%s' % (cls.__name__, kwargs))
class ProgramBook(Book, items=['WEB', 'SQL', 'GUI']): # 第一个父类是最重要的
    pass
class MathBook(Book, support=['数据分析'], author='牛顿'):
    pass
def main(): # 主函数
    pass
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

#####################################################

