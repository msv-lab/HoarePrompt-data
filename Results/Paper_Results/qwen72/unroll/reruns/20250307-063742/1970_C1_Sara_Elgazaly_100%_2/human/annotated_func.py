#State of the program right berfore the function call: n is an integer such that 2 \leq n \leq 2\times 10^5, t is an integer and t=1, the edges of the tree are represented by n-1 pairs of integers (u, v) where 1 \leq u, v \leq n, and the starting node for the round is an integer 1 \leq u_1 \leq n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: The variable `t` remains 1, `lst` is a defaultdict with list as the default factory where each key `a` has a list of `x-1` appended values `b`, and `rev` is a defaultdict with list as the default factory where each key `b` has a list of `x-1` appended values `a`. The values of `n`, the edges of the tree, `u_1`, `x`, and `y` remain unchanged.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: `one` is `False` or `True` depending on the initial length of `lst[z]` being even or odd, `tmp` is the last element in the path traced by the loop, and `lst` and `rev` remain unchanged except for the elements popped from `lst[z]` and its subsequent elements.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: `one` remains unchanged, `tmp` is the last index of `rev` that has a non-empty list, `rev` remains unchanged except for the elements popped from `rev[tmp]` and its subsequent elements, `two` is `False` if the number of elements popped is odd, and `True` if the number of elements popped is even.
    print('Hermione' if two and one else 'Ron')
    #This is printed: - Since `one` remains unchanged and its value is not specified, we need to consider both possible values of `one` (True or False).
    #   - `two` is determined by the parity of the number of elements popped from `rev[tmp]` and its subsequent elements. Without the exact number of elements popped, we can't determine the exact value of `two`, but we know it will be either `True` or `False`.
    #
    #Given the lack of specific values for `one` and the exact number of elements popped to determine `two`, we need to consider all possible combinations:
    #
    #- If `one` is `True` and `two` is `True`, the output will be `'Hermione'`.
    #- If `one` is `True` and `two` is `False`, the output will be `'Ron'`.
    #- If `one` is `False` and `two` is `True`, the output will be `'Ron'`.
    #- If `one` is `False` and `two` is `False`, the output will be `'Ron'`.
    #
    #Since we don't have the exact values of `one` and `two`, we can only describe the output based on the possible conditions:
    #
    #Output:
#Overall this is what the function does:The function processes a tree structure represented by a set of edges and a starting node. It reads the number of nodes `x` and a value `y` from input, constructs adjacency lists `lst` and `rev` for the tree, and then performs two traversals starting from a given node `z`. The first traversal follows the forward edges, toggling a boolean `one` based on the parity of the path length. The second traversal follows the reverse edges, toggling a boolean `two` similarly. The function prints 'Hermione' if both `one` and `two` are `True` after the traversals, and 'Ron' otherwise. The function does not return any value.

