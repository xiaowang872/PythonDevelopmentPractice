# input_data = input('请输入要发送的信息：')
# print('【信息响应】' + input_data)
# input_data = input('请输入你所掌握的编程技能，使用空格分割：')
# 既然由用户输入，那么首先要去掉左右空格，而后所有的数据统一转大写
# skill = input_data.strip().upper().split(' ') # 按照空格拆分
# print('【列表】你的技能为：' + str(skill))

print("##########将输入字符串转化为字典数据项#########")
map = input('请输入数据：').split(' ') # 将输入的内容直接拆分
# 字符串中的split()函数一旦执行之后，数据会以列表的结构返回
message = {} # 定义一个空的字典
message.update({map[0]: map[1]})
print('【字典】内容' + message.__str__())
# 弹出字典中的数据
print("##########弹出字典中的数据###########")
map = dict(java='《Java程序设计开发实战》', python='《Python开发实战》') # 字典集合
print('【字典】原始内容：' + map.__str__())
key = input('请输入要弹出数据的KEY：') # 等待用户输入
print('【字典】数据弹出：' + map.pop(key).__str__())
print('【字典】当前内容：' + map.__str__())