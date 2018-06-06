"""
    变量作用域
        L local局部作用域
        E enclosing 闭包函数外的函数中
        G global 全局作用域
        B built-in 内建作用域
    以L->E->G->B规则查找。局部找不到，会去局部外的局部栈（闭包），再去全局找，再去内建中找.
"""


# 1.python除了def/08-class/lambda外，其他如：/if/elif/else/except for/while并不能改变其作用域if elif else中定义，外部还是可以问访问的(和java不同)。
def hello():
    if True:
        a = 12
    b = "hello"
    print(a)  # 可访问的
    print(b)


hello()
# 局部变量外部无法访问
# print(b)  NameError: name 'b' is not defined

# 2.def/08-class/lambda内进行赋值，变成了其局部作用域.
# 局部作用域会覆盖全局作用域，但是不影响全局作用域
g = 1  # 全局的


def fun():
    g = 2  # 局部的
    return g


print(fun())  # 返回结果2
print(g)  # 返回结果1 ，局部不影响全局的，还是1

# 未被赋值之前引用错误。可使用global var 声明，但是全局的var会跟着改变
var = 1


def fun1():
    # UnboundLocalError: local variable 'var' referenced before assignment
    # print(var)
    var = 200


var2 = 1


def fun2():
    # UnboundLocalError: local variable 'var' referenced before assignment
    # var = var + 1
    return var


# 3.闭包Closure
"""
    闭包定义：
       如果一个内部函数里，对外部函数内(但不是全局作用域)的作用域引用。那么内部函数就被认为是闭包(closure)
"""
# 函数嵌套/闭包中的作用域
a = 1


def external():
    global a
    a = 200
    print(a)
    b = 100

    def internal():
        # 同样报错，相当于局部引用“全局”
        nonlocal b  # nonlocal解决这个问题
        print(b)
        b = 200
        return b


print(external())

# 不执行的时候，认为是局部变量为绑定错误
from functools import wraps


def wrapper(log):
    def external(F):
        @wraps(F)
        def internal(**kw):
            if False:
                # 当没有执行的时候，也会认为是没有赋值问题，尽量不要在闭包中修改变量
                # log = "modified"
                pass
            print(log)

        return internal

    return external


@wrapper('first')
def abc():
    pass


print(abc())

print("#" * 30)


# 用nonlocal解决这个问题
# 由于list具有可变性，而字符串是不可变类型
def counter(start):
    count = [start]

    def internal():
        count[0] += 1
        return count[0]

    return internal


count = counter(0)
for n in range(10):
    print(count())

print("#" * 30)
count = counter(0)
print(count())

# globals()和locals()
"""
    global()和关键字global是不同的，global关键字来声明一个局变量为全局变量。
        globals()和locals()提供了基于字典访问全局和局部变量的方式
"""


# 1. globals()
# 如果函数1中定义一个局部变量，名字和宁一个函数2相同，但又要在函数1内引用这个函数
def var():
    pass


def f2():
    var = "Just a String"
    f1 = globals()['var']
    print(var)
    return type(f1)


print(f2())


# just a string
# <type '07-function'>

# 2.如果使用Python的Web框架，把一个视图函数很多局部变量传递给引擎，然后作用在HTML上。
# 将locals()局部变量都打包一起扔出去

@app_route('/')
def view():
    user = User.query.all()
    article = Article.query.all()
    ip = request.environ.get('HTTP_X_RFAL_IP', request.remote_addr)
    s = 'Just a String'
    return render_template('index.html', user=user, article=article, ip=ip, s=s)
    # return render_template('index.html',**locals())
