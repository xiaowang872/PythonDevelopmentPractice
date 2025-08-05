# 多进程编程简介

import multiprocessing # 导入多进程的开发模块
def main(): # 主函数
    print('CPU内核数量：%s' % multiprocessing.cpu_count()) # 获取CPU的内核数量
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/多进程编程/brief introduction.py"
# CPU内核数量：20


