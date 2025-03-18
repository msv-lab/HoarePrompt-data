#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) of each round contains exactly one integer per round such that 1 ≤ u_i ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: x is an integer decreased by 1, y is an integer, n is an integer such that 2 ≤ n ≤ 2×10^5, t is 1, u and v are integers such that 1 ≤ u, v ≤ n, lst is a defaultdict where the key is an integer and the value is a list of integers representing the nodes connected to the key node, rev is a defaultdict where the key is an integer and the value is a list of integers representing the reverse connections (i.e., which nodes point to the key node).
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: The variable `tmp` will be set to the last element of the list corresponding to its current value in `lst`, or it will be set to `None` if the list is empty. The variable `one` will be toggled (flipped) with each iteration of the loop. All other variables (`x`, `y`, `n`, `t`, `u`, `v`, `lst`, `rev`, `z`, and `one`) will remain in their initial states.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: Output State: `two` is `False`, `tmp` is the last element of the list that was initially in `rev[tmp]`, and all other variables (`x`, `y`, `n`, `t`, `u`, `v`, `lst`, `rev`, `one`) remain in their initial states.
    #
    #Explanation: The loop continues to execute as long as `rev[tmp]` is not empty. Each iteration of the loop toggles the value of `two` (from `True` to `False` or vice versa) and removes the last element from the list `rev[tmp]`. This process continues until `rev[tmp]` becomes an empty list. At that point, the loop terminates. Since the loop starts with `two` being `True`, it will be `False` after the last iteration because the number of iterations is equal to the length of the list `rev[tmp]`, which is an odd number if the initial value of `two` was `True`. The variable `tmp` will hold the last element that was popped from `rev[tmp]`.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function processes a tree structure defined by a series of edges and checks two conditions related to traversing the tree in forward and backward directions. If both conditions are met (i.e., the traversal in both directions results in alternating nodes), it prints "Hermione"; otherwise, it prints "Ron". The function does not return any value but prints the result directly.

