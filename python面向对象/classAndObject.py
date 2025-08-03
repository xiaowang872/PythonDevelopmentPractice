class Book: # 类使用class关键字定义
    # 在类中定义的函数里面会自动有一个self的定义
    def set(self, author, name): # 属性设置方法
        # 采用“self.属性名称”的形式可以为对象动态的添加属性
        self.author = author # 进行对象属性赋值
        self.name = name # 进行对象属性赋值
    def get(self): # 获取属性内容
        return f'【图书】名称：《{self.name}》、作者：{self.author}' # 字符串格式化
class BookTmp: # 类使用class关键字定义
    def get(self): # 获取属性内容
        return id(self)


def main(): # 定义一个主函数
    # Python之中没有进行强制性变量类型的声明要求，因此变量直接定义并为其赋值即可
    book = Book() # 实例化Book类对象
    # 类一旦产生了实例化对象之后，就可以通过对象调用类中的方法
    book.set('李兴华', 'Python开发实战') # 不要去管self（当前对象）
    # set()方法执行完成之后，就可以进行对象属性的设置
    print(book.get()) # 返回对象的信息
    print('【类型】主函数：%s' % type(main))
    print('【类型】Book中的set()方法：%s' % type(book.set))
    # 如果要想获取类对象之中的某一个成员属性，那么就必须首先保证该属性存在
    print('【类型】Book类中的author属性：%s' % type(book.author))
    print("#########################################")
    book_a = Book() # 实例化Book类对象
    book_a.name = 'Java程序设计开发实战'
    book_a.author = '沐言科技-李兴华'
    print('【主函数】book_a实例化对象地址：%d' % id(book_a))
    book_b = Book() # 实例化Book类对象
    book_b.name = 'Python开发实战'
    book_b.author = 'YOOTK-李兴华'
    print('【主函数】book_b实例化对象地址：%d' % id(book_b))
    book_c = BookTmp()
    book_d = BookTmp()
    print('【主函数】book_c实例化对象地址：{}'.format(id(book_c)))
    print('【get()方法】“book_c.get()”返回地址：{:^20}'.format(book_c.get()))
    print('【主函数】book_d实例化对象地址：{}'.format(id(book_d)))
    print('【get()方法】“book_d.get()”返回地址：{:^20}'.format(book_d.get()))
    print("#############################")
    book_e = Book() # 实例化Book类对象
    book_e.author = '李兴华' # 分配对象成员属性
    book_e.name = 'Python开发实战' # 分配对象成员属性
    temp = book_e # 对象引用传递
    # book对象之中已经存在了name的属性，因此此时是进行属性修改
    temp.name = 'Java程序设计开发实战'
    print(book_e.get())
    
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数