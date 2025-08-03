# 该变量定义在Python程序之中，不在任何的子结构里面
num = 100 # 全局变量
num2 = 100 # 全局变量
def update_number():
    # 此时在函数内部定义了一个新的变量，名称为num
    # 按照LEGB原则，内部的局部变量应该被首先访问
    num = 30 # 定义了一个新的变量
def update_number2():
    global num2 # 函数后续的操作为全局变量操作
    num2 = 30 # 定义了一个新的变量


def counter(): # 计数器
    number3 = 10 # 外部函数局部变量
    def increment(): # 计数器的自增
        nonlocal number3 # 不是内部函数的局部变量
        number3 += 1 # 修改外部函数中的number变量内容
        return number3
    return increment # 返回内部函数引用

message = '沐言科技 - YOOTK' # 全局变量
author = '李兴华' # 全局变量


def main(): # 定义一个主函数
    update_number() # 希望修改num全局变量的内容
    print('【全局变量】num = %d' % num)
    update_number2() # 希望修改num全局变量的内容
    print('【全局变量】num2 = %d' % num2)
    count = counter() # 计数器函数引用
    print('【计数操作】当前数值：%d' % count())
    print('【计数操作】当前数值：%d' % count())
    print('【计数操作】当前数值：%d' % count())
    book_java = '《Java程序设计开发实战》' # 局部变量
    book_python = '《Python开发实战》' # 局部变量
    def hello(): # 内部函数
        pass
    print('【全局变量】%s' % globals())
    print('【局部变量】%s' % locals())




if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

