# get查询，pop删除，update更新，copy拷贝
# 创建一个包含有图书信息的字典集合，字典的KEY为技术名称，Value为对应的图书
# 当前的字典之中包含有四组二元偶对象的信息
book = {'java': '《Java程序设计开发实战》', 'python': '《Python开发实战》',
        'go': '《Go开发实战》', 'mysql': '《MySQL开发实战》'}
# 列表存储数据的目的是为了输出方便（输出目的）
# 元组存储数据的目的是为了进行标记
# 字典存储数据的目的是为了通过KEY查询对应的VALUE（查询目的）
print('【字典查询】java = ' + book['java']) # 根据key获取对应的value
print('【字典查询】python = ' + book['python']) # 根据key获取对应的value
# print('【字典查询】c = ' + book['c']) # 根据key获取对应的value
# 注意：如果字典中没有指定的key，则会报错
# dict()函数在创建的时候对于数据key可以编写，而key的类型推荐使用字符串结构
book = dict(java='《Java程序设计开发实战》', python='《Python开发实战》',
            go='《Go开发实战》', mysql='《MySQL开发实战》') # 内置的系统函数
print('【字典查询】java = ' + book['java']) # 根据key获取对应的value
print('【字典查询】python = ' + book['python']) # 根据key获取对应的value
# 创建两个不同的序列的结构，每一个结构都属于key=value的映射关系
content_a = ('java', '《Java程序设计开发实战》') # 创建一个元组
content_b = ['python', '《Python开发实战》'] # 创建一个列表
book = dict([content_a, content_b]) # 内置的系统函数
print('【字典查询】java = ' + book['java']) # 根据key获取对应的value
print('【字典查询】python = ' + book['python']) # 根据key获取对应的value
# 字典函数配置
book = {'java': '《Java程序设计开发实战》', 'python': '《Python开发实战》',
        'go': '《Go开发实战》', 'mysql': '《MySQL开发实战》'}
print('【数据查询】java = ' + str(book.get('java')))
# 使用get()函数进行字典数据查询的时候，如果该key不存在会返回None
print('【数据查询】c++ = ' + str(book.get('c++')))
# 使用get()函数可以通过一个默认值的参数来进行key不存在时的value内容
print('【数据查询】c++ = ' + str(book.get('c++', 'Not Founding')))
print("###############################")
book = {'java': '《Java程序设计开发实战》', 'python': '《Python开发实战》',
        'go': '《Go开发实战》', 'mysql': '《MySQL开发实战》'}
print('【数据查询】java = ' + str(book.get('java')))
# 使用get()函数进行字典数据查询的时候，如果该key不存在会返回None
print('【数据查询】c++ = ' + str(book.get('c++') == None))
# 如果更新的KEY不存在，则表示的是向已有的字典之中追加新的数据项
book.update({'mysql': '《MySQL开发实战》'}) # 更新字典数据
print('【字典】第一次更新后的结果', book)
# update()函数在更新的时候可以同时传入多组key=value映射结构
book.update({'java': '《Spring开发实战》', 'python': '《Python神经网络》'}) # key存在则进行更新
print('【字典】第二次更新后的结果', book)
book = {'java': '《Java程序设计开发实战》', 'python': '《Python开发实战》'}
book.update({'mysql': '《MySQL开发实战》'}) # 更新字典数据
print('【字典】原始内容：', book)
# 数据弹出的时候，会直接返回其保存的value的信息
print('【字典】根据KEY弹出数据：', book.pop('python'))
print('【字典】第一次弹出后的内容：', book)
# 当弹出一组数据之后，其内容是以元组的结构保存的
print('【字典】弹出一组数据：', book.popitem()) # 随机弹出
print('【字典】第二次弹出后的内容：', book)

# 在使用Python默认的标记创建字典时，内部允许提供有重复key的数据，重复的时候就进行内容的覆盖
book = {'java': '《Java程序设计开发实战》', 'python': '《Python开发实战》', 'mysql': '《MySQL开发实战》',
        'go': '《Go开发实战》', 'java': '《Spring Boot开发实战》', 'python': '《Python人工智能》'}
print('【字典】原始内容：', book)
keys = book.keys() # 获取全部的数据KEY
# 此时集合之中所有的数据key都按照dict_keys类型进行保存，其中对应的内容为列表
print('【字典KEY】数据KEY内容：', type(keys))
# Python的运算符之中存在有一种集合的运算符，使用IN判断某个数据是否存在于某个序列之中
# 包括列表、字符串、元组都可以使用此运算符，如果不存在使用NOT IN运算符来进行判断
print('【IN运算符】判断java的key是否存在：', 'java' in keys)
print('【IN运算符】判断html的key是否存在：', 'html' in keys)
print('【简化写法】判断python的key是否存在：', 'python' in book.keys())
print('元组集合：', book.items()) # 类型：<class 'dict_items'>
print('【字典】原始数据：', book)
del book['mysql'] # 删除数据
del book['go'] # 删除数据
print('【字典】数据删除：', book)
# 此时的字典里面保存有字符串、列表以及元组内容

author = dict(name='李兴华',
                skill=['java', 'python', 'HTML', 'go', 'c++'],
                dept=('技术部', '教学部', '财务部', '市场部')) # 创建字典集合
print('【字典】获取数据：name = ', author.get('name'))
print('【字典】获取数据：skill = ', author.get('skill'))
print('【字典】获取数据：dept = ', author.get('dept'))
print("##########字典拷贝##########")

author_a = dict(name='李兴华', skill=['java']) # 创建一个字典
# 此时的author_a和author_b应该是属于两块不同的堆内存空间
author_b = author_a.copy() # 拷贝字典集合
print('【1】观察内存空间的地址，author_a地址：' + str(id(author_a)) + '、author_b地址：' + str(id(author_b)))
# 此时在进行操作的时候，分别使用了不同的字典集合变量来进行的处理
author_a['skill'].append('python') # 扩充了字典中的子列表的数据
author_b['skill'].append('sql') # 扩充了字典中子列表的数据
print('【2】图书作者一：' + author_a.__str__())
print('【2】图书作者二：' + author_b.__str__())
# 当前内存关系为浅拷贝，只拷贝当前字典堆内存的地址，如果字典里还包含其他数据的应用，那么只会拷贝当前字典的堆内存地址
# 因此如果直接使用copy()函数，则代表author_a和author_b的堆内存地址skill子项，会指向同一块内存空间
print("##########字典深拷贝##########")
import copy # 导入copy模块
author_a = dict(name='李兴华', skill=['java']) # 创建一个字典
# 此时的author_a和author_b应该是属于两块不同的堆内存空间
author_b = copy.deepcopy(author_a) # 深拷贝
print('【1】观察内存空间的地址，author_a地址：' + str(id(author_a)) + '、author_b地址：' + str(id(author_b)))
# 此时在进行操作的时候，分别使用了不同的字典集合变量来进行的处理
author_a['skill'].append('python') # 扩充了字典中的子列表的数据
author_b['skill'].append('sql') # 扩充了字典中子列表的数据
print('【2】图书作者一：' + author_a.__str__())
print('【2】图书作者二：' + author_b.__str__())


