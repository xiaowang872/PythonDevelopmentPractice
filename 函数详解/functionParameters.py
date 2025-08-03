def message(book, author='李兴华'): # 信息的输出
    return f'【图书】名称：{book}、作者：{author}'
# 在参数上加一个“*”表示的是必须依据命名参数的方式来进行函数参数的传递
def message2(*, book, author='李兴华'): # 信息的输出
    return f'【图书2】名称：{book}、作者：{author}'


def avg(*numbers): # 可变参数
    # 可变参数指的用户可以根据需要向里面传递若干个参数的数据内容，但是数量不确定，类型为元组
    print('【可变参数】数据类型：%s' % type(numbers))
    result = float(sum(numbers)) # 元组数据的累加
    return result / len(numbers)
def skill(**kwargs): # KeyWord Args：命名参数
    for key, value in kwargs.items(): # 字典迭代
        print('【开发技术】编程技术：%s、配套图书：%s' % (key, value))
def message3(company, flag='MUYAN', *authors, **kwargs):
    # pass # 如果函数的内部没有任何的函数体，使用pass标记
    info = f'图书出版机构：{flag} - {company}\n'
    info += f'图书作者列表：{authors}\n'
    info += '机构已出版教材：\n'
    for key, value in kwargs.items():
        info += f'\t【图书】分类：{key}、名称：{value}\n'
    return info

def main(): # 定义一个主函数
    print(message(author='沐言科技', book='《Python开发实战》'))
    print(message('《Java程序设计开发实战》')) # 没有传递author参数
    # 错误的代码：print(message2('《Java程序设计开发实战》'))
    print(message2(book='《Java程序设计开发实战》')) # 没有传递author参数
    print(message2(author='沐言科技', book='《Java程序设计开发实战》')) 
    print('【数据计算】计算数据平均值：%5.2f' % avg(1, 2, 3))
    print('【数据计算】计算数据平均值：%5.2f' % avg(1, 2, 3, 6, 7, 8))
    skill(java='《Java程序设计开发实战》', python='《Python开发实战》', go='《GO开发实战》')
    print(message3('沐言科技', 'YOOTK', '李兴华', '马老师', '王老师',
                java='《Java程序设计开发实战》', python='《Python开发实战》'))

if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数




