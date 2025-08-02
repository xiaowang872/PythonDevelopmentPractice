# 列表字符串连接，增删改查等
# 定义一个列表，这个列表的内容可以随意添加
skills = ["Python","Python",["Java", "JavaScript"],"C++", "C#"]
print(skills)
skills.append('Linux') # 在列表尾部追加数据
# 列表也属于序列的一种，因此所有的数据项都有索引数值
skills.insert(0, 'C语言') # 在指定索引位置上添加数据
print('获取列表全部数据', skills)
print('获取指定索引数据，索引为0', skills[0])
print('列表数据的分片操作', skills[0 : 2 : 1])
# 列表中的数据删除时，是区分大小写的，因此如果没有匹配成功，则无法删除，会直接报错
print('删除列表数据', skills.remove('Python'))
# print('删除列表数据', skills.remove('python'))
#这个会报错，因为列表中没有'python'这个数据而是'Python'
print(skills) 
print('删除列表最后一个数据', skills.pop())
print('获取列表长度', len(skills))
print('判断列表中是否包含某个数据', 'Python' in skills)
print(skills)  
#删除的方式一种remove()，另一种是pop()，remove()是删除指定数据(大小写敏感)，而pop()是删除指定索引位置上的数据
#如果不指定索引位置，则默认删除最后一个数据
print("###################################################")
# 使用字符串连接方式处理列表
skills = ["Python","Python","Java", "JavaScript","C++", "C#"]
print("处理后的列表数据为：" + str(skills))
print("处理后的列表数据为：" + " , ".join(skills))
# 在列表之中使用“+”表示的是列表的连接操作，即：若干个不同的列表变为一个完整列表
skills = ['Python'] * 3 + ['Java'] * 5 # 定义一个列表
print(skills)
print("####################列表的拷贝操作#########################")
# copy()方法是列表的拷贝操作
skill_a = ['Java', 'Python', 'Go'] # 定义列表
skill_b = skill_a.copy() # 列表拷贝
print('【1】观察skill_a列表的内存地址：', id(skill_a)) # 2172287852416
print('【1】观察skill_b列表的内存地址：', id(skill_b)) # 2172288031936
skill_a.append('SQL') # 列表一追加数据
skill_b.append('HTML') # 列表二追加数据
print('【2】观察skill_a列表内容：', skill_a)
print('【2】观察skill_b列表内容：', skill_b)
# 列表变字符串,字符串连接
# print('【3】观察skill_a列表的id：'+ skill_a)
print('【3】观察skill_a列表的id：'+ skill_a.__str__()) # 使用__str__()方法将列表转换为字符串
print('【3】观察skill_b列表的id：'+ str(skill_b)) # 使用__str__()方法将列表转换为字符串
print("####################列表的扩展操作#########################")
skill = ['Java', 'Python', 'Go'] # 定义基础列表
# 对已有列表的功能进行扩展，等于“+”的功能，将新的数据添加到已有的列表内容之后
skill.extend(['Node.JS', 'Java', 'Python', 'C', 'C++'])
print('【4】观察skill列表内容：', skill) # 扩展后的列表内容
# 数据查询表示
print('【5】查询skill列表中是否包含Python：', 'Python' in skill) # 查询skill列表中是否包含Python
print('【6】数据查找：', skill.index('Python')) # 查找skill列表中Python的索引位置
print('【7】数据查找：', skill.index('Java')) # 查找skill列表中Java的索引位置
# 数据排序
print("#######################列表的排序操作#########################")
skill = [1, 5, 0, 2, 3, 6, 8]  # 定义基础列表
# 列表的排序操作是在同一块内存空间进行的，而此处是将排序的结果给了另外一个变量
# 既然是变量就需要为其分配内存地址，因此内存地址不同（内容是None）
skill_sort = skill.sort() # 数据排序
print('原始列表内存地址：', id(skill)) # 2687324770560
print('排序列表内存地址：', id(skill_sort)) # 140703559951872
print('列表排序后的内容：', skill)
skill.reverse() # 列表反转
print('列表反转后的内容：', skill)




