#State of the program right berfore the function call: No variables in the function signature. The function `func_1` is assumed to read input from the standard input and return a map object containing integers, which are split from the input string.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing integers that are split from the input string.
#Overall this is what the function does:The function `func_1` reads a line of input from the standard input, splits it into components based on whitespace, converts each component into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are used in the function signature of `func_2`.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers that are obtained by splitting the input string and converting each split substring into an integer.
#Overall this is what the function does:The function `func_2` takes no input parameters. It reads a line of input from the user, splits the line into substrings based on whitespace, converts each substring into an integer, and returns a list of these integers.

#State of the program right berfore the function call: n is an integer representing the number of sides of a regular polygon (4 ≤ n ≤ 10^9), and v is a list of integers representing vertices chosen by Bessie (2 ≤ len(v) ≤ min(n, 2 · 10^5)).
def func_3(n, v):
    return [v for i in range(n)]
    #The program returns a list that contains the list `v` repeated `n` times.
#Overall this is what the function does:The function takes an integer `n` and a list `v` as input and returns a new list where the list `v` is repeated `n` times.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon (4 ≤ n ≤ 10^9), m is an integer representing the number of vertices Bessie has chosen (2 ≤ m ≤ min(n, 2 · 10^5)), and v is a value that will be used to populate a 2D list of dimensions n by m.
def func_4(n, m, v):
    return [[v for i in range(m)] for i in range(n)]
    #The program returns a 2D list with n rows and m columns, where each element in the list is the value v.
#Overall this is what the function does:The function generates and returns a 2D list with `n` rows and `m` columns, where each element in the list is set to the value `v`.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, and m is an integer representing the number of edges or connections between vertices that will be added to the list of adjacency lists.
def func_5(n, m):
    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x].append(y)
        
        l[y].append(x)
        
    #State: `n` is an integer representing the number of sides of the polygon, `m` is an integer representing the number of edges or connections between vertices that will be added to the list of adjacency lists and must be greater than 0, `l` is a list of `n + 1` lists where each list contains the indices of the vertices that are connected to the corresponding vertex, `i` is `m - 1`, `x` and `y` are the values returned by `func_1()` in the last iteration.
    return l
    #The program returns `l`, which is a list of `n + 1` lists where each inner list contains the indices of the vertices that are connected to the corresponding vertex.
#Overall this is what the function does:The function accepts two integer parameters, `n` representing the number of vertices in a graph, and `m` representing the number of edges. It returns a list `l` of `n + 1` lists, where each inner list contains the indices of the vertices that are directly connected to the corresponding vertex, effectively representing an adjacency list of the graph.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon (4 ≤ n ≤ 10^9), and m is an integer representing the number of vertices that can be used to form diagonals (2 ≤ m ≤ min(n, 2 · 10^5)).
def func_6(n, m):
    l = [[(0) for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x][y] = 1
        
        l[y][x] = 1
        
    #State: `n` is an integer representing the number of sides of the polygon (4 ≤ n ≤ 10^9), `m` is an integer representing the number of vertices that can be used to form diagonals (2 ≤ m ≤ min(n, 2 · 10^5)) and must be greater than 0, `l` is a 2D list of size (n+1) x (n+1) with `l[x][y]` set to 1 for `m` pairs of vertices (x, y) returned by `func_1()`, `i` is `m-1`, `x` and `y` are the values returned by `func_1()` in the last iteration.
    return l
    #The program returns a 2D list `l` of size (n+1) x (n+1) where `l[x][y]` is set to 1 for `m` pairs of vertices (x, y) returned by `func_1()`.
#Overall this is what the function does:The function accepts two parameters, `n` and `m`. `n` represents the number of sides of a polygon, constrained by 4 ≤ n ≤ 10^9. `m` represents the number of vertices that can be used to form diagonals, constrained by 2 ≤ m ≤ min(n, 2 · 10^5). The function returns a 2D list `l` of size (n+1) x (n+1) where `l[x][y]` is set to 1 for `m` pairs of vertices (x, y) returned by `func_1()`.

#State of the program right berfore the function call: l is a list of integers.
def func_7(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    #State: `l` is a list of integers, and `d` is a dictionary where each key is an integer from the list `l` and its value is the count of how many times that integer appears in `l`.
    return d
    #The program returns a dictionary `d` where each key is an integer from the list `l` and its value is the count of how many times that integer appears in `l`.
#Overall this is what the function does:The function accepts a list of integers and returns a dictionary where each key is an integer from the list and its value is the count of how many times that integer appears in the list.

#State of the program right berfore the function call: l is a 2D list of integers, n is the number of rows in l, and m is the number of columns in l.
def func_8(l):
    n = len(l)
    m = len(l[0])
    p = [[(0) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
        
    #State: `p` is a 2D list of dimensions `(n+1) x (m+1)` where `p[i][j]` is the sum of all elements in the submatrix of `l` from `(0,0)` to `(i-1,j-1)` for all `i` from 1 to `n` and for all `j` from 1 to `m`.
    return p
    #The program returns a 2D list `p` of dimensions `(n+1) x (m+1)` where each element `p[i][j]` is the sum of all elements in the submatrix of `l` from `(0,0)` to `(i-1,j-1)` for all `i` from 1 to `n` and for all `j` from 1 to `m`.
#Overall this is what the function does:The function accepts a 2D list `l` of integers and returns a 2D list `p` of dimensions `(n+1) x (m+1)`. Each element `p[i][j]` in the returned list represents the sum of all elements in the submatrix of `l` from `(0,0)` to `(i-1,j-1)`, where `n` is the number of rows and `m` is the number of columns in `l`.

#State of the program right berfore the function call: x is a non-negative integer.
def func_9(x):
    return max(1 - (x & x - 1), 0)
    #The program returns 1 if x is a power of 2, otherwise it returns 0.
#Overall this is what the function does:The function accepts a non-negative integer `x` and returns 1 if `x` is a power of 2; otherwise, it returns 0.

#State of the program right berfore the function call: l is a list of integers.
def func_10(l):
    a = 0
    for i in l:
        a = gcd(a, i)
        
    #State: `l` is a list of integers, `a` is the greatest common divisor of all integers in `l`.
    return a
    #The program returns `a`, which is the greatest common divisor of all integers in the list `l`.
#Overall this is what the function does:The function accepts a list of integers and returns their greatest common divisor.

#State of the program right berfore the function call: num is an integer greater than 1.
def func_11(num):
    prime = [(True) for i in range(num + 1)]
    Highest_Prime = [(0) for i in range(num + 1)]
    Lowest_Prime = [(0) for i in range(num + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p <= num:
        if prime[p] == True:
            Lowest_Prime[p] = p
            Highest_Prime[p] = p
            for i in range(2 * p, num + 1, p):
                prime[i] = False
                Highest_Prime[i] = p
                if Lowest_Prime[i] == 0:
                    Lowest_Prime[i] = p
        
        p += 1
        
    #State: `num` is an integer greater than 1; `prime` is a list of `num + 1` elements where `prime[i]` is `True` if `i` is a prime number and `False` otherwise; `Highest_Prime` is a list of `num + 1` elements where `Highest_Prime[i]` is the highest prime factor of `i`; `Lowest_Prime` is a list of `num + 1` elements where `Lowest_Prime[i]` is the lowest prime factor of `i`; `p` is `num + 1`.
    p = []
    for i in range(num + 1):
        if prime[i]:
            p.append(i)
        
    #State: `num` is an integer greater than 1; `prime` is a list of `num + 1` elements where `prime[i]` is `True` if `i` is a prime number and `False` otherwise; `Highest_Prime` is a list of `num + 1` elements where `Highest_Prime[i]` is the highest prime factor of `i`; `Lowest_Prime` is a list of `num + 1` elements where `Lowest_Prime[i]` is the lowest prime factor of `i`; `p` is a list containing all prime numbers from `2` to `num`.
    return p
    #The program returns a list `p` containing all prime numbers from 2 to `num`, where `num` is an integer greater than 1.
#Overall this is what the function does:The function accepts an integer `num` greater than 1 and returns a list of all prime numbers from 2 to `num`.

#State of the program right berfore the function call: num is a positive integer, Prime_array is a list or array where Prime_array[i] contains the smallest prime factor of i for all i from 2 up to at least the value of num.
def func_12(num, Prime_array):
    d = {}
    while num != 1:
        x = Prime_array[num]
        
        d[x] = d.get(x, 0) + 1
        
        num //= x
        
    #State: `num` is 1, `Prime_array` remains the same, `d` contains the prime factorization of the original `num`.
    return d
    #The program returns an empty list `d`
#Overall this is what the function does:The function accepts a positive integer `num` and a list or array `Prime_array` where `Prime_array[i]` contains the smallest prime factor of `i` for all `i` from 2 up to at least the value of `num`. It returns a dictionary `d` containing the prime factorization of `num`, where the keys are the prime factors and the values are their respective counts.

#State of the program right berfore the function call: n is an integer greater than or equal to 2.
def func_13(n):
    d = {}
    x = 2
    while x * x <= n:
        while n % x == 0:
            d[x] = d.get(x, 0) + 1
            n //= x
        
        x += 1
        
    #State: n is 1; d is {2: 3, 3: 3}; x is 4.
    if (n > 1) :
        d[n] = d.get(n, 0) + 1
    #State: `n` is 1; `d` is `{2: 3, 3: 3}`; `x` is 4. Since the condition `n > 1` is false, the dictionary `d` and the integer `x` remain unchanged.
    return d
    #The program returns the dictionary `{2: 3, 3: 3}`
#Overall this is what the function does:The function accepts an integer `n` greater than or equal to 2 and returns a dictionary representing the prime factorization of `n`. For the given example where `n` is 72, it returns `{2: 3, 3: 2}`. However, based on the provided return postcondition, the function always returns `{2: 3, 3: 3}`.

#State of the program right berfore the function call: d is a dictionary where keys are integers greater than 1 and values are positive integers.
def func_14(d):
    s = 0
    for i in d:
        s += pow(i, d[i] - 1) * (i - 1)
        
    #State: `d` is the same dictionary as the initial state; `s` is the sum of `pow(i, d[i] - 1) * (i - 1)` for all key-value pairs in `d`.
    return s
    #The program returns the sum of `pow(i, d[i] - 1) * (i - 1)` for all key-value pairs in `d`.
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers greater than 1 and values are positive integers. It returns the sum of `pow(i, d[i] - 1) * (i - 1)` for all key-value pairs in `d`.

#State of the program right berfore the function call: n is a positive integer, and mod is a positive integer.
def func_15(n, mod):
    f = [1]
    for i in range(1, n + 1):
        f.append(f[i - 1] * i % mod % mod)
        
    #State: `n` is a positive integer, `mod` is a positive integer, `f` is a list containing the elements `[1, 1, 2 % mod, (2 % mod) * 3 % mod, ..., (n % mod) * n % mod]`
    return f
    #The program returns a list `f` containing the elements `[1, 1, 2 % mod, (2 % mod) * 3 % mod, ..., (n % mod) * n % mod]`.
#Overall this is what the function does:The function `func_15` accepts two parameters, `n` and `mod`, both of which are positive integers. It returns a list `f` containing the elements `[1, 1, 2 % mod, (2 % mod) * 3 % mod, ..., (n % mod) * n % mod]`.

#State of the program right berfore the function call: n is a positive integer, mod is an integer where mod can be -1 or any other integer value.
def func_16(n, mod):
    if (mod == -1) :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) * (dearr[i - 1] + dearr[i - 2]))
            
        #State: n is 4, mod is -1, dearr is [1, 0, 1, 2, 9, 44]
    else :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod)
            
        #State: `dearr` is `[1, 0, 1 % mod, 2 % mod, (3 % mod) * (3 % mod) % mod, ..., ((n % mod) * (dearr[n - 1] + dearr[n - 2]) % mod)`
    #State: `n` is a positive integer, `mod` is an integer where `mod` can be -1 or any other integer value. If `mod` is -1, `dearr` is set to `[1, 0, 1, 2, 9, 44]`. Otherwise, `dearr` is a list where each element is calculated based on the formula: the first three elements are `1`, `0`, and `1 % mod`, the fourth element is `2 % mod`, the fifth element is `(3 % mod) * (3 % mod) % mod`, and so on, with the nth element being `((n % mod) * (dearr[n - 1] + dearr[n - 2]) % mod)` for `n` greater than 2.
    return dearr
    #The program returns `dearr` which is `[1, 0, 1, 2, 9, 44]` if `mod` is -1, otherwise it is `[1, 0, 1 % mod, 2 % mod, (3 % mod) * (3 % mod) % mod, (4 % mod) * ((3 % mod) * (3 % mod) % mod + 2 % mod) % mod, ...]`
#Overall this is what the function does:The function accepts a positive integer `n` and an integer `mod` (which can be -1 or any other integer). It returns a list `dearr` where the elements are calculated based on specific arithmetic rules. If `mod` is -1, the list is `[1, 0, 1, 2, 9, 44]`. Otherwise, the list starts with `[1, 0]` and each subsequent element is computed using the formula involving modulo operations with `mod`.

#State of the program right berfore the function call: p is a sorted list of integers, and x is an integer. The function returns the index of x in p if x is present, otherwise it returns -1.
def func_17(p, x):
    i = bisect_left(p, x)
    if (i != len(p) and p[i] == x) :
        return i
        #The program returns `i`, which is the index of `x` in the sorted list `p`.
    else :
        return -1
        #The program returns -1.
#Overall this is what the function does:The function accepts a sorted list of integers `p` and an integer `x`. It returns the index of `x` in `p` if `x` is present, otherwise it returns -1.

#State of the program right berfore the function call: p is a sorted list of integers, and x is an integer such that x is within the range of values in p.
def func_18(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[0] > x) :
        return -1
        #The program returns -1
    #State: `p` is a sorted list of integers, `x` is an integer such that `x` is within the range of values in `p`, `n` is the length of `p`, `l` is 0, `r` is `n - 1`, and `p[0]` is less than or equal to `x`
    while l <= r:
        mid = (l + r) // 2
        
        if p[mid] <= x:
            if mid != n - 1:
                if p[mid + 1] > x:
                    break
                else:
                    l = mid + 1
            else:
                mid = n - 1
                break
        else:
            r = mid - 1
        
    #State: `l` is `mid + 1` or `n` if `x` is greater than the last element, `r` is `mid`, and `mid` is the largest index such that `p[mid] <= x`.
    return mid
    #The program returns `mid`, which is the largest index such that `p[mid] <= x`.
#Overall this is what the function does:The function `func_18` accepts a sorted list of integers `p` and an integer `x`. It returns `-1` if `x` is less than the smallest element in `p`. Otherwise, it returns the largest index `mid` such that `p[mid]` is less than or equal to `x`.

#State of the program right berfore the function call: p is a list of integers sorted in non-decreasing order, and x is an integer.
def func_19(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[-1] < x) :
        return n
        #The program returns n, which is the length of the list p.
    #State: `p` is a list of integers sorted in non-decreasing order, `x` is an integer, `n` is the length of `p`, `l` is 0, `r` is `n - 1`. The last element of `p` is greater than or equal to `x`.
    while l <= r:
        mid = (l + r) // 2
        
        if p[mid] >= x:
            if mid != 0:
                if p[mid - 1] < x:
                    break
                else:
                    r = mid - 1
            else:
                mid = 0
                break
        else:
            l = mid + 1
        
    #State: `l` is the index of the first element in `p` that is greater than or equal to `x`, and `r` is `l - 1`.
    return mid
    #The program returns `mid`
#Overall this is what the function does:The function `func_19` accepts a sorted list of integers `p` and an integer `x`. It returns the index of the first element in `p` that is greater than or equal to `x`. If all elements in `p` are less than `x`, it returns the length of the list `p`.

#State of the program right berfore the function call: x is a non-negative integer.
def func_20(x):
    if (x == 0 or x == 1) :
        return x
        #The program returns the value of x, which is either 0 or 1.
    #State: x is a non-negative integer, and x is neither 0 nor 1
    l = 1
    r = x
    while l <= r:
        mid = (l + r) / 2
        
        y = mid * mid
        
        if y > x:
            r = mid - 1
        elif y == x:
            return mid
        elif (mid + 1) * (mid + 1) > x:
            return mid
        else:
            l = mid + 1
        
    #State: The loop terminates with `mid` being the largest integer such that `mid * mid` is less than or equal to `x`.
#Overall this is what the function does:The function `func_20` accepts a non-negative integer `x` and returns the integer part of the square root of `x`.

#State of the program right berfore the function call: a and b are non-negative integers, mod is a positive integer.
def func_21(a, b, mod):
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        
        a = a * a % mod
        
        b >>= 1
        
    #State: - `a` will be some value that is the result of repeated squaring and reduction modulo `mod`, but it is not directly relevant to the final answer.
    #- `b` will be 0, indicating the loop has terminated.
    #- `mod` remains unchanged as it is a constant.
    #- `ans` will be the result of \( a^b \mod \text{mod} \).
    #
    #Therefore, the final output state is:
    #
    #Output State:
    return ans
    #The program returns 1
#Overall this is what the function does:The function accepts two non-negative integers `a` and `b`, and a positive integer `mod`. It computes and returns the result of \( a^b \mod \text{mod} \).

#State of the program right berfore the function call: a and b are lists of integers.
def func_22(a, b):
    dp = [([0] * (len(b) + 1)) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
    #State: `dp` is a 2D list where `dp[i][j]` contains the length of the LCS of the first `i` elements of `a` and the first `j` elements of `b`. The value `dp[len(a)][len(b)]` represents the length of the LCS of `a` and `b`.
    i, j = len(a), len(b)
    l = []
    while i != 0 and j != 0:
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            i -= 1
            j -= 1
            l.append(a[i])
        
    #State: `dp` is a 2D list where `dp[i][j]` contains the length of the LCS of the first `i` elements of `a` and the first `j` elements of `b`. `i` is 0, `j` is 0, and `l` is a list containing the characters of the LCS of `a` and `b` in reverse order.
    s = ''.join(l)
    return s[::-1]
    #The program returns an empty string
#Overall this is what the function does:The function `func_22` accepts two lists of integers, `a` and `b`, and returns an empty string.

#State of the program right berfore the function call: arr is a list of integers.
def func_23(arr):
    l = []
    for i in arr:
        pos = bisect_left(l, i)
        
        if pos == len(l):
            l.append(i)
        else:
            l[pos] = i
        
    #State: `l` is a sorted list representing the longest non-decreasing subsequence of `arr`.
    return len(l)
    #The program returns the length of the sorted list `l`, which represents the longest non-decreasing subsequence of `arr`.
#Overall this is what the function does:The function accepts a list of integers and returns the length of the longest non-decreasing subsequence within the list.

#State of the program right berfore the function call: ver is an integer representing a vertex in the graph, graph is a dictionary where keys are vertices and values are lists of adjacent vertices, and vis is a list or dictionary used to keep track of visited vertices such that vis[node] is 1 if the node has been visited and 0 otherwise.
def func_24(ver):
    stack = []
    stack.append(ver)
    vis[ver] = 1
    while len(stack):
        ver = stack.pop()
        
        print(ver, end=' ')
        
        for node in graph[ver]:
            if not vis[node]:
                stack.append(node)
                vis[node] = 1
        
    #State: `ver` is undefined, `graph` remains unchanged, `vis` has `1` for all nodes visited, and `stack` is empty.
#Overall this is what the function does:The function `func_24` starts from a given vertex `ver` and performs a depth-first traversal of the graph, marking all visited vertices in the `vis` list or dictionary. It prints each visited vertex. The function does not return a value but modifies the `vis` list or dictionary to reflect the visited status of the vertices.

#State of the program right berfore the function call: ver is an integer representing a vertex in the graph, graph is a dictionary or adjacency list representing the graph where each key is a vertex and its value is a list of adjacent vertices, vis is a list or dictionary used to keep track of visited vertices where vis[node] is 1 if the node has been visited and 0 otherwise.
def func_25(ver):
    q = deque()
    q.append(ver)
    vis[ver] = 1
    while len(q):
        ver = q.popleft()
        
        print(ver, end=' ')
        
        for node in graph[ver]:
            if not vis[node]:
                q.append(node)
                vis[node] = 1
        
    #State: All vertices in the connected component of the initial vertex `ver` have been visited, printed, and marked as visited in `vis`. The queue `q` is empty.
#Overall this is what the function does:The function `func_25` performs a breadth-first traversal (BFS) starting from the given vertex `ver` in the graph represented by `graph`. It prints each vertex in the connected component of `ver` and marks them as visited in the `vis` list or dictionary. The function modifies `vis` in place to reflect which vertices have been visited.

