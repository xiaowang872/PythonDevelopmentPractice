RESOURCE = '资源下载：YOOTK - 沐言优拓'
class Book: # 图书类
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')
    def __str__(self):
        return f'【图书】名称：{self.__name}、作者：{self.__author}'
class Press: # 出版社
    def publish(self, book): # 图书出版
        print(book)
