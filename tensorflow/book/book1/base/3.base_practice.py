import tensorflow as tf

"""
    tensorboard 中张量流动中：
        [None]代表任意一个长度的向量
        []    代表一个标量
"""

# 显示的Graph
graph = tf.Graph()

# 将graph对象作为默认
with graph.as_default():
    with tf.name_scope("variables"):
        # 计算运行次数
        global_step = tf.Variable(0, dtype=tf.int32, trainable=False, name="global_step")
        # 计算累加和
        total_output = tf.Variable(0.0, dtype=tf.float32, trainable=False, name="total_output")
    with tf.name_scope("transformation"):
        # 独立输入层
        with tf.name_scope("input"):
            a = tf.placeholder(tf.float32, shape=[None], name="input_placeholder_a")
        # 独立中间层
        with tf.name_scope("intermediate_layer"):
            b = tf.reduce_prod(a, name="product_b")
            c = tf.reduce_sum(a, name="sum_c")
        # 独立输出层
        with tf.name_scope("output"):
            output = tf.add(b, c, name="output")
    with tf.name_scope("update"):
        # 更新输出total_out
        update_total = total_output.assign_add(output)
        increment_step = global_step.assign_add(1)
    # 数据汇总
    with tf.name_scope("summaries"):
        avg = tf.div(update_total, tf.cast(increment_step, tf.float32), name="average")
        # 为输出节点创建汇总数据
        #tf.summary.scalar(b'Output', output, name="out_put_summary")
        #tf.summary.scalar(b'sum of output over time', update_total, name="total_summary")
        #tf.summary.scalar(b'Average of outputs over time', avg, name="average_summary")
        tf.summary.scalar('Output 10', output)
        tf.summary.scalar('sum of output over time 10', update_total)
        tf.summary.scalar('Average of outputs over time 10', avg)
    with tf.name_scope("global_ops"):
        init = tf.global_variables_initializer()
        merged_summaries = tf.summary.merge_all()

sess = tf.Session(graph=graph)
writer = tf.summary.FileWriter("C:\\Users\\dell\\PycharmProjects\\tensorflow\\improved_graph", graph)
sess.run(init)


def run_graph(input_tensor):
    feed_dict = {a: input_tensor}
    # “_”表示对output值存储,不关心
    _, step, summary = sess.run([output, increment_step, merged_summaries], feed_dict=feed_dict)
    # step 横轴
    writer.add_summary(summary, global_step=step)


run_graph([2, 8])
run_graph([3, 1, 3, 3])
run_graph([8])
run_graph([1, 2, 3])
run_graph([11, 4])
run_graph([4, 1])
run_graph([7, 3, 1])
run_graph([6, 3])
run_graph([0, 2])
run_graph([4, 5, 6])

writer.flush()
writer.close()
sess.close()
