# python中所有的类都是从object类派生而来的（继承）
# class Book(object): # 定义图书类
#     def get(self):
#         print('【Book】Python开发实战')
# class ComputerBook(Book): # 定义图书子类
#     def get(self):# 方法覆写
#         print('【ComputerBook】沐言科技，Python开发实战')
# class MathBook(Book):
#     def get(self): # 方法覆写
#         print('【MathBook】Python与数学应用')
# class ProgramBook(ComputerBook, MathBook): # 此时继承两个父类
#     # 当前类中没有定义任何的方法，因此在调用get()的时候应该找到的父类中的方法
#     pass # 不定义方法体
# def main(): # 主函数
#     # 此时三个父类都有get()方法，那么请问最终调用的是那一个呢？
#     ProgramBook().get()
#     print(ProgramBook.__mro__)
# # S E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/object super class/object.py"
# # 【ComputerBook】沐言科技，Python开发实战
# # (<class '__main__.ProgramBook'>, <class '__main__.ComputerBook'>, <class '__main__.MathBook'>, <class '__main__.Book'>, <class 'object'>)
# # PS E:\summer_study\python开发\programe\pythonProject>
# # 广度优先算法，从左到右依次访问
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
#############################################
# class A: pass
# class B: pass
# class X (A, B): pass # MRO广度优先：A、B
# class Y (B, A): pass # MRO广度优先：B、A
# class Z (X, Y): pass # MRO广度优先：X、Y、（“A、B”还是“B、A”？）
# def main(): # 主函数
#     print(Z.__mro__)

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
#   File "e:\summer_study\python开发\programe\pythonProject\object super class\object.py", line 29, in <module>
#     class Z (X, Y): pass # MRO广度优先：X、Y、（“A、B”还是“B、A”？）
#     ^^^^^^^^^^^^^^^^^^^^
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/object super class/object.py"
#   File "e:\summer_study\python开发\programe\pythonProject\object super class\object.py", line 29, in <module>
#     class Z (X, Y): pass # MRO广度优先：X、Y、（“A、B”还是“B、A”？）
#     ^^^^^^^^^^^^^^^^^^^^
#########################################
# 修改
# class A: pass
# class B: pass
# class X (A, B): pass # MRO广度优先：A、B
# class Y (A, B): pass # MRO广度优先：B、A
# class Z (X, Y): pass # MRO广度优先：X、Y、（“A、B”还是“B、A”？）
# def main(): # 主函数
#     print(Z.__mro__)

# if __name__ == '__main__':  # Python程序运行起点
    # main() # 调用主函数
# # PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/object super class/object.py"   
# (<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# PS E:\summer_study\python开发\programe\pythonProject> 

#############################################

class Book: # 定义图书类
    """
        这是一个关于图书结构的描述，该类默认是object子类，可以直接继承已有的object类中的全部结构
        注意，这样话该类可以拥有不少的原始功能支持
        类之中的构造方法本质上就属于覆写object父类之中所提供的方法
    """
    def __init__(self, **kwargs): # 构造方法
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
def main(): # 主函数
    book = Book(author='李兴华', name='Python开发实战')
    print('【对象类型】%s' % book.__class__)
    print('【结构列表】%s' % dir(book))
    print('【属性字典】%s' % book.__dict__)
    print('【对象说明】%s' % book.__doc__)

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/object super class/object.py"
# 【对象类型】<class '__main__.Book'>
# 【结构列表】['_Book__author', '_Book__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__'] 
# 【属性字典】{'_Book__name': 'Python开发实战', '_Book__author': '李兴华'}
# 【对象说明】
#         这是一个关于图书结构的描述，该类默认是object子类，可以直接继承已有的object类中的全部结构
#         注意，这样话该类可以拥有不少的原始功能支持
#         类之中的构造方法本质上就属于覆写object父类之中所提供的方法
