

```python
%matplotlib inline
```

## 1.1 Numpy 数组对象

32位的Python等到int32的，64位得到int64

from pylab import *


```python
a=arange(5)
print(a.dtype)
print(a)
```

    int32
    [0 1 2 3 4]
    

32位python 返回int32，,64位Python返回int64


```python
a=array([1,2,4,5,6])
a.shape
```




    (5,)



一个包含5个元素的向量。shape属性返回一个元组。其中元组中元素个数表示向量维度，元素大小表示每一维上的大小。1维，第1维大小为5.

## 1.2 创建多维数组


```python
m=array([arange(3),arange(3)])
print("m=",m)
print('m.shape=',m.shape)
```

    m= [[0 1 2]
     [0 1 2]]
    m.shape= (2, 3)
    

创建一个2x3数组


```python
m=array([arange(3),arange(3),arange(3)])
print('m=',m)
print('m=',m.shape)
```

    m= [[0 1 2]
     [0 1 2]
     [0 1 2]]
    m= (3, 3)
    

创建一个3x3数组

### 1.2.1 选取数组元素


```python
a = array([[1,2],[3,4]])
print(a[0,0])
print(a[1,1])
```

    1
    4
    

|排|版|
|--|--|
|[0,0]|[0,1]|
|[1,0]|[1,1]|

### 1.2.2 Numpy数据类型
|类型|描述|
|--|--|
|bool|一位存储的布尔类型|
|inti|平台决定其精度整数（一般为int32或int64）|
|int8|-128-127|
|uint8|0-255|
|float64或float|双精度|
|complex64|复数,分别用两个32浮点表示实部和虚部|
|complex128或complex|分别用两个64浮点数表示实部和虚部|

类型转换:


```python
float64(42)
```




    42.0




```python
bool(42)
```




    True




```python
int0(42)  # 表示索引
```




    42




```python
array([0,1,2,3,4],dtype=uint16) #指定参数类型
```




    array([0, 1, 2, 3, 4], dtype=uint16)




```python
a=int0(42)
a.dtype.itemsize #占的字节数 8 表示64位
```




    8



### 1.2.3 自定义数据类型


```python
dtype(float)
```




    dtype('float64')




```python
dtype('f') # 字符编码来指定
```




    dtype('float32')




```python
# 创建一个长度为40字符串，32位整数，和32位单精度来记录商品
t=dtype([('name',str_,40),('numitem',int32),('price',float32)])
t
```




    dtype([('name', '<U40'), ('numitem', '<i4'), ('price', '<f4')])




```python
t['name'] #查看数据类型
```




    dtype('<U40')




```python
# array函数穿创建数组，没有指定参数，默认浮点。
#　创建自定义，必须指定参数类型，否则ＴypeError
itemz=array([('meaning of life DVD',42,3.14),('butter',13,2.72)],dtype=t)
print(itemz[1])
print("itemz.shape=",itemz.shape)

```

    ('butter', 13, 2.72)
    itemz.shape= (2,)
    

### 1.2.4 数组的切片


```python
a=arange(9) #(0,1,2,3,4,5,6,7,8)
a[3:7]      #      (3,4,5,6)
```




    array([3, 4, 5, 6])




```python
a[:2]
```




    array([0, 1])




```python
a[:7:2]  # 0-7步长为2
```




    array([0, 1])




```python
a[::-1]   #翻转数组
```




    array([8, 7, 6, 5, 4, 3, 2, 1, 0])



ndarray支持多维数组上切片操作。为了方便可以用省略号(...)来遍历剩下的维度


```python
b=arange(24).reshape(2,3,4)
print(b)
print(b.shape)
```

    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
    (2, 3, 4)
    


```python
print("b[0,0,0]=",b[0,0,0])
print("b[:,0,0]=",b[:,0,0])
print("b[0,:,:]=\n",b[0,:,:])
print("b[0,...]=\n",b[0,...])
print("b[...,1]=\n",b[...,1])

# ??? 结果有问题？
print("b[:,1]=\n",b[:1]) # 与print("b[...,1]=\n",b[...,1])类似 对下标省略
```

    b[0,0,0]= 0
    b[:,0,0]= [ 0 12]
    b[0,:,:]=
     [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    b[0,...]=
     [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    b[...,1]=
     [[ 1  5  9]
     [13 17 21]]
    b[:,1]=
     [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]]
    


```python
print("b[0,::-1,-1]=\n",b[0,::-1,-1])
print("b[::-1]=\n",b[::-1])
print("b[::-1,::-1,::-1]=\n",b[::-1,::-1,::-1])
```

    b[0,::-1,-1]=
     [11  7  3]
    b[::-1]=
     [[[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]
    
     [[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]]
    b[::-1,::-1,::-1]=
     [[[23 22 21 20]
      [19 18 17 16]
      [15 14 13 12]]
    
     [[11 10  9  8]
      [ 7  6  5  4]
      [ 3  2  1  0]]]
    

### 1.2.6改变数组维度


```python
# 1.ravel 函数完成展平操作
print("b.ravel=",b.ravel())
print("b=",b)
```

    b.ravel= [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
    a= [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
    b= [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
    


```python
# 2.flatten 展平，与ravel相同。但是flatten函数会请求分配内存保存结果
# 而ravel函数只是返回数组一个试图(view)
print("b.flatten",b.flatten())
print("b",b)
```

    b.flatten [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
    b [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
    


```python
# 3.用元素设置维度
b.shape=(6,4)
b
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15],
           [16, 17, 18, 19],
           [20, 21, 22, 23]])




```python
# 4.transpose 转置矩阵
b.transpose()
```




    array([[ 0,  4,  8, 12, 16, 20],
           [ 1,  5,  9, 13, 17, 21],
           [ 2,  6, 10, 14, 18, 22],
           [ 3,  7, 11, 15, 19, 23]])




```python
# resize和reshape功能类似，但是resize会直接改变所操作的数组
b.resize(2,12)
b # b本身已经被改变了 ！！！
```




    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
           [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]])



###  1.2.7 数组的组合
Numpy数组水平组合、垂直组合和深度组合等多种方式。
使用`vstack`,`dstack`,`hstack`,`column_stack`,`row_stack`和`concatenate`


```python
a=arange(9).reshape(3,3)
a
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
b=2*a
b
```




    array([[ 0,  2,  4],
           [ 6,  8, 10],
           [12, 14, 16]])




```python
# 1.水平组合
hstack((a,b))
```




    array([[ 0,  1,  2,  0,  2,  4],
           [ 3,  4,  5,  6,  8, 10],
           [ 6,  7,  8, 12, 14, 16]])




```python
# 用concatenate实现同样效果
concatenate((a,b),axis=1)
```




    array([[ 0,  1,  2,  0,  2,  4],
           [ 3,  4,  5,  6,  8, 10],
           [ 6,  7,  8, 12, 14, 16]])




```python
# 2.垂直组合
vstack((a,b))
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 0,  2,  4],
           [ 6,  8, 10],
           [12, 14, 16]])




```python
# concatenate实现同样效果
concatenate((a,b),axis=0)
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 0,  2,  4],
           [ 6,  8, 10],
           [12, 14, 16]])




```python
# 3.深度组合
dstack((a,b))
```




    array([[[ 0,  0],
            [ 1,  2],
            [ 2,  4]],
    
           [[ 3,  6],
            [ 4,  8],
            [ 5, 10]],
    
           [[ 6, 12],
            [ 7, 14],
            [ 8, 16]]])




```python
# 4.列组合 column_stack按列方向进行组合，对于一维数组可以按列方向组合
# 对于二维数组和hstack效果相同
oned=arange(2)
oned
```




    array([0, 1])




```python
twice_oned=2*oned
twice_oned
```




    array([0, 2])




```python
column_stack((oned,twice_oned))
```




    array([[0, 0],
           [1, 2]])




```python
# 5.行组合。row_stack,两个一维数组，可以直接叠加成一个二维数组
# 类似于vstack
row_stack((oned,twice_oned))
```




    array([[0, 1],
           [0, 2]])



### 1.2.9 数组的分割

Numpy数组可以进行水平、垂直或深度分割，相关函数有`hsplit`,`vsplit`,`dsplit`和`split`。分割成相同大小的子数组。


```python
# 1.水平分割
a=arange(9).reshape(3,3)
print(a)
print(hsplit(a,3))
```

    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    [array([[0],
           [3],
           [6]]), array([[1],
           [4],
           [7]]), array([[2],
           [5],
           [8]])]
    


```python
# split 中指定axis=1 水平分割
split(a,3,axis=1)
```




    [array([[0],
            [3],
            [6]]), array([[1],
            [4],
            [7]]), array([[2],
            [5],
            [8]])]




```python
#　２．垂直分割
vsplit(a,3)
```




    [array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]




```python
# 3.深度分割
c=arange(27).reshape(3,3,3)
c
```




    array([[[ 0,  1,  2],
            [ 3,  4,  5],
            [ 6,  7,  8]],
    
           [[ 9, 10, 11],
            [12, 13, 14],
            [15, 16, 17]],
    
           [[18, 19, 20],
            [21, 22, 23],
            [24, 25, 26]]])




```python
dsplit(c,3)
```




    [array([[[ 0],
             [ 3],
             [ 6]],
     
            [[ 9],
             [12],
             [15]],
     
            [[18],
             [21],
             [24]]]), array([[[ 1],
             [ 4],
             [ 7]],
     
            [[10],
             [13],
             [16]],
     
            [[19],
             [22],
             [25]]]), array([[[ 2],
             [ 5],
             [ 8]],
     
            [[11],
             [14],
             [17]],
     
            [[20],
             [23],
             [26]]])]



### 1.211 数组的属性

除了shape和dtype属性之外，ndarray还有很多属性


```python
# 1.ndim 属性,给出数组的维度，或数组轴的个数。
a
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
a.ndim
```




    2




```python
#２.size 属性 给出数组元素总个数
a.size
```




    9




```python
# 3.itemsize 给出元素在内存占的字节数
b.itemsize
```




    4




```python
# 4.nbytes数组所占存储空间，itemsize和size的成绩
a.nbytes
```




    36




```python
# 5.t属性效果和transpose函数一样
# 一维数组，T属性就是原数组
a.T
```




    array([[0, 3, 6],
           [1, 4, 7],
           [2, 5, 8]])




```python
# tolist函数将数组转换成列表
a.tolist()
```




    [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


