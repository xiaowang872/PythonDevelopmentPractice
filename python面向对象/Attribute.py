# # 类属性，相当于公共属性
# class Book: # 类使用class关键字定义
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name') # 图书名称
#         self.__author = kwargs.get('author') # 图书作者
#         self.__press = kwargs.get('press') # 出版社
#     def get(self):
#         return f'【图书】书名：《{self.__name}》、作者：{self.__author}、出版社：{self.__press}'
# def main(): # 定义一个主函数
#     book_a = Book(name='Python开发实战', author='李兴华', press='人民邮电出版社') # 【构造】对象实例化
#     book_b = Book(name='Java程序设计开发实战', author='李兴华', press='人民邮电出版社')  # 【构造】对象实例化
#     book_c = Book(name='MySQL开发实战', author='李兴华', press='人民邮电出版社')  # 【构造】对象实例化
#     print(book_a.get())
#     print(book_b.get())
#     print(book_c.get())
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

###################################


class Book: # 类使用class关键字定义
    __slots__ = ('__author', '__name')
    # __slots__定义了类的属性，限制了类只能有这两个属性
    # 但对__PRESS属性不进行限制
    # 因为__PRESS是一个公共属性，不属于某一个对象
    __PRESS = 'YOOTK教学研发部' # 原本的公共属性内容
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name') # 图书名称
        self.__author = kwargs.get('author') # 图书作者
    # 公共属性不属于某一个对象，因此不再追加self参数，理解为是一个公共方法
    def set_press(press): # 修改公共属性
        Book.__PRESS = press # 公共属性通过类名称进行访问
    def get(self):
        return f'【图书】书名：《{self.__name}》、作者：{self.__author}、出版社：{self.__PRESS}'
def main(): # 定义一个主函数
    book_a = Book(name='Python开发实战', author='李兴华')
    book_b = Book(name='Java程序设计开发实战', author='李兴华')
    book_c = Book(name='MySQL开发实战', author='李兴华')
    print(book_a.get())
    print(book_b.get())
    print(book_c.get())
    print('--------------------- 修改出版社的信息 ---------------------')
    # set_press()方法不是普通方法，而是一个公共方法，公共方法使用类名称直接进行访问
    Book.set_press('人民邮电出版社') # 修改公共的属性
    print(book_a.get())
    print(book_b.get())
    print(book_c.get())
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

