# class Book: # 类使用class关键字定义
#     # 类的初始化的操作，在Python里面是固定了一个方法名称
#     def __init__(self): # 构造方法
#         print('【Book】构造方法调用，self = %d' % id(self))
# def main(): # 定义一个主函数
#     book = Book() # 实例化Book类对象
#     print('【主函数】book类的实例化对象：%d' % id(book))
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数


# ##########################################################
# # 下面可以发现__init__()比之前的构造函数更为灵活
# class Book: # 类使用class关键字定义
#     def __init__(self, author, name): # 构造方法进行参数配置
#         print('【构造方法】实例化Book类对象，并设置对象属性内容。')
#         self.__author = author # 属性设置
#         self.set_name(name) # 调用setter方法设置（这是可以的）
#     # def set_author(self, author):
#     #     self.__author = author
#     def set_name(self, name):
#         self.__name = name
#     def get_author(self):
#         return self.__author
#     def get_name(self):
#         return self.__name
# def main(): # 定义一个主函数
#     book = Book('李兴华', 'Python开发实战') # 1、实例化Book类对象
#     print('【图书】名称：《%s》、作者：%s' % (book.get_name(), book.get_author()))
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
#############################################################

# **kwargs**的使用可以让类的构造方法更为灵活(动态配置属性无参构造)
class Book: # 类使用class关键字定义
    def __init__(self, **kwargs): # 构造方法进行参数配置
        print('【构造方法】实例化Book类对象，并设置对象属性内容，参数个数：%s' % len(kwargs))
        if len(kwargs) == 0: # 当前是无参调用
            # 由于所有的属性都是动态配置的内容，因此需要首先考虑代码不出错
            self.__name = 'python' # 默认信息
            self.__author = 'yootk' # 默认信息
        else: # 有参调用
            self.__name = kwargs.get('name') # 获取参数
            self.__author = kwargs.get('author') # 获取参数
    def set_author(self, author):
        self.__author = author
    def set_name(self, name):
        self.__name = name
    def get_author(self):
        return self.__author
    def get_name(self):
        return self.__name
    def __del__(self): # 析构方法
        print('【析构方法】Book类对象被销毁，self = %d' % id(self))
def main(): # 定义一个主函数
    book1 = Book() # 1、实例化Book类对象
    print('【图书】名称：《%s》、作者：%s' % (book1.get_name(), book1.get_author()))
    book1.set_name('Java程序设计开发实战') # 修改属性的内容
    print('【图书】名称：《%s》、作者：%s' % (book1.get_name(), book1.get_author()))
    # 这边注意要写name='', author=''，否则会报错
    book2 = Book(name='Python开发实战', author='李兴华')
    print('【图书】名称：《%s》、作者：%s' % (book2.get_name(), book2.get_author()))
    del book2 # 删除book2对象，触发析构方法的调用
    # del book1 # 删除book1对象，触发析构方法的调用
    print('程序结束')







if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


















