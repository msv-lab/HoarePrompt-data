#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin


class Node(object):
    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def tree_insert(top, z):
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


def tree_find(node, key):
    if not node:
        return False
    if node.key == key:
        return True
    if key < node.key:
        return tree_find(node.left, key)
    return tree_find(node.right, key)


def inorder_walk(node):
    if node.left:
        inorder_walk(node.left)
    print('', node.key, end='')
    if node.right:
        inorder_walk(node.right)


def preorder_walk(node):
    print('', node.key, end='')
    if node.left:
        preorder_walk(node.left)
    if node.right:
        preorder_walk(node.right)


n = int(stdin.readline())
#assert n <= 500000

top = None
for _ in range(n):
    cmd = stdin.readline()
    if cmd.startswith('i'):
        key = int(cmd[7:])
        #assert -2000000000 <= key <= 2000000000
        top = tree_insert(top, Node(key))
    elif cmd.startswith('f'):
        key = int(cmd[5:])
        r = tree_find(top, key)
        print('yes' if r else 'no')
    else:
        inorder_walk(top)
        print()
        preorder_walk(top)
        print()