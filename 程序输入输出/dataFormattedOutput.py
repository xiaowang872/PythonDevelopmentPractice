# 数据格式化输出，这边vars()函数，返回当前作用域的所有变量
num_a = 10
num_b = 3
print('【除法计算】' + str(num_a) + ' ÷ ' + str(num_b) + ' = ' + str(num_a / num_b))
print('【除法计算】', num_a, ' ÷ ', num_b, ' = ', (num_a / num_b))
author = '李兴华'
book = '《Python开发实战》'
price = 89.80
version = 10 # 印刷版本
print('图书名称：%s、图书作者：%s、图书价格：%f、印刷版次：%d' %
        (book, author, round(price), version))
print('图书名称：%s、图书作者：%s、图书价格：%f、印刷版次：%d' %
        (book, author, round(price, 2), version)) # 保留2位小数
# 5.2f格式化：5位的长度，其中小数位占2位
print('图书名称：%s、图书作者：%s、图书价格：%5.2f、印刷版次：%d' %
        (book, author, round(price, 2), version))  # 保留2位小数
price = 89.8282828283 # 随意定义一个数字
# %10.2f：代表数据长度为10，其中小数位占2位，整数位占8位
print('【数字格式化】price = %10.2f' % price)
print('【数字格式化】price = %+10.2f' % price)
print('【数字格式化】price = %+010.2f' % price)

author = '李兴华'
book = '《Python开发实战》'
print('【图书】作者：%s、名称：%s' % (author, book))
print(vars()) # vars()是一个Python内置函数，提供了所有的变量存储字典
# %(author)s代表了填充标记，该标记与变量名称匹配
print('【图书】作者：%(author)s、名称：%(book)s' % vars())





