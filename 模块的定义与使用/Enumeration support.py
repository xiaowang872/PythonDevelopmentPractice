# 枚举支持

import enum # 导入枚举模块
@enum.unique # 定义枚举结构
class Item (enum.Enum): # 创建枚举类
    # 枚举项一般都使用大写字母表示，并且每一个枚举项都要有一个自己的数值
    PYTHON = 0 # 枚举项
    JAVA = 1 # 枚举项
    CPP = 2 # 枚举项
def main(): # 主函数
    print('【枚举信息】key = %s、value = %s' % (Item.PYTHON.name, Item.PYTHON.value))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/模块的定义与使用/Enumeration support.py"
# 【枚举信息】key = PYTHON、value = 0

###############################
import enum # 导入枚举模块
class ItemWrapper: # 类型信息
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name') # 类型名称
        self.__note = kwargs.get('note') # 类型说明
    def get_name(self):
        return self.__name
    def get_note(self):
        return self.__note
@enum.unique # 定义枚举结构
class Item (enum.Enum): # 创建枚举类
    PYTHON = ItemWrapper(name='python', note='辅助编程开发') # 枚举项
    JAVA = ItemWrapper(name='java', note='业务编程开发') # 枚举项
    CPP = ItemWrapper(name='c++',note='专业编程开发') # 枚举项
class Book: # 创建图书类
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
        self.__item = kwargs.get('item')
    def __str__(self):
        return f'【图书】名称：《{self.__name}》、作者：{self.__author}、' \
                f'分类：{self.__item.value.get_name()}（{self.__item.value.get_note()}）'
def main(): # 主函数
    print(Book(name='Python开发实战', author='李兴华', item=Item.PYTHON))
    print(Book(name='C++开发实战', author='李兴华', item=Item.CPP))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【图书】名称：《Python开发实战》、作者：李兴华、分类：python（辅助编程开发）
# 【图书】名称：《C++开发实战》、作者：李兴华、分类：c++（专业编程开发）



