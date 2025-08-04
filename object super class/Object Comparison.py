# 对象比较


# class Book: # 定义图书类
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name')
#         self.__author = kwargs.get('author')
#         self.__price = kwargs.get('price')
#     def __le__(self, other): # 小于等于判断
#         return self.__price <= other.__price # 内部找到对象属性
#     def __gt__(self, other): # 大于判断
#         return self.__price > other.__price
#     def __str__(self):
#         return f'【图书】名称：{self.__name}、作者：{self.__author}、价格：{self.__price}'
# def main(): # 主函数
#     book_a = Book(name = 'Java程序设计开发实战', author='李兴华', price=7980) # 创建图书对象
#     book_b = Book(name = 'Java进阶开发实战', author='李兴华', price=8980) # 创建图书对象
#     print('【对象地址】book_a = %d、book_b = %d' % (id(book_a), id(book_b)))
#     # 此时是在自定义的对象结构之中使用了Python内置的关系运算符
#     print('【对象比较】book_a <= book_b = %s' % str(book_a <= book_b))
#     # 所有的关系运算的判断一定要有与之匹配的特殊方法定义
#     print('【对象比较】book_a > book_b = %s' % str(book_a > book_b))

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/object super class/Object Comparison.py"
# 【对象地址】book_a = 3186887944336、book_b = 3186887943120
# 【对象比较】book_a <= book_b = True
# 【对象比较】book_a > book_b = False

##############################################################################
# 对象相等比较（用hash()方法）


class Book: # 定义图书类
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
        self.__price = kwargs.get('price')
    def __eq__(self, other): # 相等判断
        if other == None: # 没有对象
            return False # 对象不相等
        if id(self) == id(other): # 地址相同
            return True # 对象相等
        if hash(self) == hash(other): # 哈希编码相同
            return True
        return self.__name == other.__name and self.__author == other.__author \
                and self.__price == other.__price # 属性依次比较
    def __hash__(self):
        result = self.__name + ',' + self.__author + ',' + str(self.__price)
        return object.__hash__(result)
    def __str__(self):
        return f'【图书】名称：{self.__name}、作者：{self.__author}、价格：{self.__price}'
def main(): # 主函数
    book_a = Book(name = 'Java程序设计开发实战', author='李兴华', price=7980) # 创建图书对象
    book_b = Book(name = 'Java进阶开发实战', author='李兴华', price=8980) # 创建图书对象
    print('【对象比较】book_a == book_a = %s' % str(book_a == book_a))
    print('【对象比较】book_a == book_b = %s' % str(book_a == book_b))

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/object super class/Object Comparison.py"
# 【对象比较】book_a == book_a = True
# 【对象比较】book_a == book_b = False
# PS E:\summer_study\python开发\programe\pythonProject>
# 将已有的运算符和类中的特殊方法整合在一起，这就是python特殊方法存在的意义，用户可以随意地的进行结构的扩充