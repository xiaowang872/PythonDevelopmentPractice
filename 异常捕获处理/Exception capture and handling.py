# 异常的捕获和处理

class NetCalculator: # 网络计算器
    def connect(self): # 建立网络连接
        print('【网络计算】连接网络服务器，准备执行数学计算。')
        return True # 连接成功
    def division(self, x, y): # 除法计算
        if self.connect(): # 连接正确
            result = x / y # 数学计算
            self.close() # 关闭网络连接
            return result # 返回计算结果
        else: # 如果未连接
            return None # 此时不返回结果
    def close(self): # 关闭网络连接
        print('【网络计算】关闭网络服务器的连接。')
def main(): # 主函数
    calc = NetCalculator()# 网络计算器
    print('【除法计算】10 / 5 = %s' % calc.division(10, 5))
    print('-' * 50)
    print('【除法计算】10 / 0 = %s' % calc.division(10, 0))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/异常捕获处理/Exception capture and handling.py"
# 【网络计算】连接网络服务器，准备执行数学计算。
# 【网络计算】关闭网络服务器的连接。
# 【除法计算】10 / 5 = 2.0
# --------------------------------------------------
# 【网络计算】连接网络服务器，准备执行数学计算。
# Traceback (most recent call last):
#   File "e:\summer_study\python开发\programe\pythonProject\异常捕获处理\Exception capture and handling.py", line 22, in <module>
#     main() # 调用主函数
#     ^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\异常捕获处理\Exception capture and handling.py", line 20, in main
#     print('【除法计算】10 / 0 = %s' % calc.division(10, 0))
#                                 ^^^^^^^^^^^^^^^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\异常捕获处理\Exception capture and handling.py", line 9, in division
#     result = x / y # 数学计算
#              ~~^~~
# ZeroDivisionError: division by zero
###############################################################################
class NetCalculator: # 网络计算器
    def connect(self): # 建立网络连接
        print('【网络计算】连接网络服务器，准备执行数学计算。')
        return True # 连接成功
    def division(self, x, y): # 除法计算
        if self.connect(): # 连接正确
            result = x / y # 数学计算
            self.close() # 关闭网络连接
            return result # 返回计算结果
        else: # 如果未连接
            return None # 此时不返回结果
    def close(self): # 关闭网络连接
        print('【网络计算】关闭网络服务器的连接。')
def main(): # 主函数
    calc = NetCalculator()# 网络计算器
    print('【除法计算】10 / 5 = %s' % calc.division(10, 5))
    print('-' * 50)
    print('【除法计算】10 / 0 = %s' % calc.division(10, 0))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数



# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【网络计算】连接网络服务器，准备执行数学计算。
# 【网络计算】关闭网络服务器的连接。
# 【除法计算】10 / 5 = 2.0
# --------------------------------------------------
# 【网络计算】连接网络服务器，准备执行数学计算。
# Traceback (most recent call last):
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 20, in <module>
#     main() # 调用主函数
#     ^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 18, in main
#     print('【除法计算】10 / 0 = %s' % calc.division(10, 0))
#                                 ^^^^^^^^^^^^^^^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\tmp\abc.py", line 7, in division
#     result = x / y # 数学计算
#              ~~^~~
# ZeroDivisionError: division by zero


# try: # 捕获有可能产生的异常
# 	程序语句1
# 		...
# 	程序语句n
# [ except  [ 异常类型 [ as 对象] ] :
# 	异常处理程序语句
#   except  [ 异常类型 [ as 对象] ] :
# 	异常处理程序语句 ... ]
# [ else : 
# 	异常未出现时执行的程序语句 ]
# [ finally:
# 	异常的统一出口]


class NetCalculator: # 网络计算器
    def connect(self): # 建立网络连接
        print('【网络计算】连接网络服务器，准备执行数学计算。')
        return True # 连接成功
    def division(self, x, y): # 除法计算
        if self.connect(): # 连接正确
            try: # result变量只能够在异常处理中使用
                result = x / y # 数学计算
                return result # 返回当前的计算结果
            except ZeroDivisionError as err: # 除数为零
                print('【计算异常】%s' % err)
                return None # 如果产生异常，直接返回一个空数据
            finally: # 不管是否产生异常，都执行当前的代码
                self.close() # 关闭网络连接
        else: # 如果未连接
            return None # 此时不返回结果
    def close(self): # 关闭网络连接
        print('【网络计算】关闭网络服务器的连接。')
def main(): # 主函数
    calc = NetCalculator()# 网络计算器
    print('【除法计算】10 / 0 = %s' % calc.division(10, 0))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【网络计算】连接网络服务器，准备执行数学计算。
# 【计算异常】division by zero
# 【网络计算】关闭网络服务器的连接。
# 【除法计算】10 / 0 = None
