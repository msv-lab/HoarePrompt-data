#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? d (where d is an integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns v and u, where v and u are input integers.
#Overall this is what the function does:The function accepts an integer `d` within the range 0 to n-1 and reads two integers `v` and `u` from user input. It then returns these two integers `v` and `u`.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5.
def func_2(n):
    path = []
    remaining_vertices = set(range(1, n + 1))
    while remaining_vertices:
        for d in range(n - 1, -1, -1):
            v, u = func_1(d)
            if v == 0:
                continue
            if v in remaining_vertices:
                path.append(v)
                remaining_vertices.remove(v)
                break
        
    #State: Output State: `remaining_vertices` is an empty set, `d` is -1, `n` is less than or equal to 0, and `path` contains a sequence of vertices from the loop, ending with the last `u` value encountered before the loop terminates.
    #
    #Explanation: After the loop completes all its iterations, `remaining_vertices` will be empty because all possible vertices have been processed and added to `path`. The variable `d` will be -1 because the loop decrements `d` from `n-1` to 0 and then continues until `d` reaches -1. The variable `n` will still be less than or equal to 0 as per the given conditions, even though it might have been greater initially. The `path` will contain all the vertices that satisfied the condition `v in remaining_vertices` during the loop's execution, forming a sequence of vertices that were added to `path` before the loop terminated.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: !
    sys.stdout.flush()
#Overall this is what the function does:The function accepts an integer \( n \) where \( 2 \leq n \leq 10^5 \). It constructs a path by iterating through possible values and adding vertices to the path based on certain conditions. After processing all possible vertices, it prints the path as a sequence of vertices. The function does not return any value; instead, it prints the path and ensures that all vertices are included in the path before terminating.

