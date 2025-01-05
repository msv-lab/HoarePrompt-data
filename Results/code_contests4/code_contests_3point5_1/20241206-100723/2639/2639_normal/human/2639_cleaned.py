class Node(object):

    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def func_1(top, z):
    y = None
    x = top
    while isinstance(x, Node):
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is None:
        top = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return top

def func_2(node, key):
    if not node:
        return False
    if node.key == key:
        return True
    if key < node.key:
        return func_2(node.left, key)
    return func_2(node.right, key)

def func_3(node):
    if node.left:
        func_3(node.left)
    print('', node.key, end='')
    if node.right:
        func_3(node.right)

def func_4(node):
    print('', node.key, end='')
    if node.left:
        func_4(node.left)
    if node.right:
        func_4(node.right)
n = int(stdin.readline())
top = None
for _ in range(n):
    cmd = stdin.readline()
    if cmd.startswith('i'):
        key = int(cmd[7:])
        top = func_1(top, Node(key))
    elif cmd.startswith('f'):
        key = int(cmd[5:])
        r = func_2(top, key)
        print('yes' if r else 'no')
    else:
        func_3(top)
        print()
        func_4(top)
        print()