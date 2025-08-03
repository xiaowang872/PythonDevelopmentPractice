class Book: # 类使用class关键字定义
    # 将本类中允许出现的属性以元组的形式进行了详细的定义
    __slots__ = ('__author', '__name', '__price')
    def set_author(self, author): # 设置属性
        self.__author = author # 属性初始化
    def set_name(self, name): # 设置属性
        self.__name = name
    def set_price(self, price): # 设置属性
        if price > 0: # 满足设置条件
            self.__price = price
        else:
            self.__price = 0
    def get_author(self): # 返回数据
        return self.__author # 返回属性
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get(self):
        return f'【图书】名称：《{self.__name}》、作者：{self.__author}、价格：{self.__price}'
def main(): # 定义一个主函数
    book = Book() # 实例化Book类对象
    book.set_author('李兴华') # 通过特定的数据接口访问私有属性
    book.set_name('Python开发实战')
    book.set_price(-79.8) # 自带保护机制
    
    # book.company = '沐言科技' # 属性无法封装

    print(book.get())


if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数




