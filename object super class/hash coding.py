# 哈希编码

class Book: # 定义图书类
    def __init__(self, **kwargs): # 构造方法
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')

    def __hash__(self): # 获取哈希码
        result = self.__name + ',' + self.__author # 拼凑的内容
        # 此时的哈希计算是由Python内部的操作完成的
        return object.__hash__(result) # 哈希计算
def main(): # 主函数
    # 创建两个不同的对象，随后观察两个对象的内容都是相同的
    book_a = Book(author='李兴华', name='Python开发实战')
    book_b = Book(author='李兴华', name='Python开发实战')
    print('【哈希编码】book_a = %s、book_b = %s' % (hash(book_a), hash(book_b)))

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数