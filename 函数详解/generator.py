# def generator():
#     ids = ('yootk-{num:0>20}'.format(num=item)
#            for item in range(9999))  # 循环生成一个序列数据
#     return ids  # 返回生成的编号
# def main(): # 定义一个主函数
#     result = generator() # 保存生成结果
#     for item in result: # 数据循环
#         print('【ID】%s' % item) # 获取ID
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数


# ############################################
# def generator():
#     print('【yield生成器】yield数据返回之前。')
#     # yield作用实际上和return类似，但是它的返回是需要通过外部的next()函数调用后才可以触发的
#     param = yield 'yootk-000' # 必须先返回1次
#     print('【yield生成器】接收send()函数接收的参数，param = %s' % param)
#     yield f'yootk-{param}' # 返回send()函数的处理结果
# def main(): # 定义一个主函数
#     result = generator() # 保存生成结果
#     print('【主函数】调用next()函数：%s' % next(result))
#     print('【主函数】调用send()函数：%s' % result.send(128))
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数
#############################################
# 使用yield生成ID
# def generator(max_num):
#     for num in range(1, max_num): # 不是一次性生成
#         yield 'yootk-{num:0>20}'.format(num=num) # 返回yield生成的结果
# def main(): # 定义一个主函数
#     result = generator(3) # 保存生成结果
#     for item in result: # 直接迭代
#         print('【ID】%s' % item)
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数



# # 生成器委派
# def delegator(): # 委派生成器
#     yield from sub_generator() # 调用子生成器
# def sub_generator(): # 子生成器
#     data = yield # 等待send()传送数据
#     yield 'yootk-{num:0>20}'.format(num=data  * 2) # 返回生成的ID
# def main(): # 定义一个主函数
#     delegator_gen = delegator() # 获取委派生成器
#     next(delegator_gen) # 操作委派生成器
#     result = delegator_gen.send(15) # 向子生成器中发送数据
#     print(result)
# if __name__ == '__main__':  # Python程序运行起点
#     main() # 调用主函数

# 委派多个子生成器

def delegator(): # 委派生成器
    yield from sub_generator1() # 调用子生成器
    yield from sub_generator2() # 调用子生成器
def sub_generator1(): # 子生成器
    for item in range(5): # 生成数据：0 ~ 4
        yield item # 返回生成的结果
def sub_generator2(): # 子生成器
    for item in range(5, 10): # 生成数据：5 ~ 9
        yield item # 返回生成的结果
def main(): # 定义一个主函数
    delegator_gen = delegator() # 获取委派生成器
    for num in delegator_gen:
        print(num, end='、')
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数