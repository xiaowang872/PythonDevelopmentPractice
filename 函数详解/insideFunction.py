def outer(msg): # 外部函数
    def prefix(): # 内部函数
        return '【ECHO】' # 此内容可能是代码生成的
    return prefix() + msg # 字符串连接

def accumulation(data): # 外部实现累加参数
    def factorial(num): # 内部实现阶乘操作
        if num == 1: # 递归的结束条件
            return 1 # 递归最后的返回结果
        return num * factorial(num - 1) # 阶乘计算
    if data == 1: # 递归结束判断
        return factorial(1)
    return factorial(data) + accumulation(data - 1)
def add(num_a): # 加法计算
    def inner_add(num_b): # 内部函数
        return num_a + num_b # 加法操作
    return inner_add # 返回内部函数的引用






def main(): # 定义一个主函数
    print(outer('李兴华，《Python开发实战》'))
    print('【阶乘累加计算】15! = {:^30,}'.format(accumulation(15)))
    print("#############闭包################")
        # outer其实就代表了此时的num_a的参数内容，固定为10
    outer2 = add(10) # 获取函数的引用
    print('【数据计算】10 + 20 = %d' % outer2(20))
    print('【数据计算】10 + 50 = %d' % outer2(50))










if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数
