import os
import sys


INDENT_STEP = '    '


def print_tree(root, indent=''):
    for line in _tree(root):
        print(line)


def _tree(root, indent=''):
    yield f'{indent}{os.path.basename(root)}/'

    indent += INDENT_STEP
    for entry in sorted(os.scandir(root), key=lambda e: e.name):
        line = f'{indent}{entry.name}'

        if entry.is_dir():
            yield from _tree(entry.path, indent=indent)
        else:
            yield line


if __name__ == '__main__':
    try:
        root = sys.argv[1]
    except IndexError:
        root = '.'

    # Handle . and ./ gracefully
    if root in ('.', './'):
        root = '.'
    else:
        root = os.path.abspath(root)

    print_tree(root)
