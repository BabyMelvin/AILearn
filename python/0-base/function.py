"""
函数形式   def 函数名和含参数圆括号
return 有：返回值。没有：返回None
global全局变量函数中可进行赋值
"""


# 定义介绍
def fib(n):
    """print fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a + b
    print()


def fib2(n):
    """return a list containing the Fibonacci"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# 默认参数值
def ask_ok(prompt, retries=4, complaint='Yes or no,please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


# ask_ok('Do you really want to quit?')
# ask_ok('Ok to override the file?', 2)
# ask_ok('Ok to override the file?', 2, 'Come on,only yes or no!')

# 默认值只被赋值一次
i = 5


def f(arg=i):
    print(arg)


i = 6
f()  # 值为5


# 当默认值是可变对象时有所不同，后续调用会累计
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))  # [1]
print(f(2))  # [1,2]
print(f(3))  # [1,2,3]


# 不想让默认值后续调用中累积
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


"""
    关键字参数
"""


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage,the", type)
    print("-- It's", state, "!")


# 关键字参数必须跟在位置参数后面，任何参数不可以多次赋值
parrot(1000)
parrot(voltage=1000)
parrot(voltage=100000, action='VOOOOM')
parrot(action='VOOOOOM', voltage=100000)
parrot('a million', 'bereft of list', 'jump')
parrot('a thousand', state='pushing up the daisies')
"""错误的情况"""
# parrot()                       required argument missing
# parrot(voltage=5.0, 'dead')    non-keyword argument after a keyword argument
# parrot(110, voltage=220)        duplicate value for the same argument
# parrot(actor='John Cleese')     unknown keyword argument
"""错误结束"""


# *name形式参数，接收一个元组。 **name参数时，接收一个字典
def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any,", kind, "?")
    print("-- I'm sorry,we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheese_shop("Limburger", "it's very ruuny,sir",
            "it's really very,VERY runny,sir",
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")
"""
    可变参数列表
"""


# 函数调用可变个数参数，参数被包装进一个元组,可以有零个到多个普通参数
def write_multiply_items(file, separator, *args):
    file.write(separator.join(args))


# 出现在*arg后的参数，只能作为关键字参数，不能为位置参数
def concat(*arg, sep='/'):
    return sep.join(arg)


concat("earth", "mars", "venus")
# 'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
# 'earth.mars.venus'

# 参数列表分拆,展开的意思
list(range(3, 6))
# [3,4,5]
args = [3, 6]
list(range(*args))
d = {"voltage": "four million", "state": "bleedin", "action": "VOOM"}
parrot(**d)

"""
lambda 形式 lambda a,b:a+b 计算a+b
"""


# 函数嵌套形式
def make_increment(n):
    return lambda x: x + n


# make_increment返回函数地址(lambda)
f = make_increment(42)
f(0)  # 42
f(1)  # 43

"""
    函数注解,用户自定义函数完全可选的
"""


# 注解形式存储在__annotations__属性中
# 参数注解在参数名称冒号后面，返回值注解->后面
def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("Annotations", f.__annotations__)
    print("Arguments", ham, eggs)


f("wonderful")
