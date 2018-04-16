import os
import sys


INDENT_STEP = '    '


def print_tree(root, indent=''):
    for line in _tree(root):
        print(line)


def _tree(root, indent=''):
    for entry in sorted(os.scandir(root), key=lambda e: e.name):
        line = f'{indent}{entry.name}'

        if entry.is_dir():
            yield line + '/'
            yield from _tree(entry.path, indent=indent + INDENT_STEP)
        else:
            yield line


if __name__ == '__main__':
    try:
        root = sys.argv[1]
    except IndexError:
        print(f'usage: {sys.argv[0]} PATH', file=sys.stderr)
        sys.exit(1)

    print_tree(root)
