import fibo  # 同目录下，忽略提醒

# 模块名就是文件名都掉.py
# 命令行执行时候__name__ = __main__
print(__name__)
fibo.fib(12)
print(fibo.__name__)
fib = fibo.fib
fib(500)
# 1 1 2 3 5 8 fibo.py----: fibo
# fibo

# python 以模块划分，无需担心全局文件冲突 modname.itemname

from fibo import fib, fib2

fib(300)

# 导入除了_开头命名模块 ,交互式，避免重启解释器，import imp;imp.reload(moduulename)
from fibo import *

fib(300)

# python fibo.py <arg>
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))

"""
    模块搜索路径
    导入spam模块，解释器在当前目录搜索spam.py。没有的去sys.path找。
    sys.paty变量初始值来自:
        1.输入脚本目录(当前目录)
        2.环境变量PYTHONPATH目录
        3.Python默认安装路径中搜索
"""
import sys

print(sys.path)

"""
    ”编译的“Python文件
        加快加载模块的速度会在__pycache__目录下module.version.pyc名字缓存
        
"""

"""
    标准模块
        一些标准模块内置解释器之中。sys模块内置所有的Python解释器
"""
# 修改搜索路径
import sys

sys.path.append('/ufs/guido/lib/python')

# dir()函数
# 按模块名搜索模块定义
import fibo, sys

print(dir(fibo))

"""
    包：通常是使用原点模块名，结构化模块命名空间。
        A.B模块表示：A包中B的子模块
        包定义可以避免模块名的冲突，模块避免全变量之间的冲突
       为了让PYthon将目录当作内容的包，目录必须含有__init__.py文件，避免含有有些目录含有搜索中出出现有效模块
         __init__.py文件可以为空
                    也可以执行包的初始化代码
                    或者__all__变量
         
"""
# 导入 sound.effects.echo子模块
import sound.effests.echo
# 可选择的方式导入echo子模块
from sound.effects import echo
echo.echofilter()
from sound.effects.echo import echofilter
# import item.subitem.susubitem这样语句，子项必须是包

# 从* 导入包,可能花掉很长时间
from sound.effects import *　
#解决办法
# __init__.py代码中定义一个名为__all__列表，按照列表给的导入
# import *不想全导入
# sound/effects/__init__.py
# __all__=["echo","reverse"]

"""
    包内引用
        按绝对位置导入子模块,python主模块总是导入绝对路径
        也可以用相对位置导入包
"""
# 在 surround模块中可以
from . import echo
from .. import formats
from ..filter import equalizer


