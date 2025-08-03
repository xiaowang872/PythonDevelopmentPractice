


def main(): # 定义一个主函数
    # 格式：lambda 参数列表 : 程序语句
    operate = lambda x, y : x + y # 两个数字相加
    print('【加法计算】10 + 20 = %d' % operate(10, 20))
    add = lambda *args: sum(args) # 数据求和
    print('【累加计算】1 + 2 + 3 + 4 + 5 + 6 = %d' % add(1, 2, 3, 4, 5, 6))
    factorial = lambda num: 1 if num == 1 else num * factorial(num - 1)
    accumulation = lambda num : 1 if num == 1 else factorial(num) + accumulation(num - 1)
    print('【阶乘计算】3! + 2! + 1! = %d' % accumulation(3))
    numbers = [9, 8, 2, 1, 6, 3, 5, 7] # 数据无序存储
    sort_result = sorted(numbers, key=lambda x: x) # 每次获取一个数据排序
    print('【数据排序】%s' % sort_result)
    even_result = list(filter(lambda x: x % 2 == 0, numbers)) # 可以被2整除的为偶数
    print('【数据过滤】%s' % even_result)
    double_result = list(map(lambda x: x * 2, numbers))
    print('【数据翻倍】%s' % double_result)
    print('##################')
    # 我们模拟一个编程热度的TOP-N榜首，有一个排名
    access = dict(java=10, python=50, go=3, sql=7, html=20)
    sort_result = sorted(access.items(), key=lambda x: -x[1]) # 降序排列
    print('【字典排序】%s' % sort_result)





if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

