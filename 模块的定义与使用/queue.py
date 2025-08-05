# 队列
import collections # 导入集合
def main(): # 主函数
    info = collections.deque() # 创建队列实例
    info.append('python') # 添加队列数据
    info.appendleft('java') # 添加数据
    info.appendleft('C++') # 添加队列数据
    print('【队列】保存数据长度：%s' % len(info))
    print('【队列】保存数据：%s' % info)
    print('【队列】从队首（右端）弹出数据：%s' % info.pop())
    print('【队列】从队尾（左端）弹出数据：%s' % info.popleft())
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数



# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/模块的定义与使用/queue.py
# 【队列】保存数据长度：3
# 【队列】保存数据：deque(['C++', 'java', 'python'])
# 【队列】从队首（右端）弹出数据：python
# 【队列】从队尾（左端）弹出数据：C++
# PS E:\summer_study\python开发\programe\pythonProject>
