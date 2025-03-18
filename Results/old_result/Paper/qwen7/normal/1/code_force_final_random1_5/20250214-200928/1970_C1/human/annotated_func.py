#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer such that 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: After the loop executes all its iterations, `x` will be 0, `a` and `b` will no longer be defined within the loop context, `rev[b]` will contain a list of all integers `a` such that there is an edge from `a` to `b` in the graph, and `lst[a]` will contain a list of all integers `b` such that there is an edge from `a` to `b` in the graph.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: Output State: `z` is an input integer, `tmp` is now the last element of the list obtained by repeatedly popping the last element from `lst[z]` until the list is empty, `x` is 0, and `one` is False.
    #
    #This means that after the loop has executed all its iterations, `tmp` will be set to the final value obtained by successively popping the last element from the nested lists starting from `lst[z]` until the innermost list is empty. The variable `x` remains 0 as it is not affected by the loop, and `one` becomes False after the last iteration of the loop.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: Output State: `z` is an input integer, `tmp` is equal to `rev[rev[rev[z].pop().pop()].pop()].pop()`, `x` is 0, `one` is False, `two` is True.
    #
    #Explanation: The loop continues to pop elements from the list `rev[tmp]` until it becomes empty. Based on the pattern observed, after each iteration, `tmp` is updated to the popped value from the previous `tmp`. After the loop has executed all its iterations, `tmp` will be the last element popped from the nested structure defined by the `rev` dictionary, with `two` alternating between True and False as described.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function processes a graph represented as an adjacency list and determines whether a specific path exists based on the parity of traversing both the original and reversed graph. It reads the graph structure from standard input, then checks if the path from the starting node (determined by the first input) alternates between even and odd steps when traversed in both forward and reverse directions. If the path alternates correctly in both directions, it prints "Hermione"; otherwise, it prints "Ron".

