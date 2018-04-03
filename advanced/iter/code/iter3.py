def simple_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


if __name__ == '__main__':
    for i in simple_range(10):
        print(i)
