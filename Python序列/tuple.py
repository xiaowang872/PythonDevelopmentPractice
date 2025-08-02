author = ('李兴华', '沐言科技', 'YOOTK') # 定义元组
print('元组内容：', author)
# 可以将元组中的内容依次取出，而后与特定的字符串进行连接
print(type(author)) # 查看元组类型
print('元组内容：', ', '.join(author))
# 列表转化元组
skills = ['Python', 'Java', 'C++'] # 定义列表
skills_tuple = tuple(skills) # 列表转化元组
print('元组内容：', skills_tuple)
# 将字符串转为元组
str_tuple = tuple('Hello World')
print('元组内容：', str_tuple)
# 变相修改元组内容
author = ('李兴华', '沐言科技', 'YOOTK', '新内容') # 重新定义元组
print('元组内容：', author)
# 将字符串转为列表
str_list = list('李兴华，《Python开发实战》')
print(type(str_list))
print('字符串列表集合：', str_list) # 字符串转为列表
# 将一个元组的结构转为列表，因为元组使用“()”进行定义
book_list = list(('Java程序设计开发实战', 'Python开发实战', 'MySQL开发实战'))
# book_list = list(tuple(['Java程序设计开发实战', 'Python开发实战', 'MySQL开发实战']))
print('图书列表集合：', book_list)
# 重要部分
my_tuple = ('Hello ', ) # 只有一个元素
print('变量类型：', type(my_tuple))
my_tuple = ('Hello ') # 只有一个元素
print('变量类型：', type(my_tuple))