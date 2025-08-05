# 偏函数
import functools # 模块导入
def add(x, y=3): # 加法计算函数
    return x + y;
def main(): # 主函数
    plus = functools.partial(add, 100) # x参数的内容统一为100
    print('【函数调用】加法计算：%s' % plus()) # 第2个参数有默认值
    print('【函数调用】加法计算：%s' % plus(5))
    # 调用 plus(y) 相当于调用 add(100, y)。
    # plus 已经固定了 x=100(不可替换)，所以 y 的值会覆盖默认值 3

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


#                                                     > & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/模块的定义与使用/partial function.py"        
# 【函数调用】加法计算：103
# 【函数调用】加法计算：105

#######################################
import functools # 模块导入
def write_book(*args, **kwargs):
    return f'【图书创作】名称：《{kwargs.get("name")}》、作者：{kwargs.get("author")}、特点：{args}'
def main(): # 主函数
    # 此时对已有的图书创作函数进行了包装，可以增加很多固定参数的内容
    wrapper = functools.partial(write_book, '图书', '系统', '案例', author='李兴华')
    print(wrapper('零基础', name='Python开发实战'))
    print(wrapper('就业', name='Java程序设计开发实战'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【图书创作】名称：《Python开发实战》、作者：李兴华、特点：('图书', '系统', '案例', '零基础')
# 【图书创作】名称：《Java程序设计开发实战》、作者：李兴华、特点：('图书', '系统', '案例', '就业')