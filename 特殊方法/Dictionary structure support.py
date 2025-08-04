# 字典结构支持

# class BinaryTree: # 二叉树（BT）
#     class Entry: # 数据实体存储
#         def __init__(self, **kwargs):
#             self.key = kwargs.get('key')
#             self.value = kwargs.get('value')
###############################################################################

# class BinaryTree: # 二叉树（BT）
#     class Entry: # 数据实体存储
#         def __init__(self, **kwargs):
#             self.key = kwargs.get('key') # 数据KEY，依据此key找到对应的value
#             self.value = kwargs.get('value') # 数据关联的value内容
#     class Node: # 定义数据保存节点
#         def __init__(self, **kwargs): # 构造方法
#             # 此时的数据是一个二元偶对象，因此都是通过Entry对象封装的
#             self.data = kwargs.get('data') # 配置节点中的数据
#         def __getattr__(self, item): # 处理空属性问题
#             return None
##########################################################################################
# class BinaryTree: # 二叉树（BT）
#     class Entry: # 数据实体存储
#         def __init__(self, **kwargs):
#             self.key = kwargs.get('key') # 数据KEY，依据此key找到对应的value
#             self.value = kwargs.get('value') # 数据关联的value内容
#         # 节点之间是需要进行大小关系匹配的，小于根节点的数据放在左子树，大于的放在右子树
#         # 因此此时的Entry对象的内部将基于key的大小进行判断，如果不使用这些方法，就直接通过属性判断
#         def __lt__(self, other): # 小于判断（“<”运算符）
#             return self.key < other.key
#         def __gt__(self, other): # 大于判断（“>”运算符）
#             return self.key > other.key
#         def __eq__(self, other):
#             return self.key == other.key
#     class Node: # 定义数据保存节点
#         def __init__(self, **kwargs): # 构造方法
#             # 此时的数据是一个二元偶对象，因此都是通过Entry对象封装的
#             self.data = kwargs.get('data') # 配置节点中的数据
#         def __getattr__(self, item): # 处理空属性问题
#             return None
#         def set_node(self, newNode): # 添加新节点
#             # self为当前对象，在整个的节点处理之中被称为当前节点
#             # 每一个节点里面保存的数据类型为Entry，每一个Entry的内容为key和value的集合
#             if self.data < newNode.data: # 新节点的数据大于当前节点
#                 if self.right == None: # 当前节点没有右子树
#                     self.right = newNode # 保存新节点
#                 else: # 存在右子树
#                     return self.right.set_node(newNode) # 递归调用
#             elif self.data > newNode.data: # 内容小于当前节点数据
#                 if self.left == None: # 没有左子树
#                     self.left = newNode # 保存新节点
#                 else: # 存在左子树
#                     return self.left.set_node(newNode) # 递归调用
#             else: # 等于判断，要更新内容
#                 self.data.value = newNode.data.value # 更新节点的数据
#     # ------------------ 下面为二叉树的开发实现 ---------------------------
#     def __init__(self):
#         self.__root = None # 根节点
#         self.__count = 0 # 节点数量
#     def __setitem__(self, key, value): # 内容的设置
#         # 每一个字典数据的配置都一定采用的是key和value的组织模式
#         entry = BinaryTree.Entry(key=key, value=value) # 将数据保存在Entry实例之中
#         # 每一个存储的entry对象的内容，都属于一个节点的配置
#         newNode = BinaryTree.Node(data=entry) # 创建新的节点
#         self.__count += 1 # 保存个数
#         # 在进行数据保存的时候，如果保存了同样的key的内容，则应该将原始的value返回
#         if self.__root == None: # 没有根节点
#             self.__root = newNode # 根节点引用
#             return None # 没有数据存储的时候返回None
#         else: # 根节点存在
#             self.__root.set_node(newNode) # 交给Node类负责处理
#     def __len__(self):
#         return self.__count
# class Book: # 自定义图书类型
#     def __init__(self, **kwargs):
#         self.__name = kwargs.get('name') # 属性初始化
#         self.__author = kwargs.get('author') # 属性初始化
#     def __str__(self):
#         return f'【图书】名称：《{self.__name}》、作者：{self.__author}'
# def main(): # 主函数
#     binary_tree = BinaryTree() # 创建二叉树
#     # 在讲解字典的时候曾经分析过，作为字典的key建议使用字符串，因此这个时候如果是重复的字符串就发生替换
#     binary_tree['java_basic'] = Book(name='Java程序设计开发实战', author='李兴华') # 保存数据
#     binary_tree['java_adv'] = Book(name='Java进阶开发实战', author='李兴华') # 保存数据
#     binary_tree['python'] = Book(name='Python开发实战', author='李兴华') # 保存数据
#     print('【二叉树】保存数据量：%d' % len(binary_tree))
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# 
# PS E:\summer_study\python开发\programe\pythonProject>
#                                                     > & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/特殊方法/Dictionary structure support.py"    
# 【二叉树】保存数据量：3
# PS E:\summer_study\python开发\programe\pythonProject> 

class BinaryTree: # 二叉树（BT）
    class Entry: # 数据实体存储
        def __init__(self, **kwargs):
            self.key = kwargs.get('key') # 数据KEY，依据此key找到对应的value
            self.value = kwargs.get('value') # 数据关联的value内容
        # 节点之间是需要进行大小关系匹配的，小于根节点的数据放在左子树，大于的放在右子树
        # 因此此时的Entry对象的内部将基于key的大小进行判断，如果不使用这些方法，就直接通过属性判断
        def __lt__(self, other): # 小于判断（“<”运算符）
            return self.key < other.key
        def __gt__(self, other): # 大于判断（“>”运算符）
            return self.key > other.key
        def __eq__(self, other):
            return self.key == other.key
    class Node: # 定义数据保存节点
        def __init__(self, **kwargs): # 构造方法
            # 此时的数据是一个二元偶对象，因此都是通过Entry对象封装的
            self.data = kwargs.get('data') # 配置节点中的数据
        def __getattr__(self, item): # 处理空属性问题
            return None
        def set_node(self, newNode): # 添加新节点
            # self为当前对象，在整个的节点处理之中被称为当前节点
            # 每一个节点里面保存的数据类型为Entry，每一个Entry的内容为key和value的集合
            if self.data < newNode.data: # 新节点的数据大于当前节点
                if self.right == None: # 当前节点没有右子树
                    self.right = newNode # 保存新节点
                else: # 存在右子树
                    return self.right.set_node(newNode) # 递归调用
            elif self.data > newNode.data: # 内容小于当前节点数据
                if self.left == None: # 没有左子树
                    self.left = newNode # 保存新节点
                else: # 存在左子树
                    return self.left.set_node(newNode) # 递归调用
            else: # 等于判断，要更新内容
                self.data.value = newNode.data.value # 更新节点的数据
        def get_node(self, key): # 依据key获取数据内容
            if self.data.key == key: # 当前节点的key为查询的key
                return self.data.value # 返回当前的数据项
            else: # KEY不匹配
                if self.data.key < key: # 右子树
                    if self.right != None: # 存在右节点
                        return self.right.get_node(key) # 查找右子树
                    else: # 没有右子树
                        return None # 数据不存在
                else: # 左子树处理
                    if self.left != None: # 存在左节点
                        return self.left.get_node(key) # 查询左节点
                    else: # 没有左节点
                        return None # 没有数据项
    # ------------------ 下面为二叉树的开发实现 ---------------------------
    def __init__(self):
        self.__root = None # 根节点
        self.__count = 0 # 节点数量
    def __setitem__(self, key, value): # 内容的设置
        # 每一个字典数据的配置都一定采用的是key和value的组织模式
        entry = BinaryTree.Entry(key=key, value=value) # 将数据保存在Entry实例之中
        # 每一个存储的entry对象的内容，都属于一个节点的配置
        newNode = BinaryTree.Node(data=entry) # 创建新的节点
        self.__count += 1 # 保存个数
        # 在进行数据保存的时候，如果保存了同样的key的内容，则应该将原始的value返回
        if self.__root == None: # 没有根节点
            self.__root = newNode # 根节点引用
            return None # 没有数据存储的时候返回None
        else: # 根节点存在
            self.__root.set_node(newNode) # 交给Node类负责处理
    def __len__(self):
        return self.__count
    def __getitem__(self, item): # 数据获取
        if item == None: # 没有查询key
            return None
        return self.__root.get_node(item) # 由Node类负责
class Book: # 自定义图书类型
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name') # 属性初始化
        self.__author = kwargs.get('author') # 属性初始化
    def __str__(self):
        return f'【图书】名称：《{self.__name}》、作者：{self.__author}'
def main(): # 主函数
    binary_tree = BinaryTree() # 创建二叉树
    # 在讲解字典的时候曾经分析过，作为字典的key建议使用字符串，因此这个时候如果是重复的字符串就发生替换
    binary_tree['java_basic'] = Book(name='Java程序设计开发实战', author='李兴华') # 保存数据
    binary_tree['java_adv'] = Book(name='Java进阶开发实战', author='李兴华') # 保存数据
    binary_tree['python'] = Book(name='Python开发实战', author='李兴华') # 保存数据
    print('【二叉树】保存数据量：%d' % len(binary_tree))
    print('【二叉树】查找KEY为“python”的数据：%s' % binary_tree['python'])
    print('【二叉树】查找KEY为“mysql”的数据：%s' % binary_tree['mysql'])
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/特殊方法/Dictionary structure support.py"
# 【二叉树】保存数据量：3
# 【二叉树】查找KEY为“python”的数据：【图书】名称：《Python开发 实战》、作者：李兴华
# 【二叉树】查找KEY为“mysql”的数据：None
# PS E:\summer_study\python开发\programe\pythonProject>









