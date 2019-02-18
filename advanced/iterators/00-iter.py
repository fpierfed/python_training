# 00-iter.py
xs = [1, 2, 3, 4, 5, 6]
for x in xs:
    print(x)


# Is equivalent to
iterator = xs.__iter__()
iterator.__next__()
iterator.__next__()
iterator.__next__()
iterator.__next__()
iterator.__next__()
iterator.__next__()
iterator.__next__()             # <-- exception!
