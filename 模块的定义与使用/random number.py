# 随机数

import random # 随机数模块
def main(): # 主函数
    print('【随机数】', end='')
    for num in range(10): # 循环10次，生成10个随机数
        print('%d' % random.randint(1, 100), end='、') # 生成1 ~ 100之间的随机数
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/模块的定义与使用/random number.py"
# 【随机数】39、39、9、19、83、97、83、62、48、16、

import random # 随机数模块
def main(): # 主函数
    lotto = [] # 保存抽奖数据
    while len(lotto) != 7: # 如果选出的数字长度不足7个
        temp = random.randint(1, 36) # 随机生成数字
        if temp not in lotto: # 数值不存在
            lotto.append(temp)
    lotto.sort() # 列表排序
    print('我的彩票数据：%s' % lotto)
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 我的彩票数据：[7, 9, 10, 14, 15, 22, 32]