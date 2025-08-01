# 字符串
message = "小王" + "，" + '《Python开发》'
result = '数学加法计算：' + str(10 + 20)
print('字符串输出一', message)
print('字符串输出二', result)
print('###################')
# \n：表示进行换行
# \t：表示与按下“Tab”键同样的效果
message = '\"小王\"\n\t《\'Python\'开发》'
print(message)
message = '''《Python开发实战》，该书包括如下内容：
1、Python开发环境搭建
2、Python基础语法
3、Python面向对象
基本上你能见到收费的Python培训课程，俺们书里都包含了。
'''
print(message)
 # 字符串前后都有空格，而且字符串中的字符有大写和小写
message = '               【Yootk】阿巴阿，     《Python开发实战》1234567890    '
print('原始字符串', message)
# 左右空格可以取消，但是中间的空格不能取消，因为这种操作是便于用户输入的
print('去掉左右空格', message.strip())
# 在进行字符串大小写转换的过程之中，非字符串的内容不会发生任何的改变
print('字符串转大写', message.upper())
print('字符串转小写', message.lower())
# 查找字符串索引位置的时候，返回的是第一个匹配字符的位置的索引
print('查找字符串的索引位置', message.find('Python'))
print('字符串居中显式', message.center(80, '*'))
print("#########数据分片########")
message = '阿巴阿，《Python开发实战》1234567890' # 定义字符串
start_index = message.find('Python') # 查找索引
print('查找索引：', start_index)
print('数据分片：', message[message.find('Python') : message.find('Python') + 15])



