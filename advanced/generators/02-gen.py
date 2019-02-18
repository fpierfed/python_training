# 02-gen.py
# Other operations on generators:
#  - gen.close() thorw a GeneratorExit exception at the yield
#  - gen.throw(excls, exval, tb) thorw an exception at the yield


def gen():
    while True:
        try:
            yield
        except GeneratorExit as e:
            print(f'Got asked to quit: {e!r}')
            break                               # We HAVE to quit at this point
        except Exception as e:
            print(f'Got {e.__class__.__name__}({e!r})')


if __name__ == '__main__':
    g = gen()
    g.send(None)

    g.throw(IndexError, 'foo')
    g.close()
