# 对象多态性
# class Book: # 定义图书父类
#     def get(self): # 父类的设计一定要满足自己的要求
#         return '【图书】YOOTK李兴华原创编程图书'
# class ProgramBook(Book): # 类继承
#     def get(self): # 方法覆写
#         return '【编程图书】李兴华，《Python开发实战》'
# class Press: # 出版社
#     def publish(self, book): # 图书出版
#         print(book.get()) # 获取图书信息，模拟图书出版
# def main(): # 主函数
#     press = Press() # 实例化出版社
#     press.publish(Book()) # 传递的父类对象
#     press.publish(ProgramBook()) # 传递的父类对象

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
# # class ProgramBook(): 如果上面的改成这样，代码也能运行，这是一个缺点

###########################################################
# 这个是向上转型
# class Book: # 定义图书父类
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name')
#         self.__author = kwargs.get('author')
#     def get(self): # 父类的设计一定要满足自己的要求
#         return f'【图书】YOOTK李兴华原创编程图书，图书名称：《{self.__name}》、作者：{self.__author}'
# class ProgramBook(Book): # 类继承
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.__type = kwargs.get('type')
#     def get(self): # 方法覆写
#         return super().get() + f'、编程类型：{self.__type}'
# class Press: # 出版社
#     def publish(self, book): # 图书出版
#         print(book.get()) # 获取图书信息，模拟图书出版
# def main(): # 主函数
#     press = Press() # 实例化出版社
#     press.publish(Book(name='Java程序设计开发实战', author='李兴华')) # 传递的父类对象
#     press.publish(ProgramBook(name='Python开发实战', author='小李', type='python')) # 传递的父类对象

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

#######################################################
# 这个是向下转型
# class Book:
#     def get(self):
#         return '【图书信息】YOOTK李兴华原创编程图书'
# class ProgramBook(Book): # 类继承
#     def prepare(self):
#         return '【编程准备】英文打字、电脑基础知识、计算机硬件。'
#     def get(self): # 方法覆写
#         return '【编程图书】李兴华、《Python开发实战》'
# def read(book): # 阅读图书的函数
#     print(book.get()) # 获取图书信息
#     if isinstance(book, ProgramBook): # 判断实例类型
#         print(book.prepare()) # 子类的特殊功能
# def main(): # 主函数
#     read(Book()) # 传递的父类对象
#     print('-' * 80)
#     read(ProgramBook()) # 传递的父类对象

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
########################
# 这个是向上转型更好一些

class Book:
    def get(self):
        return '【图书信息】YOOTK李兴华原创编程图书'
class ProgramBook(Book): # 类继承
    def prepare(self):
        return '【编程准备】英文打字、电脑基础知识、计算机硬件。'
    def get(self): # 方法覆写
        print(self.prepare()) # 调用本类方法
        return '【编程图书】李兴华、《Python开发实战》'
def read(book): # 阅读图书的函数
    print(book.get()) # 获取图书信息
def main(): # 主函数
    read(Book()) # 传递的父类对象
    print('-' * 80)
    read(ProgramBook()) # 传递的父类对象

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数