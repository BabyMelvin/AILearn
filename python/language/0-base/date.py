# enumerate,迭代元素，并返回元素的索引

def enumertate_learn():
    elements = ('foo', 'bar', 'baz')
    for elem in elements:
        print(elem)

    for index, elem in enumerate(elements):
        print(index, elem)
        # 0 foo
        # 1 bar
        # 2 baz

    for index, elem in enumerate(elements, 10):
        print(index, elem)
        # 10 foo
        # 11 bar
        # 12 baz
