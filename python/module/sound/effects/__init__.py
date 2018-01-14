# 指定import * 导入模块
__all__ = ["echo", "reverse"]
# 可以明确导入,echo 和surround导入到当前命名空间
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
