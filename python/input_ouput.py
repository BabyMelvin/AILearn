# 格式化输出
# 标准模块 string
# 值转化为字符串
# str()用于值适用于人阅读的，repr()转为为供解释器读取形式
import math
import json

s = 'Hello ,world'
str(s)
print(str(s))
print('We are the {} who say {}!'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('this {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0},{1},and {other}'.format('Bill', 'Manfered', other='Gerog'))
print('The value of PI is approximately {}'.format(math.pi))
# ：格式化指令，对值深入控制。
print('The value of PI is approximately {0:.3f}'.format(math.pi))
# 旧试字符串
print('The value of PI is approxima;tely %5.3f' % math.pi)

"""
    文件读写
"""
# r 只读取文件
# w 只是写入文件 (同名文件将被删除)
# a 表示追加，写入任何添加到末尾
# r+ 读取文件和写入

f = open('workfile', 'r+')
# 读取文件
# size未指定，读取到结束，返回''文件末尾
f.read()
# 文件读取单独一行，字符串结尾自动添加一个换行符(\n)
f.readline()
# 可以循环遍历每一行
for line in f:
    print(line, end='')
# 所有行在同一个列表中
f.readlines()
f.write('This is a test\n')
# 当前指针位置
f.tell()
# 改变位置 seek(offset,from_what)
# from_what: 0->自文件开头，1->当前文件指针开始位置，2->文件末尾开始,省略->开头
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)
# 返回5
print(f.read(1))

f.seek(-3, 2)
print(f.read(1))
f.close()

with open('workfile', 'r') as f:
    read_data = f.read()

# close 状态
print(f.closed)

# jason 存储结构化数据
# read()返回字符串，用int()将'123'字符串转换成对应的数值123
# 标准模块json可以接受Python数据结构，将转化为字符串形式，序列化。
#              字符串表示重新构成数据结构反序化

print(json.dumps([1, 'simple', 'list']))
# 对象序列化到一个文件
# json.dump(x, f)
# 重新解码对象
# x = json.load(f)
