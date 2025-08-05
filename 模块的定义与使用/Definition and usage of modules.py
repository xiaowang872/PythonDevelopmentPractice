# 模块的定义与使用

import com.yootk.message as msg # 配置引用别名
import com.yootk.data # 全名引用
def main(): # 主函数
    # msg.echo() = com.yootk.message.echo()，现在是通过别名引用的
    print(msg.echo('《Python开发实战》，李兴华')) # 通过别名调用
    print('【图书资源】%s' % com.yootk.data.RESOURCE) # 直接引用全局变量
    com.yootk.data.Press().publish(
        com.yootk.data.Book(name='Python开发实战', author='李兴华'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数



# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/模块的定义与使用/Definition and usage of modules.py"
# 【ECHO】《Python开发实战》，李兴华
# 【图书资源】资源下载：YOOTK - 沐言优拓
# 【图书】名称：Python开发实战、作者：李兴华


###############################################
from com.yootk.message import echo as message_echo # 只导入一个结构
from com.yootk.data import Book, Press # 导入模块指定结构
def main(): # 主函数
    print(message_echo('《Python开发实战》，李兴华')) # 通过别名调用
    Press().publish(Book(name='Python开发实战', author='李兴华'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/模块的定义与使用/Definition and usage of modules.py"
# 【ECHO】《Python开发实战》，李兴华
# 【图书】名称：Python开发实战、作者：李兴华


from com.yootk.message import * # 只导入一个结构
from com.yootk.data import * # 导入模块指定结构
def main(): # 主函数
    print(echo('《Python开发实战》，李兴华')) # 通过别名调用
    print('【图书资源】%s' % RESOURCE)  # 直接引用全局变量
    Press().publish(Book(name='Python开发实战', author='李兴华'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/模块的定义与使用/Definition and usage of modules.py"
# 【ECHO】《Python开发实战》，李兴华
# 【图书资源】资源下载：YOOTK - 沐言优拓
# 【图书】名称：Python开发实战、作者：李兴华



from com.yootk import * # 导入模块指定结构,这个导入的是父包
# from com.yootk.data import *
def main(): # 主函数
    print(message.echo('《Python开发实战》，李兴华')) # 通过别名调用
    Press().publish(Book(name='Python开发实战', author='李兴华'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/模块的定义与使用/Definition and usage of modules.py"
# 【ECHO】《Python开发实战》，李兴华
# Traceback (most recent call last):
#   File "e:\summer_study\python开发\programe\pythonProject\模块的定义与使用\Definition and usage of modules.py", line 59, in <module>
#     main() # 调用主函数
#     ^^^^^^
#   File "e:\summer_study\python开发\programe\pythonProject\模块的定义与使用\Definition and usage of modules.py", line 57, in main
#     Press().publish(Book(name='Python开发实战', author='李兴华'))
#     ^^^^^
# NameError: name 'Press' is not defined
# PS E:\summer_study\python开发\programe\pythonProject> 

from com.yootk import * # 导入模块指定结构,这个导入的是父包
from com.yootk.data import *
def main(): # 主函数
    print(message.echo('《Python开发实战》，李兴华')) # 通过别名调用
    Press().publish(Book(name='Python开发实战', author='李兴华'))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开 发/programe/pythonProject/模块的定义与使用/Definition and usage of modules.py"
# 【ECHO】《Python开发实战》，李兴华
# 【图书】名称：Python开发实战、作者：李兴华