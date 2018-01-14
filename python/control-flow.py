# if elif "no" switch
x = int(input("please input a number:"))
if x < 0:
    print('negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')

# for

words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

for i in range(5):
    print(i)

a = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

"""
    break continue else(loop):flase or loop end execute
"""
# break else
print(list(range(2, 2)))
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break  # not to else
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# pass,continue
def initlog(*arg):
    pass


class MyEmptyClass:
    pass


# while True:
#    pass

for num in range(2, 10):
    if num % 2 == 0:
        print("found an even number", num)
        continue
    print("find a number", num)
