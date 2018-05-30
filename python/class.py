# 命名空间和作用域
"""
    命名空间
        命名到对象的映射。通过字典实现的。
    模块的属性和全局命名有直接的映射关系：共享同一个命名空间
        属性是可以读写的。
            modulename.the_answer=42
            del modlename.the_answer 删除该属性
    python特别：
           如果没有使用global语法，赋值操作总是在最里层的作用域
        赋值不会复制数据，只是将命名绑定到对象，删除也是如此.
            引入新命名的操作都作用于局部作用域。
        import语句和函数定义将模块名或函数绑定局部作用据
            可以使用global语句将变量引入到全局作用域
        global语句用以将指明特定的变量为全局作用域，并重新绑定它。
        nonlocal语句用以指明某个变量为封闭作用域，并重新绑定它。
"""


# global 和 nonlocal
def scope_test():
    def do_local():
        # local无法个改变spam绑定.spam=test spam
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        # nonlocal赋值改变了spam绑定scope_test
        spam = "nonlocal spam"

    def do_gloabl():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("after local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_gloabl()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
"""
after local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
"""


# 类
class MyClass:
    """a simple example 08-class"""
    i = 12345

    def __init__(self):
        self.data = []

    def f(self):
        return "hello world"

    def __str__(self):
        return "hi"


x = MyClass()
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
# X.F和MyClass.f不同，是一个方法对象，不是一个函数对象
# x.f()
print(x.f())
"""
xf = x.f
while True:
    print(xf())
"""


# 类和实例变量
# 实例变量用于每一个实例嗾使唯一的数据,类变量用于类的所有实例共享的属性和方法
class Dog:
    # 08-class variant,shared by all instances
    tricks = []
    kind = 'canine'

    def __init__(self, name):
        self.name = name

    def add_trick(self, tricks):
        self.tricks.append(tricks)


d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
Dog.kind = 'hhhhhh'
print(d.name)
print(e.name)
d.kind = 'SHE'
print(e.kind)


# 类名直接调用有效

# 继承
class DerivedClassName(Exception):
    pass


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr")


class Dog(Animal):
    def bark(self):
        print("Worf")


fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()


# Magic method
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.x)

    def __floordiv__(self, other):
        return Vector2D(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Vector2D(self.x % other.x, self.y % other.y)

    def __pow__(self, power, modulo=None):
        return Vector2D(self.x ** power, self.y ** power)

    def __and__(self, other):
        return Vector2D(self.x & other.x, self.y & other.y)

    def __or__(self, other):
        return Vector2D(self.x | other.x, self.y | other.y)

    def __xor__(self, other):
        return Vector2D(self.x ^ other.x, self.y ^ other.y)

    def __lt__(self, other) -> "<":
        pass

    def __le__(self, other) -> "<=":
        pass

    def __getitem__(self, item) -> "get indexing":
        pass

    def __contains__(self, item) -> "for in":
        pass


# 声明周期
# 1.定义属于哪个类
# 2.实例化对象，__init__
# 3.在内存分配之前调用__new__方法

# 私有数据
# 弱的申明
# 单个下划线开头，只是说明，其他外部能够调用.只用在模块导入时import module_name import *有效

class Queue:
    def __int__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


# 强申明，双下划线。 不能被外部类获取
class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg()
print(s._Spam__egg)


# 下面错误申明，不能获取
# print(s.__egg)

# 类方法声明
# 由类调用，并且传递类参数
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())


# 静态方法
# 静态方法和类方法类似，除了不接受额外参数。想普通方法属于类的。
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineaple":
            raise ValueError("No pineapppls")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)


# 属性 控制用户定制实例特性
# 是某个属性成只读的
class Pizza0:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza0(["Cheese", "tomato"])
print(pizza.pineapple_allowed)


# 属性被设为只读,不能改变
# pizza.pineapple_allowed=True

# 属性可以根据下面的方法进行设置
# setter/getter
class Pizza1:
    def __init__(self, topping):
        self.topping = topping
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password!")
            if password == "SwOrdf1sh":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert intruder!")


pizza = Pizza1(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)


# python 所有方法本质上是虚方法
# isinstance()检查实例类型：isinstance(obj,int)只有在obj.__class__是int或其他从int继承的类型
# issubclass()用于检查是否是子类

# 多继承
class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class DerivedClassName1(Base1, Base2, Base3):
    pass
