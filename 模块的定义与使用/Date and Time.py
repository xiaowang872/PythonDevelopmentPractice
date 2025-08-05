# 日期时间

import datetime # 只导入模块
def main(): # 主函数
    print('【日期】当前日期：%s' % datetime.datetime.today())
    print('【日期】数据格式化：%s' % datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    # 数字与时间之间是可以进行转换的，因此如果要计算两个日期时间之间的大小，是根据数字决定的
    print('【日期】数据时间戳：%s' % datetime.datetime.today().timestamp())
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/ 模块的定义与使用/Date and Time.py"
# 【日期】当前日期：2025-08-05 21:06:36.589180
# 【日期】数据格式化：2025-08-05 21:06:36
# 【日期】数据时间戳：1754399196.58918


import datetime # 只导入模块
def main(): # 主函数
    pattern = '%Y-%m-%d %H:%M:%S' # 大部分的项目到秒就可以了
    # 通过了一个自定义的日期时间数值创建了datetime.datetime对象
    dt = datetime.datetime(1978, 9, 15, 21, 15, 35, 123)
    print('【日期】数据格式化：%s' % dt.strftime(pattern))
    # 修改当前时间的小时的数值（120小时以前的日期时间）
    dt_a = dt + datetime.timedelta(hours=-120) # 小时计算
    print('【日期】120小时前的日期：%s' % dt_a.strftime(pattern))
    # 这个地方在进行计算的时候需要考虑到闰年的问题，所以不是简单的365天来实现的计算
    dt_b = dt + datetime.timedelta(days=3600, minutes=50) # 3600天零50分后的日期时间
    print('【日期】3600天50分钟后的日期：%s' % dt_b.strftime(pattern))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【日期】数据格式化：1978-09-15 21:15:35
# 【日期】120小时前的日期：1978-09-10 21:15:35
# 【日期】3600天50分钟后的日期：1988-07-24 22:05:35