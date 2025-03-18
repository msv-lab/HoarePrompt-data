import sys

class TreeNode:

    def __init__(self):
        self.edges = []
        self.children = []
        self.subtree_size = 1
        self.parent = None

    def __str__(self):
        return f'(edges: {self.edges}, children: {self.children}, subtree_size: {self.subtree_size}, parent: {self.parent})\n'

    def __repr__(self):
        return self.__str__()
class Tree:

    def __init__(self, n):
        self.vertices = [TreeNode() for _ in range(n)]

    def add_edge(self, u: int, v: int) -> None:
        self.vertices[u].edges.append(v)
        self.vertices[v].edges.append(u)

    def root_tree(self, v: int, root: int) -> None:
        self.vertices[v].parent = root
        for u in self.vertices[v].edges:
            if u != root:
                self.vertices[v].children.append(u)
                self.root_tree(u, v)
                self.vertices[v].subtree_size += self.vertices[u].subtree_size

    def root_tree_non_recursive(self, v: int, root: int) -> None:
        stack = [(v, root)]
        while stack:
            (v, root) = stack.pop()
            self.vertices[v].parent = root
            for u in self.vertices[v].edges:
                if u != root:
                    self.vertices[v].children.append(u)
                    stack.append((u, v))
                    self.vertices[v].subtree_size += self.vertices[u].subtree_size

    def __str__(self):
        return str(self.vertices)
if __name__ == '__main__':
    sys.setrecursionlimit(int(100000.0) * 2)
    t = int(input())
    while t > 0:
        t -= 1
        func_5()

def func_1(tree: Tree, s: int, x: int) -> (int, int):
    stack = [(s, False)]
    good_components = {}
    remaining_size = {}
    while stack:
        (v, postorder) = stack.pop()
        if not postorder:
            stack.append((v, True))
            good_components[v] = 0
            remaining_size[v] = 1
            for u in tree.vertices[v].children:
                stack.append((u, False))
        elif postorder:
            for u in tree.vertices[v].children:
                good_components[v] += good_components[u]
                if remaining_size[u] >= x:
                    good_components[v] += 1
                else:
                    remaining_size[v] += remaining_size[u]
    return (good_components[s], remaining_size[s])

def func_2(tree: Tree, v: int, x: int) -> (int, int):
    good_components = 0
    remaining_size = 1
    for u in tree.vertices[v].children:
        (good_components_subtree, remaining_size_subtree) = func_2(tree, u, x)
        good_components += good_components_subtree
        if remaining_size_subtree >= x:
            good_components += 1
        else:
            remaining_size += remaining_size_subtree
    print(v, good_components, remaining_size)
    return (good_components, remaining_size)

def func_3(tree: Tree, n: int, k: int, x: int) -> bool:
    (good_components, remaining_size) = func_1(tree, 0, x)
    if good_components > k:
        return True
    if good_components == k and remaining_size >= x:
        return True
    return False

def func_4(tree: Tree, n: int, k: int) -> int:
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
    return beg

def func_5():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        tree.add_edge(u - 1, v - 1)
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))

