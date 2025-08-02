numbers = [1, 2, 3, 4, 5, 6, 7, 1, 87, 8, 6,
            8, 89, 990, 0, 0, 00, 4, 34, 312, 12, 23, 3, 3] # 定义一个数字列表
print('序列元素个数：', len(numbers))
print('序列数据求和：', sum(numbers))
print('序列的最大值：', max(numbers))
print('序列的最小值：', min(numbers))

# 重复数据内容统计
import collections # 引入一个第三方开发库
numbers = [1, 2, 3, 4, 5, 6, 7, 1, 87, 8, 6,
            8, 89, 990, 0, 0, 00, 4, 34, 312, 12, 23, 3, 3] # 定义一个数字列表
print(collections.Counter(numbers))
numbers_new = collections.Counter(numbers).keys() # 没有重复的数字
print('序列元素个数：', len(numbers_new))
print('序列数据求和：', sum(numbers_new))
print('序列的最大值：', max(numbers_new))
print('序列的最小值：', min(numbers_new))
# 字典数据统计
numbers = dict(one=1, two=2, three=3)  # 字典集合
vals = numbers.values() # 获取字典中的全部数据
print('字典内容的求和计算：', sum(vals))
print('字典内容是否完整：', all(vals))
numbers.update({'four': None}) # 向字典中追加数据
print('字典内容是否完整：', all(numbers.values())) # 此时数据中包含有None