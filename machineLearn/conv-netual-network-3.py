import tensorflow as tf

"""
  TensorFlow支持加载格式(JPG,PNG),不同的空间(RGB,ARGB)
  通道：用一个包含每个通道中颜色数量的标量的秩1张量
  red=tf.constant([255,0,0])
"""
# 图像加载
# 图像加载和其他大型为进制文件相同，只是图内容需要解码

# match_filename_once接收一个正则表达式
