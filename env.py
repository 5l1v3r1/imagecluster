import sys

for name in sys.path:
    if 'python2' in name:
        sys.path.pop(sys.path.index(name))
