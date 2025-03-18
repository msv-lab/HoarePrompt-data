#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer equal to 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) such that 1 ≤ u, v ≤ n, and the tree has exactly two leaves. There is a single integer u_1 (1 ≤ u_1 ≤ n) representing the initial node where the stone is placed.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is an integer equal to 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) such that 1 ≤ u, v ≤ n, and the tree has exactly two leaves. There is a single integer u_1 (1 ≤ u_1 ≤ n) representing the initial node where the stone is placed. `x` is an integer such that x ≥ 1, `y` is an integer read from the input. `lst` is a defaultdict with list as the default factory, where `lst[a]` contains all `b` values appended to its list for each pair (a, b) read during the loop iterations. `rev` is a defaultdict with list as the default factory, and `rev[b]` includes all `a` values appended to its list for each pair (a, b) read during the loop iterations.`
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: `tmp` is the last node visited (one of the leaves of the tree), and `one` is either `True` or `False` depending on whether the number of edges traversed is even or odd.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: `tmp` is the last element of the last non-empty list in the chain of `rev` lookups; `one` is either `True` or `False`; `two` is `False`.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function determines whether Hermione or Ron wins a game based on the parity of the path lengths from a starting node to the leaves of a tree. It reads the number of nodes, the edges forming the tree, and the starting node. It then calculates the path lengths from the starting node to both leaves and prints "Hermione" if both path lengths are of the same parity (both even or both odd), otherwise it prints "Ron".

