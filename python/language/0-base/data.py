
"""
数据类型: Number, String, List, Tuple, Set, Dictionary

Number: int, float, complex
String: str, "hello world"
List: list,[1,2,3]
Tuple: tuple, (1,2,3), (1,)
Set: set, {1,2,3}
Dictionary: dict, {'name': 'Alice', 'age': 25}


数据类型之间的转换: int(), float(), str(), list(), tuple(), set(), dict()

数据类型之间的比较: ==,!=, >, <, >=, <=

检查数据类型: isinstance()
检查实例：isinstance(obj, int)
返回数据类型：type(obj)

"""
# enumerate,迭代元素，并返回元素的索引
def enumerate_learn():
    elements = ('foo', 'bar', 'baz')
    for elem in elements:
        print(elem)

    for index, elem in enumerate(elements):
        print(index, elem)
        # 0 foo
        # 1 bar
        # 2 baz

    for index, elem in enumerate(elements, 10):
        print(index, elem)
        # 10 foo
        # 11 bar
        # 12 baz


"""
数据类型转换

1. str(X): 将对象转换为字符串
2. repr(X): 将对象转换为表达式字符串
3. eval(str): 计算字符串中表达式，并返回一个对象
4.frozenset(X):转换为不可变集合
5.chr(X): 将整数转换为字符
6.ord(X): 将字符转换为整数数值  

"""