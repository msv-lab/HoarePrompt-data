#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: After the loop executes all iterations, `x` must be greater than the total number of iterations (n), `a` and `b` will each be a series of input integers corresponding to the inputs provided during each iteration. The `lst` defaultdict will have keys as the `a` values and their corresponding values will be lists containing the `b` values from each iteration where `a` was the input. Similarly, the `rev` defaultdict will have keys as the `b` values and their corresponding values will be lists containing the `a` values from each iteration where `b` was the input.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: Output State: `z` is an input integer; `tmp` is equal to the last element of `lst[z]` after all elements have been popped from `lst[z]`, `one` is `False`, and `tmp` is now equal to the last element of `lst[tmp]` after all elements have been popped from `lst[tmp]`.
    #
    #This means that after the loop has executed all its iterations, `tmp` will be set to the last remaining element in the list it was pointing to, and `one` will be `False`. The loop continues until there are no more elements left in the list `lst[tmp]`.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: Output State: `z` is an input integer, `two` is `True`, `tmp` is the last element of `rev[tmp]` after all iterations of the loop have finished.
    #
    #Explanation: After the loop has executed all its iterations, the value of `two` will alternate between `True` and `False` based on the number of iterations. Since the loop continues until `rev[tmp]` is empty, the final state of `two` will be `True`. The variable `tmp` will be the last element of `rev[tmp]` after all elements have been popped from the list.
    print('Hermione' if two and one else 'Ron')
    #This is printed: 'Hermione' if one is True else 'Ron'
#Overall this is what the function does:The function reads a graph structure from standard input, where nodes are connected through edges. It then checks two paths from a given starting node, one following the original edges and the other following the reversed edges. Based on the alternation of visiting nodes in both paths, it determines whether to return 'Hermione' or 'Ron'.

