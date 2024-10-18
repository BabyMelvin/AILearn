import sys

"""
    打印文本信息
"""
print("文件名:", sys.getframe().f_code.co_filename)
print("当前函数:", sys.getframe().f_code.co_name)
print("当前行号:", sys.getframe().f_lineno)
