#State of the program right berfore the function call: u is an integer representing a character label in the range [1, n], e is a list of adjacency lists where each entry e[u] is a list of tuples (v, c), where v is another character label in the range [1, n] and c is a boolean indicating whether u and v love each other (True) or hate each other (False); vis is a list of booleans or integers representing the love/hate status of each character, initially set to False.
def func_1(u):
    sz = len(e[u])
    ok = True
    for i in range(sz):
        v = e[u][i][0]
        
        c = e[u][i][1]
        
        if vis[v] == False:
            if c == True:
                vis[v] = vis[u]
            else:
                vis[v] = -vis[u]
            ok = func_1(v)
        
        if c == 1 and vis[v] != vis[u]:
            return False
        
        if c == 0 and vis[v] != -vis[u]:
            return False
        
    #State of the program after the  for loop has been executed: `u` is an integer in the range [1, n], `e` is a list of adjacency lists, `vis` is a list of booleans or integers, `sz` is the length of the list `e[u]`, `ok` is the final return value of `func_1(v)` after all iterations of the loop, `v` is a character label in the range [1, n], and `c` is a boolean indicating whether `u` and `v` love each other (True) or hate each other (False). If the loop executes, `vis[v]` is set to `vis[u]` if `c` is True, and to `-vis[u]` if `c` is False, ensuring that for any two connected nodes, `vis[v]` is either the same as `vis[u]` if they love each other or the negation of `vis[u]` if they hate each other. If the loop does not execute (when `sz` is 0), `vis` remains as its initial state, which is False for all elements.
    return ok
    #The program returns `ok`, which is the final return value of `func_1(v)` after all iterations of the loop, considering the values of `vis[v]` based on whether `u` and `v` love or hate each other
#Overall this is what the function does:The function `func_1` accepts an integer `u`, a list of adjacency lists `e`, and a list `vis`. It performs a depth-first search (DFS) traversal of the graph represented by `e`, updating the `vis` list based on the relationship (love or hate) between `u` and each of its neighbors. For each neighbor `v`, if `vis[v]` is not yet set, `vis[v]` is updated to `vis[u]` if `u` and `v` love each other (`c == True`), or to `-vis[u]` if they hate each other (`c == False`). The function recursively calls itself for each neighbor. If at any point the relationships violate the conditions (either loving characters have different signs in `vis` or hating characters have the same sign), the function returns `False`. Otherwise, it returns `ok`, which is the final return value of the recursive calls, ensuring that the `vis` list maintains the required relationship signs for all connected components. The function can only return `True` (or `ok` being `True`) if the entire graph can be consistently labeled according to the given relationships without violating any conditions.

#State of the program right berfore the function call: n and m are integers such that 3 ≤ n ≤ 100 000 and 0 ≤ m ≤ 100 000. e is a list of adjacency lists where e[i] contains pairs [v, c] for each vertex v connected to vertex i with a relationship described by c (c is 1 if they love each other and 0 if they hate each other). vis is a boolean list of length n indicating whether each character has been visited during the graph traversal. mod is an integer representing the modulo value (1 000 000 007).
def func_2():
    n, m = map(int, raw_input().split())
    for i in range(m):
        u, v, c = map(int, raw_input().split())
        
        u -= 1
        
        v -= 1
        
        e[u].append([v, c])
        
        e[v].append([u, c])
        
    #State of the program after the  for loop has been executed: `n` is an integer between 3 and 100,000 inclusive; `m` is the total number of edges added; `i` is `m-1`; `vis` is a boolean list of length `n`; `mod` is 1,000,000,007; `u` and `v` are integers representing the nodes connected by an edge, each decremented by 1; `c` is an integer representing the cost of the edge; `e[u]` and `e[v]` are adjacency lists containing all the edges added by the loop.
    cnt = 0
    for i in range(n):
        if vis[i] == False:
            vis[i] = True
            cnt += 1
            if func_1(i) == False:
                cnt = 0
                break
        
    #State of the program after the  for loop has been executed: `n` is an integer between 3 and 100,000 inclusive; `m` is the total number of edges added and satisfies `1 <= m < n+1`; `vis` is a boolean list of length `n` where exactly `m` elements are set to `True`; `mod` is 1,000,000,007; `u` and `v` are integers representing the nodes connected by an edge, each decremented by 1; `c` is an integer representing the cost of the edge; `e[u]` and `e[v]` are adjacency lists containing all the edges added by the loop; `cnt` is 0. If the loop completes all iterations without breaking, `cnt` will be 0, meaning no node was found to violate the condition in `func_1(i)` during any iteration. If the loop breaks, `cnt` will be 0 and exactly `m` nodes were visited.
    ans = 1
    if (cnt == 0) :
        ans = 0
    #State of the program after the if block has been executed: *`n` is an integer between 3 and 100,000 inclusive; `m` is the total number of edges added and satisfies `1 <= m < n+1`; `vis` is a boolean list of length `n` where exactly `m` elements are set to `True`; `mod` is 1,000,000,007; `u` and `v` are integers representing the nodes connected by an edge, each decremented by 1; `c` is an integer representing the cost of the edge; `e[u]` and `e[v]` are adjacency lists containing all the edges added by the loop; `cnt` is 0; `ans` is 1, as it starts from 1 and is not modified in the if part since `cnt == 0`.
    for i in (1, cnt):
        ans *= 2
        
        ans %= mod
        
    #State of the program after the  for loop has been executed: Output State:
    print(ans)
#Overall this is what the function does:The function processes a graph represented by adjacency lists `e` and determines if the graph can be split into disjoint sets such that each set is connected internally and the relationship between any two nodes within a set is "love" (denoted by `c=1`). It performs a depth-first search (DFS) to visit all nodes, ensuring no node violates the "love" condition within its set. If any node violates the condition, the function sets `cnt` to 0 and exits early. If no node violates the condition, it calculates the number of ways to partition the graph into such sets using bitwise operations and returns the result modulo \(1,000,000,007\). If no valid partitioning is possible, it returns 0.

