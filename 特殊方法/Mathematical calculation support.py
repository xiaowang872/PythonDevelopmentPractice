# 数学计算支持
# class Book: # 创建图书类
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name')
#         self.__price = kwargs.get('price')
#     def __add__(self, other): # 加法运算支持
#         return self.__price + other.__price # 外部传递的另外一个数学计算的值
#     def __sub__(self, other): # 减法运算支持
#         return self.__price - other.__price
# def main(): # 主函数
#     book_a = Book(name='Java程序设计开发实战', price=7980) # 实例化Book类对象
#     book_b = Book(name='Python开发实战', price=8980) # 实例化Book类对象
#     print('【加法计算】book_a + book_b = %d' % (book_a + book_b)) # 数学计算
#     print('【减法计算】book_a - book_b = %d' % (book_a - book_b)) # 数学计算

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# ythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/特殊方法/Mathematical calculation support.py"
# 【加法计算】book_a + book_b = 16960
# 【减法计算】book_a - book_b = -1000
# PS E:\summer_study\python开发\programe\pythonProject>

###################################
class Book: # 创建图书类
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__price = kwargs.get('price')
    def __add__(self, other): # 加法运算支持
        return self.__price + other.__price # 外部传递的另外一个数学计算的值
    def __sub__(self, other): # 减法运算支持
        return self.__price - other.__price
def main(): # 主函数
    book_a = Book(name='Java程序设计开发实战', price=7980) # 实例化Book类对象
    book_b = Book(name='Python开发实战', price=8980) # 实例化Book类对象
    print('【加法计算】book_a + book_b = %d' % (book_a + book_b)) # 数学计算
    print('【减法计算】book_a - book_b = %d' % (book_a - book_b)) # 数学计算
    print('【乘法计算】book_a * book_b = %d' % (book_a * book_b)) # 数学计算

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/特殊方法/Mathematical calculation support.py"

# 【加法计算】book_a + book_b = 16960
# 【减法计算】book_a - book_b = -1000
# Traceback (most recent call last):
#   File "e:\summer_study\python开发\programe\pythonProject\特殊方法\Mathematical calculation support.py", line 38, in main
#     print('【乘法计算】book_a * book_b = %d' % (book_a * book_b)) # 数学计算
#                                           ~~~~~~~^~~~~~~~
# TypeError: unsupported operand type(s) for *: 'Book' and 'Book'

# 因为没有覆写乘法计算
