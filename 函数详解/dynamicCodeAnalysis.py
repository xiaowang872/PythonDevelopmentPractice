# 代码动态解析：仅仅通过一个字符串就定义了要执行的代码

def main(): # 定义一个主函数
    num = 10 # 整型变量
    statement = '3 * num' # 定义程序语句
    result = eval(statement) # 动态解析字符串
    print('【乘法计算】3 * %d = %d' % (num, result))

statement = \
    "skill = ['Java', 'Python', 'Go', 'C++', 'RUST'] \n" \
    "print('【编程技能】', end='') \n" \
    "for item in skill: \n" \
    "   print(item, end='、')" # 定义多行语句
exec(statement, globals())
# 代码的预先编译
statement = \
    "skill = [] \n" \
    "for num in range(0, 3): \n" \
    "   item = input('请输入你所掌握的编程技能：') \n" \
    "   skill.append(item) \n" \
    "print('【编程技能】%s' % skill)" # 定义多行语句
code = compile(statement, '', 'exec')
exec(code, globals())



if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

