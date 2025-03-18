#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, and the tree is represented by a list of n-1 edges, where each edge is a tuple of two integers (u, v) such that 1 ≤ u, v ≤ n. The tree has exactly two leaves. The starting node u_1 is an integer such that 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: After the loop executes all the iterations, `lst` will contain `x-1` new entries where each key `a` will have a list of values `b` that were appended during the loop. Similarly, `rev` will contain `x-1` new entries where each key `b` will have a list of values `a` that were appended during the loop. The values of `n`, `u_1`, and `y` remain unchanged.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: `lst` will have the same structure as the initial state, but the lists associated with the keys that were traversed will be empty. `rev` remains unchanged. `n`, `u_1`, and `y` remain unchanged. `z` remains unchanged. `tmp` will be the last key in the traversal chain that has an empty list. `one` will be `False` if the number of iterations is odd, and `True` if the number of iterations is even.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: `lst` remains unchanged, `rev` remains unchanged, `n` remains unchanged, `u_1` remains unchanged, `y` remains unchanged, `z` remains unchanged, `tmp` is equal to `z`, `one` is `True` if the number of iterations is even, and `False` if the number of iterations is odd, `two` is `False`.
    print('Hermione' if two and one else 'Ron')
    #This is printed: - Since the condition `two and one` is `False`, the else part of the conditional expression will be executed.
    #   - The else part is `'Ron'`.
    #
    #Output:
#Overall this is what the function does:The function `func` reads an integer `x` and an integer `z` from the input, and a list of `x-1` edges representing a tree with exactly two leaves. It then traverses the tree from node `z` in two different directions using the adjacency lists `lst` and `rev`. After the traversals, it prints 'Ron' if the number of steps in both traversals is odd, and 'Hermione' otherwise. The function does not return any value. The state of the program after the function concludes is that the adjacency lists `lst` and `rev` may have been modified (with some lists being emptied), but the original input values `x` and `z` remain unchanged.

