#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer such that 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: Output State: The loop will execute `x-1` times in total. After all iterations, `x` must be equal to the final value it was set to, which is at least 1 more than the number of times the loop runs. For each iteration, two integers `a` and `b` are entered by the user and appended to each other's lists in `lst`. Therefore, for every pair `(a, b)` entered, both `lst[a]` and `lst[b]` will contain each other as elements. The final state of `lst` will be a dictionary where each key (integer) points to a list containing all the keys that are connected to it through the pairs entered during the loop's iterations.
    #
    #In simpler terms, after the loop completes all its iterations, `x` will be the total number of iterations plus one, `a` and `b` will be the last two integers entered by the user, and `lst` will be a dictionary where each key has a list of all keys that are connected to it via the pairs entered during the loop.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: Output State: `s` is True, `x` is equal to `y`, `a` and `b` are the last two integers entered by the user, and `lst[x]` is an empty list.
    #
    #Explanation: The loop continues to execute as long as there are elements in any of the lists within the dictionary `lst`. After each full cycle through the loop (which involves potentially multiple iterations of the inner while loop), the variable `s` toggles between True and False. Since the loop will eventually terminate when all lists within `lst` are empty, the final state of `s` will be True (as it starts as True and toggles with each full iteration). The variable `x` will be set to the last `y` that caused the inner while loop to exit, and `lst[x]` will be an empty list because the loop terminates only when all lists in `lst` are empty. The values of `a` and `b` remain unchanged as they are not affected by the loop.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function constructs an undirected graph using a dictionary where each key represents a node and its value is a list of nodes connected to it. It then traverses the graph starting from the node `x` until all nodes are visited, toggling a boolean flag `s` with each traversal. Finally, it prints either "Hermione" or "Ron" based on the state of `s` after the traversal. The function does not return any value but prints "Ron" in all cases.

