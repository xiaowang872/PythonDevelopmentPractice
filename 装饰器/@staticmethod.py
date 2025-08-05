# 静态方法

# class Book: # 自定义消息类
#     __press = 'YOOTK-沐言科技民间出版社' # 图书的公共属性
#     @staticmethod # 明确的标注该方法为静态方法
#     def press(): # 静态方法不受到对象的限制
#         return Book.__press # 返回公共的信息
# def main(): # 主函数
#     print(Book.press()) # 类名称直接调用
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/装饰器/@staticmethod.py
# YOOTK-沐言科技民间出版社
##################################################################
# ！！！！！！！！！！！__new__在实例化之前运行

class Book: # 自定义消息类
    @staticmethod # 按照原有的结构定义方法
    def __new__(cls, *args, **kwargs):
        print('【实例化】类名称：%s、可变参数：%s、命名参数：%s' % (cls, args, kwargs))
        if len(args) == 0 or len(kwargs) == 0: # 没有传递可变参数和命名参数
            return None # 返回空对象
        return object.__new__(cls) # 对象实例化
    def __init__(self, *args, **kwargs): # 此时已经有了实例化对象
        print('【构造方法】调用Book类构造方法，进行Book类属性初始化，此时已经有了实例化对象')
        self.__items = args # 保存图书内容项（可变参数）
        self.__name = kwargs.get('name') # 命名参数
        self.__author = kwargs.get('author') # 命名参数
    def __str__(self):
        return f'【图书】名称：{self.__name}、作者：{self.__author}、技术项：{"、".join(self.__items)}'
def main(): # 主函数
    print(Book('Basic', '数据库', 'Web开发', name='《Python开发实战》', author='李兴华'))
    print('-' * 100)
    print(Book())
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/装饰器/@staticmethod.py
# 【实例化】类名称：<class '__main__.Book'>、可变参数：('Basic', '数据库', 'Web开发')、命名参数：{'name': '《Python开发实战》', 'author': '李兴华'}
# 【构造方法】调用Book类构造方法，进行Book类属性初始化，此时已经有了实例化对象
# 【图书】名称：《Python开发实战》、作者：李兴华、技术项：Basic 、数据库、Web开发
# ----------------------------------------------------------------------------------------------------
# 【实例化】类名称：<class '__main__.Book'>、可变参数：()、命名 参数：{}
# None
# PS E:\summer_study\python开发\programe\pythonProject>





