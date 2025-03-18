#State of the program right berfore the function call: l is a non-empty list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the maximum value in the list 'l'
#Overall this is what the function does:The function accepts a non-empty list of integers and returns the index of the maximum value within that list.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 \cdot 10^3, u2vs is a list of length n where each element is a list representing the neighbors of the corresponding vertex in the tree, and the input format is correct according to the problem description.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: Output State: After the loop executes all the iterations, `n` must be greater than 1, `u` is an integer from the input decreased by `n-1`, `v` is one less than the integer from the input decreased by `n-2`, and `u2vs[v]` contains all integers from `u-(n-2)` to `u-1` and `v`.
    #
    #In simpler terms, after the loop completes all its iterations, `u2vs[v]` will contain a list of all the `u` values that were appended to `v` during the loop's execution, starting from `u-n+2` up to `u-1`. The exact values depend on the inputs provided during each iteration of the loop.
    d, _ = bfs(0)
    a = func_1(d)
    d, previous = bfs(a)
    b = func_1(d)
    path_ba = [b]
    while True:
        n = previous[path_ba[-1]]
        
        if n == -1:
            break
        
        path_ba.append(n)
        
    #State: Output State: `d` is the result of `func_1(d)`, `previous` is the result of `bfs(a)`, `b` is the result of `func_1(d)`, `n` is the value of `-1`, `u` is an integer from the input decreased by `-2`, `v` is one less than the integer from the input decreased by `-3`, `u2vs[v]` contains all integers from `u-(-2)` to `u-1`; `path_ba` is a list containing `b` and all the values that were appended during the loop iterations until `n` became `-1`.
    #
    #Explanation: The loop continues to append the value of `previous[path_ba[-1]]` to `path_ba` as long as `n` (which starts as `previous[path_ba[-1]]`) is not equal to `-1`. After the loop exits, `n` will be `-1`, indicating that the path has ended. Therefore, `path_ba` will contain a sequence of nodes starting from `b` and ending at a node where no further path can be found, which is indicated by `n` being `-1`. The other variables (`d`, `previous`, `b`, `u`, `v`, `u2vs[v]`) remain unchanged as they are not affected by the loop.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: Output State: `i` is equal to `ci`; `ci` is `len(path_ba) // 2`; `ops` is a list containing `ci + 1` tuples, each in the form `(c, index)`, where `index` ranges from `0` to `ci`.
        #
        #Explanation: The loop runs `ci + 1` times, where `ci` is the integer division of the length of `path_ba` by 2. After all iterations, the variable `i` will be equal to `ci`. The list `ops` will contain `ci + 1` tuples, with each tuple being `(c, index)`, where `index` starts from `0` and increments by `1` up to `ci`.
    else :
        ci2 = len(path_ba) // 2
        ci1 = ci2 - 1
        c1 = path_ba[ci1]
        c2 = path_ba[ci2]
        for i in range(1, len(path_ba) - ci1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: Output State: `len(path_ba) - ci1` must be a positive even number, `i` is equal to the second last index of `path_ba`, `ops` is a list containing tuples where each tuple consists of either `c1` or `c2` paired with every even index from 1 up to and including the second last index of `path_ba`.
        #
        #This means that after all iterations of the loop, `ops` will contain pairs of `c1` and `c2` with every even index from 1 to the second last index of `path_ba`. The variable `i` will be set to the second last index of `path_ba` since the loop increments by 2 each time and stops just before the last index.
    #State: `i` is equal to `ci`, where `ci` is `len(path_ba) // 2`. `ops` is a list containing `ci + 1` tuples, each in the form `(c, index)`, where `index` ranges from `0` to `ci` if `len(path_ba) % 2 == 1`. Otherwise, `len(path_ba) - ci` must be a positive even number, `i` is equal to the second last index of `path_ba`, and `ops` is a list containing tuples where each tuple consists of either `c1` or `c2` paired with every even index from 1 up to and including the second last index of `path_ba`.
    print(len(ops))
    #This is printed: i + 1
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: - Given the initial state, `ops` contains tuples where each tuple consists of either `c1` or `c2` paired with every even index from `1` up to and including the second last index of `path_ba`.
    #   - For each tuple `(c, index)` in `ops`, the lambda function will generate a string in the format `'c + 1 index'`.
    #
    #Therefore, the output will be a series of lines, each containing a string in the format `'c + 1 index'` for each tuple in `ops`.
    #
    #Output:
    return None
    #The program returns None
#Overall this is what the function does:The function processes a tree structure defined by the number of vertices `n` and their adjacency list `u2vs`. It performs a breadth-first search (BFS) twice, calculates some values using `func_1`, constructs a path from a starting node `b` to another node, and then based on the length of this path, it populates a list `ops` with specific tuples. Finally, it prints the count of elements in `ops` followed by the formatted content of `ops`. The function does not return any value and ends by returning `None`.

