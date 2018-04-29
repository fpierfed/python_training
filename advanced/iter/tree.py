import argparse
import os


INDENT_STEP = '    '


def print_tree(root, exclude_dirs=None, indent=''):
    for line in _tree(root, exclude_dirs, indent):
        print(line)


def _tree(root, exclude_dirs=None, indent=''):
    if exclude_dirs is None:
        exclude_dirs = []

    # We handle exclude lists below. We always want to print the root dir
    # no matter what.
    yield f'{indent}{os.path.basename(root)}/'

    indent += INDENT_STEP
    for entry in sorted(os.scandir(root), key=lambda e: e.name):
        if entry.is_dir() and entry.name not in exclude_dirs:
            yield from _tree(entry.path, exclude_dirs, indent=indent)
        elif not entry.is_dir():
            yield f'{indent}{entry.name}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', default='.',
                        help='directory root')
    parser.add_argument('--exclude', action='append',
                        help='directories to skip')
    args = parser.parse_args()

    root = args.root

    # Handle . and ./ gracefully
    if root in ('.', './'):
        root = '.'
    else:
        root = os.path.abspath(root)

    print(args.exclude)
    print_tree(root, exclude_dirs=args.exclude)
