# 元数据
class Book: # 自定义图书类
    def author(self):
        return 'YOOTK - 李兴华'
def main(): # 主函数
    book = Book() # 实例化对象
    print('【数据类型】%s' % book.__class__)
    print('【数据类型】%s' % type(book))
    print('【数据类型】%s' % type(book.author()))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
#PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/装饰器/metaclass.py
# 【数据类型】<class '__main__.Book'>
# 【数据类型】<class '__main__.Book'>
# 【数据类型】<class 'str'>

########################################
class YootkType(type): # 元配置类
    @staticmethod
    def __new__(cls, name, bases, dict):
        print('【元类型】类型：%s、子类名称：%s、父类：%s' % (cls, name, bases))
        dict['author'] = 'YOOTK - 李兴华' # 添加公共属性
        return super(YootkType, cls).__new__(cls, name, bases, dict) # 对象构建
class Book(object, metaclass=YootkType): # 创建子类，并设置一个元类型
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
    def __str__(self):
        return f'【程序图书】名称：{self.__name}、作者：{self.author}' # 公共的作者信息
def main(): # 主函数
    book = Book(name='Python开发实战') # 对象实例化
    print(book)
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【元类型】类型：<class '__main__.YootkType'>、子类名称：Book、父类：(<class 'object'>,)
# 【程序图书】名称：Python开发实战、作者：YOOTK - 李兴华

#######################
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【子类实例判断】True
# 【子类实例判断】True
# 【子类实例判断】False
# PS E:\summer_study\python开发\programe\pythonProject>