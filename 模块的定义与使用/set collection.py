# set 集合（不保存重复数据）
def main(): # 主函数
    list = ['java', 'java', 'python', 'python', 'python'] # 定义List集合
    # Python内部提供了set()函数，来创建Set集合
    skill = set(list) # 定义Set集合
    skill.add('c++') # 添加数据项
    print(skill)
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe "e:/summer_study/python开发/programe/pythonProject/模块的定义与使用/set collection.py"
# {'c++', 'python', 'java'}

def main(): # 主函数
    muyan_skill = set(['java', 'python']) # 定义Set集合
    yootk_skill = set(['java', 'c++', 'go']) # 定义Set集合
    print('【交集运算】计算一：%s、计算二：%s' %
          (muyan_skill.intersection(yootk_skill), muyan_skill & yootk_skill))
    print('【差集运算】计算一：%s、计算二：%s' %
          (muyan_skill.difference(yootk_skill), muyan_skill - yootk_skill))
    print('【对称差集】计算一：%s、计算二：%s' %
          (muyan_skill.symmetric_difference(yootk_skill), muyan_skill ^ yootk_skill))
    print('【并集差集】计算一：%s、计算二：%s' %
          (muyan_skill.union(yootk_skill), muyan_skill | yootk_skill))
if __name__ == '__main__':  # Python程序运行起点
    main() # 调用主函数


# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/tmp/abc.py
# 【交集运算】计算一：{'java'}、计算二：{'java'}
# 【差集运算】计算一：{'python'}、计算二：{'python'}
# 【对称差集】计算一：{'c++', 'python', 'go'}、计算二：{'c++', 'python', 'go'}
# 【并集差集】计算一：{'java', 'go', 'c++', 'python'}、计算二：{'java', 'go', 'c++', 'python'}
# PS E:\summer_study\python开发\programe\pythonProject>