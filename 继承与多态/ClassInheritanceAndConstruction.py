# # 类的继承和构造方法
# class Book: # 类使用class关键字定义
#     def set_name(self, name): # 图书名字
#         self.__name = name # 属性保存
#     def get_name(self):
#         return self.__name
# class ProgramBook(Book): # 编程图书类
#     # 此时的编程类的图书是图书的子类，因此可以直接继承图书类的全部定义
#     pass
# def main(): # 定义一个主函数
#     program = ProgramBook() # 定义编程类的图书
#     # 此时所调用的方法是由Book父类来定义的
#     program.set_name('Python开发实战') # 属性设置
#     print('【图书】%s' % program.get_name())
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
#####################################################################
# class Book: # 类使用class关键字定义
#     def set_name(self, name): # 图书名字
#         self.__name = name # 属性保存
#     def set_author(self, author):
#         self.__author = author
#     def get_name(self):
#         return self.__name
#     def get_author(self):
#         return self.__author
# class ProgramBook(Book): # 编程图书类
#     # 此时的编程类的图书是图书的子类，因此可以直接继承图书类的全部定义
#     # 此时该子类中拥有三个属性的定义以及六个方法（setter、getter）
#     def set_type(self, type): # 子类扩充的方法
#         self.__type = type
#     def get_type(self): # 子类扩充方法
#         return self.__type
# class MathBook(Book): # 图书子类
#     def set_domain(self, domain): # 子类扩充方法
#         self.__domain = domain
#     def get_domain(self):
#         return self.__domain
# def main(): # 定义一个主函数
#     program = ProgramBook() # 定义编程类的图书
#     # 此时所调用的方法是由Book父类来定义的
#     program.set_name('Python开发实战') # 属性设置
#     program.set_author('李兴华') # 属性设置
#     program.set_type('python') # 属性设置
#     print('【编程图书】名称：《%s》、分类：%s、作者：%s' %
#           (program.get_name(), program.get_type(), program.get_author()))
#     print('-' * 100)
#     math = MathBook() # 实例化子类对象
#     math.set_name('微积分') # 父类
#     math.set_author('艾萨克·牛顿、莱布尼茨')
#     math.set_domain('高级数学')
#     print('【数学图书】名称：《%s》、领域：%s、作者：%s' %
#           (math.get_name(), math.get_domain(), math.get_author()))
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

####################################################################
#多继承

# class Book: # 定义图书
#     pass
# class System: # 操作系统
#     pass
# class Computer: # 计算机硬件
#     pass
# class ProgramBook(Book, System, Computer):
#     pass # 此时提供的是一个多继承的环境
# def main(): # 主函数
#     program = ProgramBook() # 具有三个父类和自己本类的功能
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# # 但后面可能有MRO或其他的内容
###################################################################


# 构造方法处理
# class Book: # 定义图书
#     def __init__(self):
#         print('【图书父类】创建Book类的实例化对象')
# class ProgramBook(Book):
#     def __init__(self):
#         print('【编程图书】实例化ProgramBook类对象')
# class MathBook(Book): # 没有定义任何的结构
#     pass
# def main(): # 主函数
#     program = ProgramBook() # 实例化子类对象
#     print('-' * 100)
#     math = MathBook() # 实例化子类对象
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
# 子类没有定义构造方法时，Python会自动调用父类的构造方法
# 如果子类定义了构造方法，则不会调用父类的构造方法

# # PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/ 继承与多态/Class inheritanceAndConstruction.py"
# 【编程图书】实例化ProgramBook类对象
# ----------------------------------------------------------------------------------------------------
# 【图书父类】创建Book类的实例化对象
#####################################################################
# 用__super().__init__()强行调用父类的构造方法
# class Book: # 定义图书
#     def __init__(self):
#         print('【图书父类】创建Book类的实例化对象')
# class ProgramBook(Book):
#     def __init__(self):
#         super().__init__() # 强行调用父类的构造方法
#         print('【编程图书】实例化ProgramBook类对象')
#     def set_name(self):
#         # super().__init__() # 也可以在这里调用父类的构造方法
#         pass
# def main(): # 主函数
#     program = ProgramBook() # 实例化子类对象

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

############################################################
# 构造方法实际应用

class Book: # 定义图书
    def __init__(self, **kwargs):
        print('【Book类构造】对象地址：%s、实例化参数：%s' % (id(self), kwargs))
        self.__author = kwargs.get('author')
        self.__name = kwargs.get('name')
    # 为了简化，暂时不编写setter方法了
    def get_author(self):
        return self.__author
    def get_name(self):
        return self.__name
class ProgramBook(Book):
    def __init__(self, **kwargs):
        print('【ProgramBook类构造】对象地址：%s、实例化参数：%s' % (id(self), kwargs))
        # 通过super().__init__()调用父类的构造方法
        super().__init__(**kwargs) # 帮助我们实例化父类对象
        self.__type = kwargs.get('type') # 图书类型
    def set_type(self, type): # 子类扩充的方法
        self.__type = type
    def get_type(self):
        return self.__type
def main(): # 主函数
    program = ProgramBook(name='Python开发实战', author='李兴华', type='python') # 实例化子类对象
    print('【编程图书】名称：《%s》、分类：%s、作者：%s' %
          (program.get_name(), program.get_type(), program.get_author()))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
