import numpy as np
import matplotlib.pyplot as plt
from isort.profiles import plone
from matplotlib.lines import lineStyles
from scipy.ndimage import label

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

'''
https://blog.csdn.net/hesongzefairy/article/details/113527780
常用颜色
'b'          蓝色
'g'          绿色
'r'          红色
'c'          青色
'm'          品红
'y'          黄色
'k'          黑色
'w'          白色


常用标记点形状

‘.’：点(point marker)
‘,’：像素点(pixel marker)
‘o’：圆形(circle marker)
‘v’：朝下三角形(triangle_down marker)
‘^’：朝上三角形(triangle_up marker)
‘<‘：朝左三角形(triangle_left marker)
‘>’：朝右三角形(triangle_right marker)
‘1’：(tri_down marker)
‘2’：(tri_up marker)
‘3’：(tri_left marker)
‘4’：(tri_right marker)
‘s’：正方形(square marker)
‘p’：五边星(pentagon marker)
‘*’：星型(star marker)
‘h’：1号六角形(hexagon1 marker)
‘H’：2号六角形(hexagon2 marker)
‘+’：+号标记(plus marker)
‘x’：x号标记(x marker)
‘D’：菱形(diamond marker)
‘d’：小型菱形(thin_diamond marker)
‘|’：垂直线形(vline marker)
‘_’：水平线形(hline marker)

常用线形

‘-‘：实线(solid line style)
‘–-‘：虚线(dashed line style)
‘-.’：点划线(dash-dot line style)
‘:’：点线(dotted line style)
'''

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()

# show image
from matplotlib.image import imread
img = imread('chatgpt.jpg')
# plt.imshow(img)

plt.show()

