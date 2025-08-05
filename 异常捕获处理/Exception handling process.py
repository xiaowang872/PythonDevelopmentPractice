# 异常处理流程
def main(): # 主函数
    try:
        x = int(input('请输入第一个计算数字：')) # 键盘数据输入并转型
        y = int(input('请输入第二个计算数字：'))  # 键盘数据输入并转型
        result = x / y # 除法计算
        print('【除法计算】%s ÷ %s = %s' % (x, y, round(result, 2))) # 四舍五入保留2位小数
    except ZeroDivisionError as err: # 被除数为零
        print('【计算异常】%s' % err)
    except ValueError as err: # 数据转型错误
        print('【转换异常】%s' % err) # 异常输出
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数



#####################################

def main(): # 主函数
    try:
        x = int(input('请输入第一个计算数字：')) # 键盘数据输入并转型
        y = int(input('请输入第二个计算数字：'))  # 键盘数据输入并转型
        result = x / y # 除法计算
        print('【除法计算】%s ÷ %s = %s' % (x, y, round(result, 2))) # 四舍五入保留2位小数
    except ZeroDivisionError as err: # 被除数为零
        print('【计算异常】%s' % err)
    except ValueError as err: # 数据转型错误
        print('【转换异常】%s' % err) # 异常输出
    else: # 算是Python独创的结构
        print('程序没有异常，正确执行')
    finally: # 统一出口
        print('不管是否有异常， 都会执行该统一的操作出口')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 请输入第一个计算数字：2
# 请输入第二个计算数字：0
# 【计算异常】division by zero
# 不管是否有异常， 都会执行该统一的操作出口
# PS E:\summer_study\python开发\programe\pythonProject> 

#######################################
def main(): # 主函数
    try:
        x = int(input('请输入第一个计算数字：')) # 键盘数据输入并转型
        y = int(input('请输入第二个计算数字：'))  # 键盘数据输入并转型
        result = x / y # 除法计算
        print('【除法计算】%s ÷ %s = %s' % (x, y, round(result, 2))) # 四舍五入保留2位小数
    except Exception as err: # 被除数为零
        print('【计算异常】异常类型：%s、异常信息：%s' % (type(err), err))
    else: # 算是Python独创的结构
        print('程序没有异常，正确执行')
    finally: # 统一出口
        print('不管是否有异常， 都会执行该统一的操作出口')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数



# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 请输入第一个计算数字：2
# 请输入第二个计算数字：0
# 【计算异常】division by zero
# 不管是否有异常， 都会执行该统一的操作出口
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 请输入第一个计算数字：w
# 【计算异常】异常类型：<class 'ValueError'>、异常信息：invalid literal for int() with base 10: 'w'
# 不管是否有异常， 都会执行该统一的操作出口
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/异常捕获处理/Exception handling process.py"
# 请输入第一个计算数字：2
# 请输入第二个计算数字：0
# 【计算异常】division by zero
# 请输入第一个计算数字：6
# 请输入第二个计算数字：3
# 【除法计算】6 ÷ 3 = 2.0
# 程序没有异常，正确执行
# 不管是否有异常， 都会执行该统一的操作出口
# 请输入第一个计算数字：


