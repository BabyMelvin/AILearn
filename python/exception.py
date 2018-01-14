# 错误和异常
# 语法错误
# 异常
while True:
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("Oops!,That was no valid number.Try again ...")
    except(RuntimeError, TypeError, NameError):
        pass

import sys

try:
    f = open('myfirst.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error", sys.exc_info()[0])
    raise

# try ... except 可以带有else 语句
# 当try语句没有抛出异常时，需要执行一些代码
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close()

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    x, y = inst.args
    print('x=', x)
    print('y=', y)


# 抛出异常
# raise NameError("Hi,there")


# 自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print("My exception occurted,value", e.value)


class Error(Exception):
    """base class for exception in this module"""
    pass


class InputError(Error):
    """exception raised for errors in the input
        Attributes:
            previous --state at the beginning of transition
            nex -- attempted new state
            message -- explanation of what the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# 任何都会执行的句子
"""
try:
 raise KeyboardInterrupt
finally:
    print("Goodbye ,world")
"""


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("result is ", result)
    finally:
        print("executing finally clause")


divide(2, 0)
"""
    division by zero
    executing finally clause
"""
divide(2, 1)
"""
result is  2.0
executing finally clause
"""
