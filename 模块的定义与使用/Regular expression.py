# 正则表达式
import re
def main(): # 主函数
    # 如果直接使用math()函数可以得到的是一个正则的结果，结果不为None就表示匹配成功
    # 匹配成功的内部会包含有指定数据的索引范围，因此这个时候可以通过span()函数获取到这个索引
    print('【正则】头部数据匹配：%s' % str(re.match('yootk', 'yootk-lixinghua').span()))
    print('【正则】头部数据匹配：%s' % str(re.match('yootk', 'yootk-lixinghua')))
    print('【正则】头部数据匹配：%s' % str(re.match('yootk', 'lixinghua-yootk')))
    print('【正则】头部数据匹配：%s' % str(re.search('yootk', 'muyan-yootk-lixinghua').span()))
    # re.search()函数是需要进行大小写区分的，因此这种时候可以考虑忽略掉大小写的逻辑
    print('【正则】任意位置数据匹配：%s' % str(re.search('yootk', 'muyan-YOOTK-lixinghua')))
    print('【正则】任意位置数据匹配：%s' % str(re.search('yootk', 'muyan-YOOTK-lixinghua', re.I)))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/模块的定义与使用/Regular expression.py"
# 【正则】头部数据匹配：(0, 5)
# 【正则】头部数据匹配：<re.Match object; span=(0, 5), match='yootk'>
# 【正则】头部数据匹配：None
# 【正则】头部数据匹配：(6, 11)
# 【正则】任意位置数据匹配：None
# 【正则】任意位置数据匹配：<re.Match object; span=(6, 11), match='YOOTK'>

import re
def main(): # 主函数
    # 正则里面会使用到许多的“\xx”开头的结构，因此为了可以清晰的描述出正则的规则定义，字符串前加上r
    # \d：表示一位数字，等价于“[0-9]”
    # 如果要表示多位数字，则需要追加量词定义，使用“+”表示1次或多次，等价“{1,}”
    # 小数点和小数位要一起出现，因此使用括号进行整体的定义，而后在里面通过“\.”描述小数点，使用“\d+”小数位
    # 整体的小数点和小数位只能够出现0次或1次，因此使用“?”实现量词的定义
    # 如果现在要进行某一个符号的匹配（+、-），那么就相当于设置了一个范围，范围的定义使用“[]”完成
    # 如果直接写上了一个范围，则表示必须出现一个，没出现的就表示不匹配，所以还要追加量词
    pattern = r"^[+-]?\d+(\.\d+)?$" # 定义正则匹配规则
    # 在之前讲解数据类型的时候曾经说过一个问题，就是说当输入的字符串不是由数字组成的时候，会出现异常
    # 因此在进行数据转型之前常用的做法就是进行字符串格式的验证，而这个验证就通过正则来完成。
    print('【正则】数字匹配：%s' % str(re.match(pattern, '20', re.I))) # 整数
    print('【正则】数字匹配：%s' % str(re.match(pattern, '915', re.I))) # 整数
    # 小数点应该和小数位一起出现（0或1），但是小数点理论上应该使用“.”描述，但是“.”属于正则规范的定义
    # 因此如果要使用正则规范内有定义的字符，则要进行转义处理，使用“\.”来标记
    print('【正则】数字匹配：%s' % str(re.match(pattern, '20.17', re.I))) # 小数
    print('【正则】数字匹配：%s' % str(re.match(pattern, '-20.17', re.I))) # 小数
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【正则】数字匹配：<re.Match object; span=(0, 2), match='20'>
# 【正则】数字匹配：<re.Match object; span=(0, 3), match='915'>
# 【正则】数字匹配：<re.Match object; span=(0, 5), match='20.17'>
# 【正则】数字匹配：<re.Match object; span=(0, 6), match='-20.17'>
# PS E:\summer_study\python开发\programe\pythonProject> 


import re
def main(): # 主函数
    pattern = r"""
        [a-zA-Z]            # 匹配第一个字母，由字母所组成，可大写可小写
        \w+@\w+                 # 字母、数字、下划线所组成，理论上的定义：“[a-zA-Z0-9_]”
        \.               # “.”表示任意的字符，因此需要通过转义字符来进行处理
        (cn|com|com.cn|net|gov)     # 通过括号作为整体匹配，没有量词必须出现1次，|表示或的逻辑
    """ # 用多行的形式定义正则，可以编写注释
    print('【正则】Email匹配：%s' % str(re.match(pattern, 'muyan@yootk.com', re.I | re.X)))
    print('【正则】Email匹配：%s' % str(re.match(pattern, 'muyan-yootk', re.I | re.X)))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【正则】Email匹配：<re.Match object; span=(0, 15), match='muyan@yootk.com'>
# 【正则】Email匹配：None