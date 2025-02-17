import sys

"""
    打印文本信息
"""
print("文件名:", sys.getframe().f_code.co_filename)
print("当前函数:", sys.getframe().f_code.co_name)
print("当前行号:", sys.getframe().f_lineno)


# 列表
list1 = [1, 2, 3, 4, 5]

# 列表冒号切片
print(list1[1:3])  # [2, 3]

# 列表步长切片
print(list1[0:5:2])  # [1, 3, 5]

# 冒号： 用于定义分片、步长。
# 步长： 用于指定切片的步长，默认为1。
# 切片： 用于从列表中提取一部分元素。

# a[:n]表示从第0个元素到第n个元素(不包括n), a[1: ] 表示该列表中的第1个元素到最后一个元素。

# L[2] 读取列表中第三个元素，也即第2个元素
# L[-2] 读取列表中倒数第二个元素
# L[1:] 从第二个元素开始截取列表


# python创建二维数组:
list_2d = [ [0 for i in range(5)] for i in range(4)]