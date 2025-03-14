import numpy as np

# 创建一个一维数组
arr = np.array([1, 2, 3, 4, 5])

# 创建一个布尔数组，用于选择大于2的元素
mask = arr > 2

# 使用布尔数组进行索引
selected_elements = arr[mask]

print("原始数组:", arr)
print("布尔数组:", mask)
print("选择的元素:", selected_elements)

# 将素组内容设置为0
mask = arr == 2
arr[mask] = 0
print("修改后的数组:", arr)