# 数据转化支持

# class Book: # 定义图书类
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name')
#         # 在正常的项目开发之中，是不可能通过布尔值进行金钱数据的存储的，因为有浮点型的精度的BUG
#         self.__price = kwargs.get('price') # 单位：分
#     def __bool__(self): # 对象布尔转换
#         return self.__name != None # 属性存在时返回True
#     def __int__(self): # 整型对象转换
#         return self.__price # 返回数字
#     def __float__(self): # 浮点型对象转换
#         return self.__price / 100.0 # 单位：元
#     def __round__(self, n=None): # 四舍五入
#         # 当前类的实例化对象里面，实际上会包含有“__float__()”特殊方法的支持，因此与float()函数关联
#         return round(float(self), n) # 此处写self意味着将当前类的对象处理
# def main(): # 主函数
#     book = Book(name = 'Java程序设计开发实战', price=7980) # 创建图书对象
#     print('【对象转布尔型】%s' % bool(book))
#     print('【对象转整型】%s' % int(book))
#     print('【对象转浮点型】%s' % float(book))
#     print('【四舍五入】%s' % round(book, 1))

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
##################################
# 索引分片

class BookIndex: # 图书索引类
    def __init__(self, **kwargs): # 特殊方法
        self.__keyword = kwargs.get('keyword') # 传入一个关键词
    def __index__(self): # 索引分片支持
        return len(self.__keyword) # 截取长度
def main(): # 主函数
    book_index = BookIndex(keyword='Python') # 设置图书索引对象
    print('【数据分片】%s' % 'Python开发实战'[book_index : ]) # 将对象作为索引的处理

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


