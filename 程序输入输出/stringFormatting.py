author = '李兴华' # 定义字符串变量
book = '《Python开发实战》' # 字符串变量
# 这个时候将按照“{}”占位的顺序进行内容的填充
message_a = '【图书】作者：{}、名称：{}'.format(author, book) # 字符串格式化
print(message_a)
# 如果非要给它名字，那么难受的一定是你自己
message_b = '【图书】作者：{author_param}、名称：{book_param}' \
                .format(book_param=book, author_param=author)
print(message_b)
# 如果非要将序号反过来，那么绝对是人中的王者
message_c = '【图书】作者：{1}、名称：{0}'.format(book, author)
print(message_c)
print('----------------------------------------------------------------------------------------------------------------')
infos_a = ['李兴华', '《Python开发实战》'] # 定义列表结构
# 列表集合在进行数据访问的时候可以根据索引获取内容，因此此时就是通过索引匹配
message_a = '【图书】作者：{param[0]}、名称：{param[1]}'.format(param=infos_a)
print(message_a)
infos_b = dict(author='李兴华', book='《Python开发实战》') # 字典结构
# 如果要进行字典之中的key匹配，则必须使用“**”运算符来作为参数
message_b = '【图书】作者：{author}、名称：{book}'.format(**infos_b)
print(message_b)
print('【编码】UNICODE编码：{msg!a}'.format(msg='Python开发实战'))
print('【进制】十进制转二进制：{num:b}'.format(num=915))
print('【进制】十进制转八进制：{num:o}'.format(num=915))
print('【进制】十进制转十六进制：{num:x}'.format(num=915))
print("########################################")
print('【居中显式】{msg:^30}'.format(msg=' 李兴华，Python '))
print('【数据填充】{msg:=^30}'.format(msg=' 李兴华，Python '))
print('【数据对齐】{num:>30}'.format(num=915))
print('【数据分割】{num:>30,}'.format(num=9152892923.223231231323423434))
print('【数据精度】{num:.2}'.format(num=9152892923.223231231323423434))

book = '《Python开发实战》'
author = '李兴华'
# f'字符串' == '字符串'.format()
print(f'【图书】名称：{book}、作者：{author}') # 字符串格式化