# 集合迭代支持


# class BookArray: # 自定义一个类
#     def __init__(self):
#         # 本次所有的数据上的处理操作，都是通过Python已经提供的列表的结构来完成
#         self.__books = [] # 创建一个空的列表
#     def add(self, book): # 添加数据
#         self.__books.append(book) # 添加数据
#     def __contains__(self, item): # 检查数据是否存在
#         return self.__books.__contains__(item) # 调用已有的功能
#     def __iter__(self): # 返回迭代对象
#         return self.__books.__iter__()
#     def __len__(self): # 返回数据个数
#         return len(self.__books)
# def main(): # 主函数
#     book_array = BookArray() # 创建图书数组对象
#     book_array.add('Python开发实战') # 添加图书项
#     book_array.add('MySQL开发实战') # 添加图书项
#     book_array.add('Java程序设计开发实战') # 添加图书项
#     print('【BookArray数据结构操作】获取数据保存个数：%s' % len(book_array))
#     print('【BookArray数据结构操作】检查数据是否存在：%s' % ('Python开发实战' in book_array))
#     print('【BookArray数据结构操作】数据迭代操作：')
#     for book in book_array:
#         print('\t【图书】%s' % book)
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# 【BookArray数据结构操作】获取数据保存个数：3
# 【BookArray数据结构操作】检查数据是否存在：True
# 【BookArray数据结构操作】数据迭代操作：
#         【图书】Python开发实战
#         【图书】MySQL开发实战
#         【图书】Java程序设计开发实战
############################################
# class Link: # 链表工具类
#     # 之所以使用内部类的结构，是因为该Node类只服务于Link类
#     class Node: # 链表节点类
#         def __init__(self, **kwargs): # 设置节点初始化
#             # 每一个节点只能够保存一个数据（这个数据可以是任意的内容，或者是其他的序列结构）
#             # 此时的data并没有进行封装处理，因为Node是内部类，这个类为Link服务
#             self.data = kwargs.get('data') # 保存节点数据
#     # ------------------------------- 外部类功能定义 ----------------------------------------
#     def __init__(self): # 外部类构造方法
#         # 第一个保存的数据默认为根节点
#         self.__root = None # 定义根节点
#         self.__last = None # 保存最后一个增加的节点
#         self.__count = 0 # 进行保存数据个数统计
#     def add(self, data): # 数据保存
#         # 保存的数据本身是无法进行先后顺序配置的，因此这个时候要将内容封装在Node节点之中
#         newNode = Link.Node(data = data) # 封装的目的是为了区分先后顺序
#         # 在每一个链表对象之中，都会包含有一个根节点，因此将第一个数据作为根节点
#         if self.__root == None: # 没有根节点，是一个新链表
#             self.__root = newNode # 将新的节点配置为根节点
#             self.__last = newNode # 最新的节点为最后的节点
#         else: # 如果根节点已经存在了
#             # 现在假设每一个节点之中都存在有一个next属性（Python可以动态扩充对象的成员属性）
#             self.__last.next = newNode # 问题来了
#             self.__last = self.__last.next # 修改引用配置
#         self.__count += 1 # 数量自增
#     def __len__(self): # 获取集合的长度
#         return self.__count
# class Book: # 保存对象
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name')
#         self.__author = kwargs.get('author')
# def main(): # 主函数
#     link = Link() # 实例化链表对象
#     link.add(Book(name='Python开发实战', author='李兴华'))
#     link.add(Book(name='Java程序设计开发实战', author='李兴华'))
#     link.add(Book(name='Java进阶开发实战', author='李兴华'))
#     print('【链表】数据保存个数：%d' % len(link))
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/特殊方法/Collection iteration support.py"    
# 【链表】数据保存个数：3
###################################################

# class Link: # 链表工具类
#     # 之所以使用内部类的结构，是因为该Node类只服务于Link类
#     class Node: # 链表节点类
#         def __init__(self, **kwargs): # 设置节点初始化
#             # 每一个节点只能够保存一个数据（这个数据可以是任意的内容，或者是其他的序列结构）
#             # 此时的data并没有进行封装处理，因为Node是内部类，这个类为Link服务
#             self.data = kwargs.get('data') # 保存节点数据
#         def __getattr__(self, item):
#             return None
#     # ------------------------------- 外部类功能定义 ----------------------------------------
#     def __init__(self): # 外部类构造方法
#         # 第一个保存的数据默认为根节点
#         self.__root = None # 定义根节点
#         self.__last = None # 保存最后一个增加的节点
#         self.__count = 0 # 进行保存数据个数统计
#     def add(self, data): # 数据保存
#         # 保存的数据本身是无法进行先后顺序配置的，因此这个时候要将内容封装在Node节点之中
#         newNode = Link.Node(data = data) # 封装的目的是为了区分先后顺序
#         # 在每一个链表对象之中，都会包含有一个根节点，因此将第一个数据作为根节点
#         if self.__root == None: # 没有根节点，是一个新链表
#             self.__root = newNode # 将新的节点配置为根节点
#             self.__last = newNode # 最新的节点为最后的节点
#         else: # 如果根节点已经存在了
#             # 现在假设每一个节点之中都存在有一个next属性（Python可以动态扩充对象的成员属性）
#             self.__last.next = newNode # 问题来了
#             self.__last = self.__last.next # 修改引用配置
#             # 每一个节点的next属性是在某一个数据添加的时候才会配置的属性，如果没有添加则没有该属性
#         self.__count += 1 # 数量自增
#     def __len__(self): # 获取集合的长度
#         return self.__count
#     def __contains__(self, item): # 查询某个数据是否存在
#         # 对象的查询属于对象比较的操作，因此对于外部来讲，正确的比较是“==”运算
#         current_node = self.__root # 迭代由根节点展开
#         # 现代的开发之中，不提倡使用递归操作，而是提倡通过循环的形式来代替递归结构，因为避免栈溢出
#         while current_node != None: # 节点存在
#             # 此时直接实现了对象的比较，因此通过“==”与“__eq__()”特殊方法关联
#             if current_node.data == item: # 数据匹配
#                 return True # 数据存在
#             # 修改当前节点，当前节点的下一个为新的当前节点
#             current_node = current_node.next # 修改节点
#         return False # 数据不存在
#     def __iter__(self): # 返回迭代对象
#         self.__current = self.__root # 配置当前节点引用
#         return self # 链表本身就属于一个可迭代
#     def __next__(self): # 获取数据内容
#         if self.__current == None: # 链表无数据
#             # Python对于链表数据的返回操作，如果已经没有内容了，必须使用如下语法
#             raise StopIteration() # 结束迭代异常
#         data = self.__current.data # 获取当前节点之中的数据
#         self.__current = self.__current.next # 修改引用指向
#         return data # 返回节点数据
# class Book: # 保存对象
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name')
#         self.__author = kwargs.get('author')
#     def __eq__(self, other): # 准备好对象比较的功能
#         if other == None: # 数据为空
#             return False # 对象不等
#         if id(self) == id(other): # 地址相同
#             return True
#         if self.__hash__() == other.__hash__(): # 哈希码相同
#             return True
#         if self.__name == other.__name and self.__author == other.__author: # 属性比较相同
#             return True
#         return False # 对象不等
#     def __hash__(self): # 哈希码操作
#         result = (self.__name + ' - ' + str(len(self.__name)) + ',' +
#                   self.__author + ' - ' + str(self.__author)) # 计算规则
#         return object.__hash__(result)
#     def __str__(self): # 对象信息
#         return f'\t【图书】名称：《{self.__name}》、作者：{self.__author}'
# def main(): # 主函数
#     link = Link() # 实例化链表对象
#     link.add(Book(name='Python开发实战', author='李兴华'))
#     link.add(Book(name='Java程序设计开发实战', author='李兴华'))
#     link.add(Book(name='Java进阶开发实战', author='李兴华'))
#     print('【链表】数据保存个数：%d' % len(link))
#     print('【链表】数据查询判断：%d' % (Book(name='Python开发实战', author='李兴华') in link))
#     print('【链表】数据查询判断：%d' % (Book(name='Spring开发实战', author='马老师') in link))
#     print('【链表】迭代输出链表中全部的数据项：')
#     for book in link: # 链表迭代
#         print(book)
# if __name__ == '__main__':  # Python程序运行起点
    # main() # 调用主函数
# 单向链表
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/特殊方法/Collection iteration support.py"    
# 【链表】数据保存个数：3
# 【链表】数据查询判断：1
# 【链表】数据查询判断：0
# 【链表】迭代输出链表中全部的数据项：
#         【图书】名称：《Python开发实战》、作者：李兴华        
#         【图书】名称：《Java程序设计开发实战》、作者：李兴华  
#         【图书】名称：《Java进阶开发实战》、作者：李兴华      
# PS E:\summer_study\python开发\programe\pythonProject>

# 
# class Link: # 链表工具类
#     # 之所以使用内部类的结构，是因为该Node类只服务于Link类
#     class Node: # 链表节点类
#         def __init__(self, **kwargs): # 设置节点初始化
#             # 每一个节点只能够保存一个数据（这个数据可以是任意的内容，或者是其他的序列结构）
#             # 此时的data并没有进行封装处理，因为Node是内部类，这个类为Link服务
#             self.data = kwargs.get('data') # 保存节点数据
#         def __getattr__(self, item):
#             return None
#     # ------------------------------- 外部类功能定义 ----------------------------------------
#     def __init__(self): # 外部类构造方法
#         # 第一个保存的数据默认为根节点
#         self.__root = None # 定义根节点
#         self.__last = None # 保存最后一个增加的节点
#         self.__count = 0 # 进行保存数据个数统计
#     def add(self, data): # 数据保存
#         # 保存的数据本身是无法进行先后顺序配置的，因此这个时候要将内容封装在Node节点之中
#         newNode = Link.Node(data = data) # 封装的目的是为了区分先后顺序
#         # 在每一个链表对象之中，都会包含有一个根节点，因此将第一个数据作为根节点
#         if self.__root == None: # 没有根节点，是一个新链表
#             self.__root = newNode # 将新的节点配置为根节点
#             self.__last = newNode # 最新的节点为最后的节点
#         else: # 如果根节点已经存在了
#             # 现在假设每一个节点之中都存在有一个next属性（Python可以动态扩充对象的成员属性）
#             self.__last.next = newNode # 问题来了
#             self.__last = self.__last.next # 修改引用配置
#             # 每一个节点的next属性是在某一个数据添加的时候才会配置的属性，如果没有添加则没有该属性
#         self.__count += 1 # 数量自增
#     def __len__(self): # 获取集合的长度
#         return self.__count
#     def __contains__(self, item): # 查询某个数据是否存在
#         # 对象的查询属于对象比较的操作，因此对于外部来讲，正确的比较是“==”运算
#         current_node = self.__root # 迭代由根节点展开
#         # 现代的开发之中，不提倡使用递归操作，而是提倡通过循环的形式来代替递归结构，因为避免栈溢出
#         while current_node != None: # 节点存在
#             # 此时直接实现了对象的比较，因此通过“==”与“__eq__()”特殊方法关联
#             if current_node.data == item: # 数据匹配
#                 return True # 数据存在
#             # 修改当前节点，当前节点的下一个为新的当前节点
#             current_node = current_node.next # 修改节点
#         return False # 数据不存在
#     def __iter__(self): # 返回迭代对象
#         self.__current = self.__root # 配置当前节点引用
#         return self # 链表本身就属于一个可迭代
#     def __next__(self): # 获取数据内容
#         if self.__current == None: # 链表无数据
#             # Python对于链表数据的返回操作，如果已经没有内容了，必须使用如下语法
#             raise StopIteration() # 结束迭代异常
#         data = self.__current.data # 获取当前节点之中的数据
#         self.__current = self.__current.next # 修改引用指向
#         return data # 返回节点数据
#     def __setitem__(self, key, value): # 修改指定索引的数据
#         if key > self.__count: # 设置的索引超过了长度
#             return # 结束调用
#         current_node = self.__root # 从根节点开始循环
#         # 当前是依据索引的方式修改内容的，因此需要根据索引找到对应的节点，而后再更新内容
#         index = 0 # 设置索引
#         while current_node != None: # 存在有节点
#             if key == index: # 索引相同
#                 current_node.data = value # 更新数据
#                 return # 结束方法调用
#             current_node = current_node.next # 指向下一个节点
#             index += 1 # 修改索引内容
# class Book: # 保存对象
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name')
#         self.__author = kwargs.get('author')
#     def __eq__(self, other): # 准备好对象比较的功能
#         if other == None: # 数据为空
#             return False # 对象不等
#         if id(self) == id(other): # 地址相同
#             return True
#         if self.__hash__() == other.__hash__(): # 哈希码相同
#             return True
#         if self.__name == other.__name and self.__author == other.__author: # 属性比较相同
#             return True
#         return False # 对象不等
#     def __hash__(self): # 哈希码操作
#         result = (self.__name + ' - ' + str(len(self.__name)) + ',' +
#                   self.__author + ' - ' + str(self.__author)) # 计算规则
#         return object.__hash__(result)
#     def __str__(self): # 对象信息
#         return f'\t【图书】名称：《{self.__name}》、作者：{self.__author}'
# def main(): # 主函数
#     link = Link() # 实例化链表对象
#     link.add(Book(name='Python开发实战', author='李兴华'))
#     link.add(Book(name='Java程序设计开发实战', author='李兴华'))
#     link.add(Book(name='Java进阶开发实战', author='李兴华'))
#     print('【链表】数据保存个数：%d' % len(link))
#     print('【链表】数据查询判断：%d' % (Book(name='Python开发实战', author='李兴华') in link))
#     print('【链表】数据查询判断：%d' % (Book(name='Spring开发实战', author='马老师') in link))
#     link[1] = Book(name='MySQL开发实战', author='李兴华') # 修改指定索引的数据
#     print('【链表】迭代输出链表中全部的数据项：')
#     for book in link: # 链表迭代
#         print(book)
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
#PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/特殊方法/Collection iteration support.py"    
# 【链表】数据保存个数：3
# 【链表】数据查询判断：1
# 【链表】数据查询判断：0
# 【链表】迭代输出链表中全部的数据项：
#         【图书】名称：《Python开发实战》、作者：李兴华        
#         【图书】名称：《MySQL开发实战》、作者：李兴华
#         【图书】名称：《Java进阶开发实战》、作者：李兴华

class Link: # 链表工具类
    # 之所以使用内部类的结构，是因为该Node类只服务于Link类
    class Node: # 链表节点类
        def __init__(self, **kwargs): # 设置节点初始化
            # 每一个节点只能够保存一个数据（这个数据可以是任意的内容，或者是其他的序列结构）
            # 此时的data并没有进行封装处理，因为Node是内部类，这个类为Link服务
            self.data = kwargs.get('data') # 保存节点数据
        def __getattr__(self, item):
            return None
    # ------------------------------- 外部类功能定义 ----------------------------------------
    def __init__(self): # 外部类构造方法
        # 第一个保存的数据默认为根节点
        self.__root = None # 定义根节点
        self.__last = None # 保存最后一个增加的节点
        self.__count = 0 # 进行保存数据个数统计
    def add(self, data): # 数据保存
        # 保存的数据本身是无法进行先后顺序配置的，因此这个时候要将内容封装在Node节点之中
        newNode = Link.Node(data = data) # 封装的目的是为了区分先后顺序
        # 在每一个链表对象之中，都会包含有一个根节点，因此将第一个数据作为根节点
        if self.__root == None: # 没有根节点，是一个新链表
            self.__root = newNode # 将新的节点配置为根节点
            self.__last = newNode # 最新的节点为最后的节点
        else: # 如果根节点已经存在了
            # 现在假设每一个节点之中都存在有一个next属性（Python可以动态扩充对象的成员属性）
            self.__last.next = newNode # 问题来了
            self.__last = self.__last.next # 修改引用配置
            # 每一个节点的next属性是在某一个数据添加的时候才会配置的属性，如果没有添加则没有该属性
        self.__count += 1 # 数量自增
    def __len__(self): # 获取集合的长度
        return self.__count
    def __contains__(self, item): # 查询某个数据是否存在
        # 对象的查询属于对象比较的操作，因此对于外部来讲，正确的比较是“==”运算
        current_node = self.__root # 迭代由根节点展开
        # 现代的开发之中，不提倡使用递归操作，而是提倡通过循环的形式来代替递归结构，因为避免栈溢出
        while current_node != None: # 节点存在
            # 此时直接实现了对象的比较，因此通过“==”与“__eq__()”特殊方法关联
            if current_node.data == item: # 数据匹配
                return True # 数据存在
            # 修改当前节点，当前节点的下一个为新的当前节点
            current_node = current_node.next # 修改节点
        return False # 数据不存在
    def __iter__(self): # 返回迭代对象
        self.__current = self.__root # 配置当前节点引用
        return self # 链表本身就属于一个可迭代
    def __next__(self): # 获取数据内容
        if self.__current == None: # 链表无数据
            # Python对于链表数据的返回操作，如果已经没有内容了，必须使用如下语法
            raise StopIteration() # 结束迭代异常
        data = self.__current.data # 获取当前节点之中的数据
        self.__current = self.__current.next # 修改引用指向
        return data # 返回节点数据
    def __setitem__(self, key, value): # 修改指定索引的数据
        if key > self.__count: # 设置的索引超过了长度
            return # 结束调用
        current_node = self.__root # 从根节点开始循环
        # 当前是依据索引的方式修改内容的，因此需要根据索引找到对应的节点，而后再更新内容
        index = 0 # 设置索引
        while current_node != None: # 存在有节点
            if key == index: # 索引相同
                current_node.data = value # 更新数据
                return # 结束方法调用
            current_node = current_node.next # 指向下一个节点
            index += 1 # 修改索引内容
    def __getitem__(self, item): # 获取数据
        if item > self.__count: # 设置的索引超过了长度
            return None # 结束调用
        index = 0  # 设置索引
        current_node = self.__root  # 从根节点开始循环
        while current_node != None:  # 存在有节点
            if item == index:  # 索引相同
                return current_node.data # 结束方法调用
            current_node = current_node.next  # 指向下一个节点
            index += 1  # 修改索引内容
class Book: # 保存对象
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
    def __eq__(self, other): # 准备好对象比较的功能
        if other == None: # 数据为空
            return False # 对象不等
        if id(self) == id(other): # 地址相同
            return True
        if self.__hash__() == other.__hash__(): # 哈希码相同
            return True
        if self.__name == other.__name and self.__author == other.__author: # 属性比较相同
            return True
        return False # 对象不等
    def __hash__(self): # 哈希码操作
        result = (self.__name + ' - ' + str(len(self.__name)) + ',' +
                  self.__author + ' - ' + str(self.__author)) # 计算规则
        return object.__hash__(result)
    def __str__(self): # 对象信息
        return f'\t【图书】名称：《{self.__name}》、作者：{self.__author}'
def main(): # 主函数
    link = Link() # 实例化链表对象
    link.add(Book(name='Python开发实战', author='李兴华'))
    link.add(Book(name='Java程序设计开发实战', author='李兴华'))
    link.add(Book(name='Java进阶开发实战', author='李兴华'))
    print('【链表】数据保存个数：%d' % len(link))
    print('【链表】数据查询判断：%d' % (Book(name='Python开发实战', author='李兴华') in link))
    print('【链表】数据查询判断：%d' % (Book(name='Spring开发实战', author='马老师') in link))
    link[1] = Book(name='MySQL开发实战', author='李兴华') # 修改指定索引的数据
    print('【链表】迭代输出链表中全部的数据项：')
    for book in link: # 链表迭代
        print(book)
    print('【链表】获取指定索引数据：%s' % link[0])
    print('【链表】获取指定索引数据：%s' % link[1])
    print('【链表】获取指定索引数据：%s' % link[6])
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/特殊方法/Collection iteration support.py"    
# 【链表】数据保存个数：3
# 【链表】数据查询判断：1
# 【链表】数据查询判断：0
# 【链表】迭代输出链表中全部的数据项：
#         【图书】名称：《Python开发实战》、作者：李兴华        
#         【图书】名称：《MySQL开发实战》、作者：李兴华
#         【图书】名称：《Java进阶开发实战》、作者：李兴华      
# 【链表】获取指定索引数据：      【图书】名称：《Python开发实战》、作者：李兴华
# 【链表】获取指定索引数据：      【图书】名称：《MySQL开发实战 》、作者：李兴华
# 【链表】获取指定索引数据：None





