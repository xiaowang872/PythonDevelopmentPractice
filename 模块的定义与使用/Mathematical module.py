
import math # 以后的代码都使用完整模块导入方式
def main(): # 主函数
    print('【阶乘计算】10! = %d' % math.factorial(10))
    print('【累加计算】1 + 2 + 3 + ... + 100 = %d' % math.fsum(range(1, 101)))
    print('【次方计算】10 * 10 * 10 = %d' % math.pow(10, 3))
    print('【次方计算】log2(10) = %d' % math.log2(10))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/模块的定义与使用/Mathematical module.py"
# 【阶乘计算】10! = 3628800
# 发/programe/pythonProject/模块的定义与使用/Mathematical module.py"
# 【阶乘计算】10! = 3628800
# 【累加计算】1 + 2 + 3 + ... + 100 = 5050      
# 【次方计算】10 * 10 * 10 = 1000
# 【次方计算】log2(10) = 3
# PS E:\summer_study\python开发\programe\pythonProject>

import cmath # 复数计算
def main(): # 主函数
    print(cmath.log(complex(10, 2), 2))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# (3.350219859070546+0.28478159528892355j)


