sum = 0 # 保存累加的计算结果
num = 1 # 循环条件初始化
while num <= 100: # 循环判断条件
    sum += num # 执行数据的累加操作
    num += 1 # 修改循环条件
print('【累加计算】1 ~ 100的数据累加结果：%d' % sum)
num = 1 # 循环条件初始化
abc=[]
while num <= 20: # 循环处理
    if num % 3 == 0: # 可以被3整除
        abc.append(num)
    num += 1 # 修改循环条件
print('【统计结果】可以被3整除的数字有：%s' % ', '.join(str(i) for i in abc))
sum = 0 # 保存数据累加结果
# for循环的结构基本上都是和序列的结构相关的，但是如果直接定义一个系列
# 此时生成了一个临时的序列，这个序列的内容是：1、2、3、...、100
print('【序列的生成】range(101) = %s' % range(101)) # 101指的是不超过的内容
for num in range(101): # for循环语句
    sum += num # 数据累加计算
print('【累加计算】1 ~ 100数据累加结果：%d' % sum)
skill = ['Java', 'Python', 'Go', 'C', 'C++', 'Rust', 'PHP']
for temp in skill: # 列表循环
    print('【列表数据】编程技能：%s' % temp)
# 现在创建了一个字典，字典里面包含有字符串内容以及元组和列表
member = dict(name='李兴华', company='沐言科技',
                skill=('Java', 'Python', '前端', 'Linux', '大数据', 'Go'),
                book=['《Java程序设计开发实战》', '《Python开发实战》', '《MySQL开发实战》'])
# 在使用for循环输出字典结构的时候，需要注意的是，每一次可以获取到的内容是两个：k、v
# items()方法返回的是一个元组，元组里面包含字典里所有的key和value
for key, value in member.items(): # 字典迭代
    print('【字典数据】类型 = %s、key = %s、value = %s' %
            (type(value), key, value))
print("########################################")
print('【字典数据】类型 = %s、key = %s、value = %s' %
        (type(value).__name__, key, value))
print("########################################")
for item in member.items(): # 字典迭代
    print('【字典数据】类型 = %s、长度：%s、key = %s、value = %s' %
            (type(item).__name__, len(item), item[0], item[1]))
print("########################################")
# 三角形打印
triangle_num = 5    #三角形打印总行数
for i in range(1, triangle_num + 1):  # 打印五行
    for j in range(1, triangle_num - i + 1):  # 打印空格的数量
        print(' ', end=' ')  # 打印空格
    for k in range(1, i + 1):  # 打印星号的数量
        print('*', end=' ')  # 打印星号，end=' '表示不换行
    print()  # 换行

triangle_line = 5 # 三角形打印总行数
for x in range(1, triangle_line + 1): # 打印5行
    for y in range(1, triangle_line - x + 1): # 打印空格的数量
        print(' ', end='') # 输出空格
    for y in range(1, x + 1): # 打印*的数量
        print('* ', end='') # 输出“*”
    print() # 打印空行

# 通过字符串格式化来简化
triangle_line = 5 # 三角形打印总行数
format_str = '{:^' + str(triangle_line * 2) + '}' # 设置对齐模式与长度
for x in range(1, triangle_line + 1): # 打印5行
    print(format_str.format('* ' * x)) # 数据填充

# 打印乘法表
for i in range(1, 10): # 外层循环控制行数
    for j in range(1, i + 1): # 内层循环控制列数
        print('%d * %d = %d' % (j, i, j * i), end='\t') # 打印乘法表内容
    print() # 换行
