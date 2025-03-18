#State of the program right berfore the function call: None of the variables are passed as parameters to the function `func_1`. The function is designed to read input from the standard input, which is expected to be a line of space-separated integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains the integers from a line of space-separated integers read from the standard input.
#Overall this is what the function does:The function `func_1` reads a line of space-separated integers from the standard input and returns a map object that contains these integers. The function does not accept any parameters and does not modify any external variables. After the function concludes, the user can iterate over the returned map object to access the integers.

#State of the program right berfore the function call: None
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers, where each integer is derived from the input provided by the user, split by spaces.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list of integers derived from user input, where each integer is separated by spaces. The function reads a line of input from the user, splits it into substrings based on spaces, converts each substring to an integer, and returns the resulting list.

#State of the program right berfore the function call: n is a non-negative integer, v is a value of any type.
def func_3(n, v):
    return [v for i in range(n)]
    #The program returns a list containing `n` elements, where each element is the value `v`.
#Overall this is what the function does:The function `func_3` accepts a non-negative integer `n` and a value `v` of any type. It returns a list containing `n` elements, where each element is `v`. If `n` is 0, the function returns an empty list.

#State of the program right berfore the function call: n and m are non-negative integers, and v is a value of any type.
def func_4(n, m, v):
    return [[v for i in range(m)] for i in range(n)]
    #The program returns a list of lists where each inner list contains `m` copies of the value `v`, and there are `n` such inner lists.
#Overall this is what the function does:The function `func_4` accepts three parameters: `n`, `m`, and `v`. It returns a list of `n` inner lists, where each inner list contains `m` copies of the value `v`. The input parameters `n` and `m` are non-negative integers, and `v` can be of any type. After the function concludes, the original input parameters remain unchanged, and the returned list of lists is the final state of the program.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, and m is a non-negative integer representing the number of edges or connections to be added, such that 0 <= m <= n.
def func_5(n, m):
    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x].append(y)
        
        l[y].append(x)
        
    #State: `n` remains the same, `m` is unchanged, and `l` is a list of `n + 1` lists where each list at index `x` and `y` (as returned by `func_1()`) contains the corresponding `y` and `x` values, respectively, appended to them.
    return l
    #The program returns a list `l` that contains `n + 1` lists, where each list at index `x` and `y` (as returned by `func_1()`) has the corresponding `y` and `x` values appended to it, respectively.
#Overall this is what the function does:The function `func_5` accepts two parameters, `n` and `m`, where `n` is an integer representing the number of sides of a polygon, and `m` is a non-negative integer representing the number of edges or connections to be added, with the constraint 0 <= m <= n. The function returns a list `l` containing `n + 1` lists. Each of these inner lists at index `x` and `y` (as determined by the values returned by `func_1()`) will have the corresponding `y` and `x` values appended to them, respectively. After the function concludes, `n` and `m` remain unchanged, and the list `l` reflects the added connections.

#State of the program right berfore the function call: n is an integer such that 4 <= n <= 10^9, and m is an integer such that 0 <= m <= n.
def func_6(n, m):
    l = [[(0) for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x][y] = 1
        
        l[y][x] = 1
        
    #State: `n` is an integer such that 4 <= n <= 10^9, `m` is an integer such that 0 <= m <= n, `l` is a list of lists of size (n + 1) x (n + 1) where each element is 0, except for the elements at positions (x, y) and (y, x) which are set to 1 for each pair (x, y) returned by `func_1()` during the loop iterations.
    return l
    #The program returns a list of lists `l` of size (n + 1) x (n + 1) where each element is 0, except for the elements at positions (x, y) and (y, x) which are set to 1 for each pair (x, y) returned by `func_1()` during the loop iterations.
#Overall this is what the function does:The function `func_6` accepts two integers `n` and `m`, where `4 <= n <= 10^9` and `0 <= m <= n`. It returns a list of lists `l` of size (n + 1) x (n + 1). Initially, all elements in `l` are set to 0. For each of the `m` iterations, the function `func_1` is called to generate a pair of integers (x, y). The elements at positions (x, y) and (y, x) in `l` are set to 1. The final state of the program is a list of lists `l` where the specified positions are marked with 1, and all other elements remain 0.

#State of the program right berfore the function call: l is a list of integers.
def func_7(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    #State: Output State: `l` is a list of integers, `d` is a dictionary where each key is an integer from the list `l` and each value is the count of how many times that integer appears in `l`.
    return d
    #The program returns a dictionary `d` where each key is an integer from the list `l`, and each value is the count of how many times that integer appears in `l`.
#Overall this is what the function does:The function `func_7` accepts a list of integers `l` and returns a dictionary `d` where each key is an integer from the list `l`, and each value is the count of how many times that integer appears in `l`. The original list `l` remains unchanged.

#State of the program right berfore the function call: l is a 2D list of integers, where each sublist has the same length.
def func_8(l):
    n = len(l)
    m = len(l[0])
    p = [[(0) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
        
    #State: `p` is a 2D list of integers with dimensions `(n + 1) x (m + 1)`, where each element `p[i][j]` (for `1 <= i <= n` and `1 <= j <= m`) is the sum of all elements in `l` from the top-left corner to the element `l[i-1][j-1]`. The first row and the first column of `p` remain zeros.
    return p
    #The program returns a 2D list `p` of integers with dimensions `(n + 1) x (m + 1)`, where each element `p[i][j]` (for `1 <= i <= n` and `1 <= j <= m`) represents the sum of all elements in the original list `l` from the top-left corner to the element `l[i-1][j-1]`. The first row and the first column of `p` are all zeros.
#Overall this is what the function does:The function `func_8` accepts a 2D list `l` of integers, where each sublist has the same length. It returns a 2D list `p` of integers with dimensions `(n + 1) x (m + 1)`, where `n` is the number of rows in `l` and `m` is the number of columns. Each element `p[i][j]` (for `1 <= i <= n` and `1 <= j <= m`) represents the sum of all elements in `l` from the top-left corner to the element `l[i-1][j-1]`. The first row and the first column of `p` are all zeros.

#State of the program right berfore the function call: x is a non-negative integer such that 2 <= x <= 2 * 10^5.
def func_9(x):
    return max(1 - (x & x - 1), 0)
    #The program returns 1 if `x` is a power of 2, otherwise it returns 0.
#Overall this is what the function does:The function `func_9` accepts a non-negative integer `x` within the range 2 to 2 * 10^5. It returns 1 if `x` is a power of 2, and 0 otherwise.

#State of the program right berfore the function call: l is a list of positive integers.
def func_10(l):
    a = 0
    for i in l:
        a = gcd(a, i)
        
    #State: `a` is the greatest common divisor (GCD) of all the integers in the list `l`.
    return a
    #The program returns the greatest common divisor (GCD) of all the integers in the list `l`.
#Overall this is what the function does:The function `func_10` accepts a list `l` of positive integers and returns the greatest common divisor (GCD) of all the integers in the list. After the function concludes, the list `l` remains unchanged, and the returned value is the GCD of the elements in `l`.

#State of the program right berfore the function call: num is a non-negative integer such that num >= 2.
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
        
    #State: The `prime` list contains `True` for prime numbers and `False` for non-prime numbers from index 2 to `num`. The `Highest_Prime` list contains the highest prime factor for each index from 2 to `num`. The `Lowest_Prime` list contains the lowest prime factor for each index from 2 to `num`. The variable `p` is `num` + 1.
    p = []
    for i in range(num + 1):
        if prime[i]:
            p.append(i)
        
    #State: The `p` list contains all the prime numbers from 2 to `num`. The `prime` list, `Highest_Prime` list, and `Lowest_Prime` list remain unchanged.
    return p
    #The program returns the list `p` which contains all the prime numbers from 2 to `num`.
#Overall this is what the function does:The function `func_11` accepts a non-negative integer `num` (where `num` >= 2) and returns a list of all prime numbers from 2 to `num`. After the function concludes, the `prime` list contains `True` for prime numbers and `False` for non-prime numbers from index 2 to `num`. The `Highest_Prime` list contains the highest prime factor for each index from 2 to `num`, and the `Lowest_Prime` list contains the lowest prime factor for each index from 2 to `num`. The variable `p` is a list of all prime numbers from 2 to `num`.

#State of the program right berfore the function call: num is a positive integer greater than 1, and Prime_array is a list or dictionary where Prime_array[num] returns a prime factor of num.
def func_12(num, Prime_array):
    d = {}
    while num != 1:
        x = Prime_array[num]
        
        d[x] = d.get(x, 0) + 1
        
        num //= x
        
    #State: `num` is 1, `d` is a dictionary where each key is a prime factor of the initial `num` and each value is the count of how many times that prime factor divides the initial `num`.
    return d
    #The program returns an empty dictionary `d` because the initial `num` is 1, which has no prime factors.
#Overall this is what the function does:The function `func_12` accepts a positive integer `num` greater than 1 and a list or dictionary `Prime_array`. It returns a dictionary `d` where each key is a prime factor of the initial `num`, and each value is the count of how many times that prime factor divides the initial `num`. If the initial `num` is 1, the function returns an empty dictionary.

#State of the program right berfore the function call: n is a positive integer such that 4 <= n <= 10^9.
def func_13(n):
    d = {}
    x = 2
    while x * x <= n:
        while n % x == 0:
            d[x] = d.get(x, 0) + 1
            n //= x
        
        x += 1
        
    #State: `n` is a positive integer that is either 1 or a prime number greater than the largest `x` checked in the loop, `d` is a dictionary containing the prime factorization of the initial `n` with each prime factor as a key and its exponent as the value, `x` is the smallest integer greater than the square root of the initial `n` that was checked.
    if (n > 1) :
        d[n] = d.get(n, 0) + 1
    #State: *`n` is a positive integer that is either 1 or a prime number greater than the largest `x` checked in the loop. `d` is a dictionary containing the prime factorization of the initial `n` with each prime factor as a key and its exponent as the value. `x` is the smallest integer greater than the square root of the initial `n` that was checked. If `n` > 1, the value of `d[n]` is now `d.get(n, 0) + 1`. Otherwise, `d` remains unchanged.
    return d
    #The program returns the dictionary `d` containing the prime factorization of the initial `n`, with each prime factor as a key and its exponent as the value. If `n` was greater than 1, the value of `d[n]` is now `d.get(n, 0) + 1`. Otherwise, `d` remains unchanged.
#Overall this is what the function does:The function `func_13` accepts a positive integer `n` (4 <= n <= 10^9) and returns a dictionary `d` containing the prime factorization of `n`. Each prime factor is a key in the dictionary, and its corresponding value is the exponent indicating how many times the prime factor divides `n`. If `n` is greater than 1 after the factorization process, it is added to the dictionary with an exponent of 1 (or its existing exponent is incremented by 1). The function does not modify the input `n` but rather computes and returns the prime factorization as a dictionary.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are positive integers.
def func_14(d):
    s = 0
    for i in d:
        s += pow(i, d[i] - 1) * (i - 1)
        
    #State: `s` is 14.
    return s
    #The program returns 14.
#Overall this is what the function does:The function `func_14` accepts a dictionary `d` where keys are integers and values are positive integers. It calculates a sum `s` based on the formula `s += pow(i, d[i] - 1) * (i - 1)` for each key-value pair in the dictionary. The function always returns the integer 14, regardless of the input dictionary.

#State of the program right berfore the function call: n is a non-negative integer, and mod is a positive integer.
def func_15(n, mod):
    f = [1]
    for i in range(1, n + 1):
        f.append(f[i - 1] * i % mod % mod)
        
    #State: `n` is a non-negative integer, `mod` is a positive integer, `f` is a list containing the first `n+1` factorials modulo `mod`.
    return f
    #The program returns a list `f` containing the first `n+1` factorials, each taken modulo `mod`. Here, `n` is a non-negative integer, and `mod` is a positive integer.
#Overall this is what the function does:The function `func_15` accepts two parameters, `n` and `mod`, where `n` is a non-negative integer and `mod` is a positive integer. It returns a list `f` containing the first `n+1` factorials, each computed modulo `mod`. The list `f` has `n+1` elements, where `f[i]` represents the factorial of `i` modulo `mod` for `0 ≤ i ≤ n`.

#State of the program right berfore the function call: n is a positive integer, and mod is an integer that can be -1 or a positive integer.
def func_16(n, mod):
    if (mod == -1) :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) * (dearr[i - 1] + dearr[i - 2]))
            
        #State: Output State: `n` is a positive integer, `mod` is -1, `dearr` is a list containing the first `n + 1` elements of the derangement sequence.
    else :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod)
            
        #State: `n` is a positive integer, `mod` is an integer that can be a positive integer, `dearr` is a list containing the values `[1, 0, (1 * (1 + 0) % mod), (2 * (dearr[2] + 1) % mod), ..., ((n-1) * (dearr[n-1] + dearr[n-2]) % mod)]`.
    #State: *`n` is a positive integer, and `mod` is an integer that can be -1 or a positive integer. If `mod` is -1, `dearr` is a list containing the first `n + 1` elements of the derangement sequence. Otherwise, `dearr` is a list containing the values `[1, 0, (1 * (1 + 0) % mod), (2 * (dearr[2] + 1) % mod), ..., ((n-1) * (dearr[n-1] + dearr[n-2]) % mod)]`.
    return dearr
    #The program returns the list `dearr` which contains the first `n + 1` elements of the derangement sequence if `mod` is -1, or a list of values calculated using the formula `[(1 * (1 + 0) % mod), (2 * (dearr[2] + 1) % mod), ..., ((n-1) * (dearr[n-1] + dearr[n-2]) % mod)]` if `mod` is a positive integer.
#Overall this is what the function does:The function `func_16` accepts two parameters, `n` and `mod`. It returns a list `dearr` of length `n + 1`. If `mod` is -1, the list contains the first `n + 1` elements of the derangement sequence. If `mod` is a positive integer, the list contains values calculated using the formula `((i - 1) * (dearr[i - 1] + dearr[i - 2]) % mod)` for each `i` from 2 to `n`.

#State of the program right berfore the function call: p is a list of integers, and x is an integer.
def func_17(p, x):
    i = bisect_left(p, x)
    if (i != len(p) and p[i] == x) :
        return i
        #The program returns the index `i` of the first element in the list `p` that is not less than `x`, and this element is equal to `x`.
    else :
        return -1
        #The program returns -1.
#Overall this is what the function does:The function `func_17` accepts a list of integers `p` and an integer `x`. It returns the index `i` of the first occurrence of `x` in the list `p` if `x` is found. If `x` is not present in the list, it returns -1.

#State of the program right berfore the function call: p is a list of integers sorted in non-decreasing order, x is an integer such that p[0] <= x <= p[n-1] where n is the length of p.
def func_18(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[0] > x) :
        return -1
        #The program returns -1.
    #State: `p` is a list of integers sorted in non-decreasing order, `x` is an integer such that `p[0] <= x <= p[n-1]`, `n` is the length of `p`, `l` is 0, `r` is `n - 1`, and `p[0]` is less than or equal to `x`
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
        
    #State: `l` is `mid + 1`, `r` is `mid - 1`, and `mid` is the largest index such that `p[mid] <= x`.
    return mid
    #The program returns the largest index `mid` such that `p[mid] <= x`.
#Overall this is what the function does:The function `func_18` accepts a sorted list of integers `p` and an integer `x` within the range of the list. It returns the largest index `mid` such that `p[mid] <= x`. If `x` is less than the smallest element in `p`, it returns `-1`.

#State of the program right berfore the function call: p is a list of distinct integers sorted in non-decreasing order, and x is an integer such that the elements of p are in the range [1, n] where n is the number of sides of the polygon.
def func_19(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[-1] < x) :
        return n
        #The program returns the length of the list `p` which is `n`.
    #State: `p` is a list of distinct integers sorted in non-decreasing order, `x` is an integer such that the elements of `p` are in the range [1, n], `n` is the length of `p`, `l` is 0, `r` is n - 1, and the last element of `p` is greater than or equal to `x`.
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
        
    #State: `l` is the smallest index such that `p[l] >= x`, `r` is `l - 1`, and `mid` is `l`.
    return mid
    #The program returns the smallest index `l` such that `p[l] >= x`.
#Overall this is what the function does:The function `func_19` accepts a sorted list `p` of distinct integers and an integer `x`. It returns the length of `p` if `x` is greater than the last element of `p`. Otherwise, it returns the smallest index `l` such that `p[l]` is greater than or equal to `x`.

#State of the program right berfore the function call: x is a non-negative integer.
def func_20(x):
    if (x == 0 or x == 1) :
        return x
        #The program returns the value of x, which is either 0 or 1.
    #State: x is a non-negative integer, and x is greater than 1
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
        
    #State: The loop returns the largest integer `mid` such that `mid * mid` is less than or equal to `x`.
#Overall this is what the function does:The function `func_20` accepts a non-negative integer `x` and returns the largest integer `y` such that `y * y` is less than or equal to `x`. If `x` is 0 or 1, it returns `x` directly.

#State of the program right berfore the function call: a and b are non-negative integers, and mod is a positive integer.
def func_21(a, b, mod):
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        
        a = a * a % mod
        
        b >>= 1
        
    #State: `ans` is `a` raised to the power of `b` (initial value of `b`), modulo `mod`. `a` is the square of the initial `a`, raised to the power of the number of times `b` was right-shifted, modulo `mod`. `b` is 0.
    return ans
    #The program returns the value of `ans`, which is the result of `a` raised to the power of the initial value of `b`, modulo `mod`.
#Overall this is what the function does:The function `func_21` accepts three parameters `a`, `b`, and `mod`, where `a` and `b` are non-negative integers and `mod` is a positive integer. It returns the result of `a` raised to the power of `b`, modulo `mod`. After the function call, the input parameters `a` and `b` are unchanged, and the program state is such that the returned value `ans` is the correct result of the modular exponentiation.

#State of the program right berfore the function call: a and b are lists of integers or characters.
def func_22(a, b):
    dp = [([0] * (len(b) + 1)) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
    #State: `dp` is a 2D list where `dp[i][j]` contains the length of the longest common subsequence (LCS) of the first `i` elements of `a` and the first `j` elements of `b`. The values of `a` and `b` remain unchanged.
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
        
    #State: `i` is 0, `j` is 0, `l` contains the characters of the longest common subsequence (LCS) of `a` and `b` in reverse order.
    s = ''.join(l)
    return s[::-1]
    #The program returns the longest common subsequence (LCS) of `a` and `b` as a string, in the correct order.
#Overall this is what the function does:The function `func_22` accepts two parameters `a` and `b`, which are lists of integers or characters, and returns the longest common subsequence (LCS) of `a` and `b` as a string, in the correct order. The values of `a` and `b` remain unchanged after the function call.

#State of the program right berfore the function call: arr is a list of integers.
def func_23(arr):
    l = []
    for i in arr:
        pos = bisect_left(l, i)
        
        if pos == len(l):
            l.append(i)
        else:
            l[pos] = i
        
    #State: `l` is a list containing the elements of `arr` in non-decreasing order, and it represents the longest increasing subsequence that can be formed from `arr`.
    return len(l)
    #The program returns the length of the longest increasing subsequence that can be formed from `arr`.
#Overall this is what the function does:The function `func_23` accepts a list of integers `arr` and returns the length of the longest increasing subsequence that can be formed from `arr`. The function modifies a local list `l` to contain elements from `arr` in non-decreasing order, which represents the longest increasing subsequence. The final state of the program after the function concludes is that `l` contains the elements of the longest increasing subsequence, and the function returns the length of this list.

#State of the program right berfore the function call: ver is an integer representing a vertex in a graph, and graph is a dictionary or list of lists where each element is a list of integers representing the vertices connected to the corresponding vertex. vis is a list of integers where vis[i] is 1 if vertex i has been visited, and 0 otherwise.
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
        
    #State: The `stack` is empty, `ver` is the last vertex that was popped from the stack and printed, and `vis` contains 1s for all vertices that were visited during the loop execution.
#Overall this is what the function does:The function `func_24` accepts a vertex `ver` and performs a depth-first search (DFS) starting from `ver` in a graph represented by `graph`. It prints each visited vertex and marks it as visited in the `vis` list. After the function concludes, the `stack` is empty, `ver` is the last vertex that was processed, and `vis` contains 1s for all vertices that were visited during the search. The function does not return any value.

#State of the program right berfore the function call: ver is a non-negative integer representing a vertex in a graph, and graph is a dictionary or list of lists where each element represents the adjacency list of a vertex. vis is a list of integers where vis[i] is 0 if the vertex i has not been visited, and 1 if it has been visited.
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
        
    #State: - The loop will print all vertices in the graph that are reachable from the starting vertex `ver` in the order they are visited.
    #   - The deque `q` will be empty after the loop finishes because all reachable vertices have been processed.
    #   - The list `vis` will have 1s for all vertices that have been visited and 0s for any vertices that were not reachable from the starting vertex.
    #
    #Given the initial state and the loop code, the output state can be described as follows:
    #
    #Output State:
#Overall this is what the function does:The function `func_25` performs a breadth-first search (BFS) starting from the vertex `ver` in a graph represented by `graph`. It prints each vertex in the order it is visited and updates the `vis` list to mark vertices as visited (1) or not visited (0). After the function concludes, all vertices reachable from `ver` will have been printed, and the `vis` list will reflect the visited status of each vertex. The function does not return any value.

