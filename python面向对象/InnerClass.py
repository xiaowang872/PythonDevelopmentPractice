# # 内部类

# class Book: # 类使用class关键字定义
#     __press = None
#     __slots__ = ('__author', '__name') # 定义属性插槽
#     def __init__(self, **kwargs):
#         self.__author = kwargs.get('author') # 图书作者
#         self.__name = kwargs.get('name') # 图书名称
#     def publish(self): # 图书出版
#         Book.__press = Book.Press(name='人民邮电出版社') # 图书出版社
#     def get(self):
#         return f'【图书】书名：《{self.__name}》、作者：{self.__author}、出版社：{Book.__press.get_name()}'
#     class Press: # 【内部类】出版社
#         __slots__ = ('__name') # 出版社的名字，使用了封装
#         def __init__(self, **kwargs): # 构造方法初始化
#             self.__name = kwargs.get('name') # 出版社名字
#         def get_name(self):
#             return self.__name
# def main(): # 定义一个主函数
#     book = Book(name='Python开发实战', author='李兴华')
#     book.publish() # 创建出版社的信息
#     print(book.get()) # 获取图书的详情
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

###################################################

# class Book: # 类使用class关键字定义
#     __press = None
#     __slots__ = ('__author', '__name') # 定义属性插槽
#     def __init__(self, **kwargs):
#         self.__author = kwargs.get('author') # 图书作者
#         self.__name = kwargs.get('name') # 图书名称
#     def publish(self): # 图书出版
#         Book.__press = Book.Press(name='人民邮电出版社') # 图书出版社
#         if Book.__press.check(self.__author): # 进行排版
#             if Book.__press.distributor(): # 分销商准备完毕
#                 print('【出版】《%s》图书出版成功。' % self.__name)
#     def get(self):
#         return f'【图书】书名：《{self.__name}》、作者：{self.__author}、出版社：{Book.__press.get_name()}'
#     class Press: # 【内部类】出版社
#         __slots__ = ('__name') # 出版社的名字，使用了封装
#         def __init__(self, **kwargs): # 构造方法初始化
#             self.__name = kwargs.get('name') # 出版社名字
#         # 既然要进行图书的出版操作，实际上出版社也需要做很多的事情，包括校稿、排版
#         def check(self, author): # 排版校稿
#             print('【%s】出版社收到了“%s”老师的图书，准备进行图书校稿。' % (self.__name, author))
#             return True
#         def distributor(self): # 图书分销设计
#             print('【%s】分销商备货完毕，启动各销售渠道。' % self.__name)
#             return True
#         def get_name(self):
#             return self.__name
# def main(): # 定义一个主函数
#     book = Book(name='Python开发实战', author='李兴华')
#     book.publish() # 创建出版社的信息
#     print(book.get()) # 获取图书的详情
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

#######################################################


class Book: # 类使用class关键字定义
    __press = None
    __slots__ = ('__author', '__name') # 定义属性插槽
    def __init__(self, **kwargs):
        self.__author = kwargs.get('author') # 图书作者
        self.__name = kwargs.get('name') # 图书名称
    def publish(self): # 图书出版
        Book.__press = Book.Press(name='人民邮电出版社') # 图书出版社
        if Book.__press.check(self.__author): # 进行排版
            if Book.__press.distributor(): # 分销商准备完毕
                print('【出版】《%s》图书出版成功。' % self.__name)
    def get(self):
        return f'【图书】书名：《{self.__name}》、作者：{self.__author}、出版社：{Book.__press.get_name()}'
    class Press: # 【内部类】出版社
        __slots__ = ('__name') # 出版社的名字，使用了封装
        def __init__(self, **kwargs): # 构造方法初始化
            self.__name = kwargs.get('name') # 出版社名字
        # 既然要进行图书的出版操作，实际上出版社也需要做很多的事情，包括校稿、排版
        def check(self, author): # 排版校稿
            print('【%s】出版社收到了“%s”老师的图书，准备进行图书校稿。' % (self.__name, author))
            return True
        def distributor(self): # 图书分销设计
            print('【%s】分销商备货完毕，启动各销售渠道。' % self.__name)
            return True
        def get_name(self):
            return self.__name
def main(): # 定义一个主函数
    press = Book.Press(name='YOOTK教学研发部') # 实例化内部类对象
    press.distributor() #调用了内部类的方法
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数