#State of the program right berfore the function call: n is an integer such that 2 \leq n \leq 2 \times 10^5, t is an integer and always 1, u and v are integers such that 1 \leq u, v \leq n, and u_1 is an integer such that 1 \leq u_1 \leq n. The tree is represented by a list of edges (u, v) and has exactly two leaves.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `t` is 1, `u` and `v` are integers such that 1 ≤ u, v ≤ n, `u_1` is an integer such that 1 ≤ u_1 ≤ n, `x` is an integer provided by the user and must be greater than or equal to 2, `y` is an integer provided by the user, `a` and `b` are integers provided by the user, `lst` is a defaultdict with lists as default values, and for each pair of integers (a, b) provided by the user during the loop, `lst[a]` contains `b` as an element, and `lst[b]` contains `a` as an element.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `t` is 1, `u` and `v` are integers such that 1 ≤ u, v ≤ n, `u_1` is an integer such that 1 ≤ u_1 ≤ n, `x` is the last value of `y` that was not an empty list in `lst`, `y` is the last element of `lst[x]` before the loop terminated, `a` and `b` are integers provided by the user, `lst[x]` is now empty, `s` is the negation of the initial state of `s` (i.e., if `s` was True initially, it will be False, and vice versa).
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: - If `s` was initially `True`, then `s` is now `False`, and the print statement will output `'Ron'`.
    #   - If `s` was initially `False`, then `s` is now `True`, and the print statement will output `'Hermione'`.
    #
    #Since the initial state of `s` is not explicitly provided, we can only describe the output based on the given information.
    #
    #Output:
#Overall this is what the function does:The function `func` reads two integers `x` and `y` from user input, then reads `x-1` pairs of integers to construct a tree represented as a defaultdict of lists. It traverses the tree starting from node `x`, repeatedly moving to a non-leaf node until it reaches a leaf. The function toggles a boolean variable `s` based on the traversal and prints 'Hermione' if `s` is True and 'Ron' if `s` is False. The final state of the program is that `lst[x]` is empty, and the boolean `s` has been toggled an even number of times, resulting in the opposite of its initial state. The function does not return any value.

