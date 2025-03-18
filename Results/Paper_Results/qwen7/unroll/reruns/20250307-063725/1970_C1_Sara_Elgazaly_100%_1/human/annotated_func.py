#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer u_1 such that 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: x is an integer input from the user, y is an integer input from the user, n is an integer such that 2 ≤ n ≤ 2×10^5, t is 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer u_1 such that 1 ≤ u_1 ≤ n; `lst` is a defaultdict where for each key a (where 1 ≤ a ≤ n), the value is a list containing all b such that there was an input (a, b) in the range of x-1 iterations; `rev` is a defaultdict where for each key b (where 1 ≤ b ≤ n), the value is a list containing all a such that there was an input (a, b) in the range of x-1 iterations.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: The variable `one` will be toggled between True and False depending on the number of iterations in the loop, `tmp` will be set to the last element of the list corresponding to its current value in `lst` until `lst[tmp]` becomes empty.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: Output State: `two` is `False`, `one` is toggled between `True` and `False` depending on the number of iterations in the loop, `tmp` is equal to an element from the list `rev[tmp]` after all iterations.
    #
    #Explanation: The loop continues as long as `rev[tmp]` is not empty. In each iteration, the value of `two` is toggled (i.e., if it was `True`, it becomes `False`, and vice versa), and `tmp` is updated to the last element of the list `rev[tmp]`. Therefore, after all iterations, `two` will be `False` because it starts as `True` and gets toggled with each iteration. The state of `one` depends on the number of iterations; if the number of iterations is odd, `one` will be `False`, and if even, `one` will be `True`. The variable `tmp` will hold the last element from the list `rev[tmp]` after the loop finishes executing.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function reads user inputs to construct two dictionaries, `lst` and `rev`, representing a tree structure. It then checks the parity of the path lengths from a given node to its descendants and ancestors. Based on the results, it prints either "Hermione" or "Ron".

