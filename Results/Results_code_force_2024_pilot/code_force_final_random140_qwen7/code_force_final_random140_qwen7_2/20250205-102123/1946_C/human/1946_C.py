import sys
 
class TreeNode:
 
    def __init__(self):
        self.edges = []
        self.children = []
        self.subtree_size = 1
        self.parent = None
    
    def __str__(self):
        return f"(edges: {self.edges}, children: {self.children}, subtree_size: {self.subtree_size}, parent: {self.parent})\n"
    
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
 
def check_x_dfs(tree: Tree, s: int, x: int) -> (int, int):
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
            # print(v, tree.vertices[v].good_components, tree.vertices[v].remaining_size)
    return (good_components[s], remaining_size[s])
 
def check_x_dfs_recursive(tree: Tree, v: int, x: int) -> (int, int):
    good_components = 0
    remaining_size = 1
 
    for u in tree.vertices[v].children:
        (good_components_subtree, remaining_size_subtree) = check_x_dfs_recursive(tree, u, x)
        good_components += good_components_subtree
        if remaining_size_subtree >= x:
            good_components += 1
        else:
            remaining_size += remaining_size_subtree
    print(v, good_components, remaining_size)
    return (good_components, remaining_size)
 
 
def check_x(tree: Tree, n: int, k: int, x: int) -> bool:
    # print("checking ", x)
    (good_components, remaining_size) = check_x_dfs(tree, 0, x)
    if good_components > k:
        return True
    if good_components == k and remaining_size >= x:
        return True
    return False
 
def find_x(tree: Tree, n: int, k: int) -> int:
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        if check_x(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
    return beg
 
def solve_case():
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        tree.add_edge(u-1, v-1)
    tree.root_tree_non_recursive(0, -1)
    print(find_x(tree, n, k))
 
if __name__ == '__main__':
    sys.setrecursionlimit(int(1e5)*2)
    t = int(input())
    while t > 0:
        t -= 1
        solve_case()