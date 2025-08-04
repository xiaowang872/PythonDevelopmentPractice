# 属性字典

# class Book: # 定义图书类
#     pass
# def main(): # 主函数
#     book = Book() # 创建图书对象
#     book.name = 'Python开发实战'
#     book.author = '李兴华'
#     print(book.__dict__)
#     print(book.__dict__.get('name'))

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
# ythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/object super class/Attribute Dictionary.py"
# {'name': 'Python开发实战', 'author': '李兴华'}
# Python开发实战
#########################################################
# 属性拦截

# class Book: # 定义图书类
#     def set_author(self, author): # 属性设置
#         self.__author = author # 属性保存
#     def set_name(self, name):
#         self.__name = name # 属性保存
#     def get_author(self):
#         return self.__author
#     def get_name(self):
#         return self.__name
#     def __setattr__(self, key, value): # 属性设置拦截
#         print('【属性设置】属性名称：%s、属性内容：%s' % (key, value))
#     def __getattr__(self, item): # 属性获取拦截
#         print('【属性获取】属性名称：%s' % item)
#     def __delattr__(self, item): # 属性删除拦截
#         print('【属性删除】属性名称：%s' % item)
#     def remove_name(self):
#         del self.__name # 删除属性
# def main(): # 主函数
#     book = Book() # 创建图书对象
#     book.set_name('Python开发实战')
#     book.set_author('李兴华')
#     print(book.__dict__) # 观察字典
#     print(book.get_name(), book.get_author())

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/object super class/Attribute Dictionary.py"
# 【属性设置】属性名称：_Book__name、属性内容：Python开发实战
# 【属性设置】属性名称：_Book__author、属性内容：李兴华
# {}
# 【属性获取】属性名称：_Book__name
# 【属性获取】属性名称：_Book__author
# None None

# ##########################################
# 修改拦截操作方法
# class Book: # 定义图书类
#     def set_author(self, author): # 属性设置
#         self.__author = author # 属性保存
#     def set_name(self, name):
#         self.__name = name # 属性保存
#     def get_author(self):
#         return self.__author
#     def get_name(self):
#         return self.__name
#     def __setattr__(self, key, value): # 属性设置拦截
#         print('【属性设置】属性名称：%s、属性内容：%s' % (key, value))
#         # 所有的属性需要保存在属性字典之中，因为此时有了拦截
#         self.__dict__[key] = value # 手工处理
#     def __getattr__(self, item): # 属性获取拦截
#         print('【属性获取】属性名称：%s' % item)
#         if self.__dict__.get(item) == None: # 属性不存在
#             return 'YOOTK' # 返回默认值
# # __getattr__ 只有在 访问不存在的属性 时才会被调用。
#     def __delattr__(self, item): # 属性删除拦截
#         print('【属性删除】属性名称：%s' % item)
#         del self.__dict__[item] # 删除字典
#     def remove_name(self):
#         print("###")
#         del self.__name # 删除属性
# def main(): # 主函数
#     book = Book() # 创建图书对象
#     book.set_name('Python开发实战')
#     book.set_author('李兴华')
#     book.remove_name()
#     print(book.__dict__) # 观察字典
#     print(book.get_name(), book.get_author())

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# e:/summer_study/python开发/programe/pythonProject/object super class/Attribute Dictionary.py"
# 【属性设置】属性名称：_Book__name、属性内容：Python开发实战
# 【属性设置】属性名称：_Book__author、属性内容：李兴华
# ###
# 【属性删除】属性名称：_Book__name
# {'_Book__author': '李兴华'}
# 【属性获取】属性名称：_Book__name
# YOOTK 李兴华



# 缺点是开发者手工“__dict__”操作，容易出错，且不方便。
########################################

# 新的“__getattribute__()”可以对任何调度进行拦截

class Book: # 定义图书类
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
    def get_name(self):
        return self.__name
    def __getattribute__(self, item): # 属性获取拦截
        print('【结构调用】结构名称：%s' % item) # 获取属性时也调用该方法
        return object.__getattribute__(self, item) # 获取属性
def main(): # 主函数
    book = Book(name = 'Python开发实战') # 创建图书对象
    print('【图书】名称：%s' % book.get_name())

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
# ！！！如果是封装属性，那么保存在字典里的key为“_类名称__属性名称”而普通属性都是直接保存在字典里面的（属性名称为字典的key）
# 这两个区别一定要记住，同时，每当获取对象属性时时，都会调用“__getattribute__()”方法

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/object super class/Attribute Dictionary.py"
# 【结构调用】结构名称：get_name
# 【结构调用】结构名称：_Book__name
# 【图书】名称：Python开发实战
