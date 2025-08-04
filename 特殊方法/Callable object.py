# 可调用对象
# class Book: # 创建图书类
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name')
#         self.__author = kwargs.get('author')
#     # 可调用对象采用的是“对象()”的形式来进行处理，因此这时可以传递参数的
#     def __call__(self, *args, **kwargs): # 调用操作
#         return self.__str__() + f'、核心内容：{args}、标记：{kwargs}'
#     def __str__(self): # 返回对象的内容
#         return f'【图书】名称：{self.__name}、作者：{self.__author}'
# def main(): # 主函数
#     book = Book(name='Python开发实战', author='李兴华') # 实例化Book类对象
#     print(book('基础语法', '面向对象', 'Web开发', '科学计算', company='YOOTK')) # 可调用对象
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数



# 在Python中，__call__ 是一个特殊方法（magic method），它允许一个类的实例像函数一样被调用。当你对一个实例使用 () 运算符时，Python 会自动调用该实例的 __call__ 方法。
# 当你写 book('基础语法', '面向对象', company='YOOTK') 时，Python 会调用 book.__call__('基础语法', '面向对象', company='YOOTK')。
# *args：接收任意数量的位置参数（非关键字参数），在调用时会被打包成一个元组。
# **kwargs：接收任意数量的关键字参数，在调用时会被打包成一个字典。
# 
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/ 特殊方法/Callable object.py"
# 【图书】名称：Python开发实战、作者：李兴华、核心内容：('基础语法', '面向对象', 'Web开发', '科学计算')、标记：{'company': 'YOOTK'}
##############################################################################################
# 检查处理函数callable()

# class Book: # 创建图书类
#     def __call__(self, *args, **kwargs):
#         pass
# def main(): # 主函数
#     book = Book() # 实例化Book类对象
#     print('【可调用状态检查】book()函数是否可用：%s' %  callable(book))
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# # 【可调用状态检查】book()函数是否可用：True



# class Book: # 创建图书类
#     # def __call__(self, *args, **kwargs):
#         pass
# def main(): # 主函数
#     book = Book() # 实例化Book类对象
#     print('【可调用状态检查】book()函数是否可用：%s' %  callable(book))
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# 【可调用状态检查】book()函数是否可用：False
# 只要在类中提供了__call__()方法，那么该类对象就可以被调用,callable()方法返回True


#####################################
# ！！！！！！！！！！！不仅是类对象，函数对象也可以被调用


def main(): # 主函数
    add = lambda x, y : x + y # 函数必须存在才可以判断
    print('【可调用状态检查】main()函数是否可用：%s' %  callable(main)) # 只写上函数名称
    print('【可调用状态检查】print()函数是否可用：%s' %  callable(print)) # 只写上函数名称
    print('【可调用状态检查】add()函数是否可用：%s' %  callable(add)) # 只写上函数名称
    print('【可调用状态检查】“hello”字符串可调用状态：%s' %  callable('hello')) # 只写上函数名称
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

