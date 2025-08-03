# Method overlay
# 方法覆写的前提是要有继承
# class Book: # 定义图书父类
#     def __init__(self, **kwargs):
#         self.__author = kwargs.get('author')
#         self.__name = kwargs.get('name')
#     def get(self): # 父类的设计一定要满足自己的要求
#         return f'【图书】名称：《{self.__name}》、作者：{self.__author}'
# class ProgramBook(Book): # 类继承
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs) # 调用父类构造
#         self.__type = kwargs.get('type')
#     # 方法覆写：将父类的方法定义完整的拿到子类，进行方法体的变更
#     def get(self): # 此时需要继续使用父类中的方法名称
#         # 调用父类方法：super().方法名称()
#         return super().get() + f'、分类：{self.__type}'
# class MathBook(Book): # 类继承
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.__domain = kwargs.get('domain')
#     def get(self): # 子类覆写方法
#         return super().get() + f'、领域：{self.__domain}'
# def main(): # 主函数
#     book = Book(name='Python开发实战', author='李兴华')
#     print(book.get())
#     print('-' * 80)
#     program = ProgramBook(name='MySQL开发实战', author='李兴华', type='database')
#     # 现在是由子类对象实例发出的方法调用，并且get()方法已经被子类所覆写了，所以调用覆写过的方法
#     print(program.get())
#     print('-' * 80)
#     math = MathBook(name='微积分', author='牛顿、莱布尼茨', domain='高级数学')
#     print(math.get())
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

##############################################################
# 方法覆写原则：子类的方法与父类的方法定义完全相同
# 我写个不同的
class Book: # 定义图书父类
    def __init__(self, **kwargs):
        self.__author = kwargs.get('author')
        self.__name = kwargs.get('name')
    def get(self): # 父类的设计一定要满足自己的要求
        return f'【图书】名称：《{self.__name}》、作者：{self.__author}'
class ProgramBook(Book): # 类继承
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # 调用父类构造
        self.__type = kwargs.get('type')
    def get(self, *items): # 此时的方法和父类方法不同
        return super().get() + f'、分类：{self.__type}\n【技术项】{items}'
def main(): # 主函数
    program = ProgramBook(name='MySQL开发实战', author='李兴华', type='database')
    # 现在是由子类对象实例发出的方法调用，并且get()方法已经被子类所覆写了，所以调用覆写过的方法
    print(program.get())
    print('-' * 80)
    print(program.get('基础语法', '办公自动化', '网络爬虫', '数据分析', 'Web开发'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


