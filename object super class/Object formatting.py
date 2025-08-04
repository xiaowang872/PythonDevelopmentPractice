# 对象格式化

# class Book: # 定义图书类
#     __slots__ = ('__name', '__author') # 定义属性范围元组
#     def __init__(self, **kwargs): # 构造方法
#         self.__name = kwargs.get('name')
#         self.__author = kwargs.get('author')
#     def __format__(self, format_spec): # 对象格式化
#         print('【格式化字符串】%s' % format_spec) # 观察使用
#         if format_spec == '' or format_spec == None: # 没有格式化标记
#             print("-"*30)
#             print(str(self))
#             print("-"*30)
#             return str(self) # self为当前对象，调用__str__()方法的返回结果
#         format_data = format_spec.replace('%name', self.__name) \
#             .replace('%author', self.__author) # 属性替换
#         return format_data # 该方法必须返回字符串
#     def __str__(self): # 方法覆写
#         return f'【图书】名称：{self.__name}、作者：{self.__author}'
# def main(): # 主函数
#     book = Book(author='李兴华', name='Python开发实战')
#     # 希望将book类对象中的属性取出，而后填充到指定的格式化字符串之中
#     # 这个时候由于传入的是一个book类的对象，因此会调用Book类中的__format__()方法
#     print('【格式化】{}'.format(book)) # 字符串定义的格式化操作
#     print("##########")
#     print(f'【格式化】书名：{book:%name}、作者：{book:%author}')
#     print('【格式化】%s' % format(book, '书名：%name、作者：%author'))

# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/object super class/Object formatting.py" 
# 【格式化字符串】
# ------------------------------
# 【图书】名称：Python开发实战、作者：李兴华
# ------------------------------
# 【格式化】【图书】名称：Python开发实战、作者：李兴华
# ##########
# 【格式化字符串】%name
# 【格式化字符串】%author
# 【格式化】书名：Python开发实战、作者：李兴华
# 【格式化字符串】书名：%name、作者：%author
# 【格式化】书名：Python开发实战、作者：李兴华


# 因为 f-string 中的 每个格式化表达式都是独立计算的，所以：

# {book:%name} 和 {book:%author} 是两个独立的格式化请求。

# 每次都会触发 __format__ 方法，导致调试信息打印两次。
# ####################################################################

# 图书馆实例

class Book: # 定义图书类
    __slots__ = ('__name', '__author') # 定义属性范围元组
    def __init__(self, **kwargs): # 构造方法
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
    def __format__(self, format_spec): # 对象格式化
        print('【格式化字符串】%s' % format_spec)
        if format_spec == '' or format_spec == None: # 没有格式化标记
            # format(book)  # 等效于 format(book, "")print("{}".format(book)) 
            # format_spec = ""
            # print(f"{book}")  # format_spec = ""
            return str(self) # self为当前对象，调用__str__()方法的返回结果
        format_data = format_spec.replace('%name', self.__name) \
            .replace('%author', self.__author) # 属性替换
        return format_data # 该方法必须返回字符串
    def __str__(self): # 方法覆写
        return f'【图书】名称：{self.__name}、作者：{self.__author}'
class Library: # 定义图书馆类型
    __slots__ = ('__books', '__name') # 一个表示图书集合，另外一个表示图书馆名字
    def __init__(self, name): # 构造方法
        self.__name = name # 保存图书馆名字
        # 每一个字典之中，可以存放不同种类的图书，key为分类的信息，value为一个列表（list）
        self.__books = {} # 创建空字典
    # 在参数定义上可以使用“参数名称:类型”的形式进行定义，这样可以明确参数的传递形式
    def add_book(self, item, book:Book): # item表示图书分类
        if item == '' or item == None: # 分类不允许为空
            return  # 结束方法调用
        book_list = self.__books.get(item) # 获取分类列表
        if book_list == None: # 分类不存在
            book_list = [] # 创建一个新的列表
        book_list.append(book) # 添加图书
        self.__books.update({item.strip().lower(): book_list}) # 更新字典
    def __str__(self): # 获取图书馆信息
        return f'【图书馆】名称：{self.__name}、藏书类型：{self.__books.keys().__str__()}'
    def __format__(self, format_spec): # 数据格式化处理
        if format_spec == '' or format_spec == None: # 未设置字符串格式化
            return str(self) # 返回对象信息
        format_data = format_spec.replace('%name', self.__name) + '\n' # 格式化数据
        count = 1 # 访问计数
        for key, value in self.__books.items(): # 字典迭代
            format_data += '【图书分类  - ' + str(count) + '】' + key + '\n'
            count += 1 # 序号自增
            for book in value: # 列表迭代
                format_data += '\t' + f'〖图书〗书名：{book:%name}、作者：{book:%author}\n'
        return format_data
def main(): # 主函数
    library = Library('YOOTK编程图书馆')
    library.add_book('java', Book(name='Java程序设计开发实战', author='李兴华'))
    library.add_book('java', Book(name='Java进阶开发实战', author='李兴华'))
    library.add_book('python', Book(name='Python开发实战', author='李兴华'))
    library.add_book('database', Book(name='MySQL开发实战', author='李兴华'))
    library.add_book('database', Book(name='Redis开发实战', author='李兴华'))
    print('{lib:%name}'.format(lib=library))

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
