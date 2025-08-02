num_a = input('请输入乘法运算中的第一个数字：')
num_b = input('请输入乘法运算中的第二个数字：')
# int()函数可以将字符串转为整型数据
result = int(num_a) * int(num_b) # 数字的乘法计算
# num_a和num_b都是由键盘输入的字符串，因此直接进行字符串连接即可
# result是一个计算出来的结果，是一个数字，使用str()将数字转为字符串
print('【乘法运算】' + num_a + ' × ' + num_b + ' = ' + str(result))
flag = bool(input('确定要发送此信息吗？')) # 输入数据直接转换
print('【布尔】类型：' + str(type(flag)) + '、内容：' + flag.__str__())
print('【布尔】类型：' + str(type(flag)) + '、内容：' + str(flag))
message = input('请输入任意的数据一：')
print('【输入检查一】是否输入数据：' + bool(message.strip()).__str__())
message = input('请输入任意的数据二：')
print('【输入检查二】是否输入数据：' + bool(message.strip()).__str__())
num_a = float(input('请输入计算的第一个数字：')) # 输入数据并转为浮点型
num_b = float(input('请输入计算的第二个数字：')) # 输入数据并转为浮点型
print('【除法计算】' + str(num_a) + ' ÷ ' + str(num_b) + ' = ' + str(num_a / num_b))



