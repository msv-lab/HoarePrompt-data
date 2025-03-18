#State of the program right berfore the function call: None of the variables are passed to the function, as it reads input directly from the user.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains the integers obtained from the user input, where the input is split by spaces.
#Overall this is what the function does:The function `func_1` reads a line of input from the user, splits the input by spaces, converts each split element to an integer, and returns a map object containing these integers. The function does not modify any external variables or state. After the function concludes, the user has a map object that can be iterated over to access the integers.

#State of the program right berfore the function call: None of the variables are passed to the function. The function reads input from the standard input, which is expected to be a space-separated list of integers.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers, where each integer is converted from the space-separated list of integers provided by the user through standard input.
#Overall this is what the function does:The function reads a space-separated list of integers from the standard input and returns a list of integers, where each integer is converted from the input string. The function does not modify any external variables or state.

#State of the program right berfore the function call: n is a non-negative integer, v is a value of any type.
def func_3(n, v):
    return [v for i in range(n)]
    #The program returns a list containing `n` elements, where each element is the value `v`.
#Overall this is what the function does:The function `func_3` accepts a non-negative integer `n` and a value `v` of any type. It returns a list containing `n` elements, where each element is the value `v`. The function does not modify any input parameters.

#State of the program right berfore the function call: n and m are non-negative integers, and v is a value of any type.
def func_4(n, m, v):
    return [[v for i in range(m)] for i in range(n)]
    #The program returns a list of n lists, where each of the n lists contains m occurrences of the value v.
#Overall this is what the function does:The function `func_4` accepts three parameters: `n`, `m`, and `v`, where `n` and `m` are non-negative integers and `v` is a value of any type. It returns a list containing `n` sublists, each of which contains `m` occurrences of the value `v`. The function does not modify any of its input parameters.

#State of the program right berfore the function call: n and m are non-negative integers such that n represents the number of sides of a regular polygon and m represents the number of chosen vertices or edges (it's not clear from the function signature alone, but typically m would be less than or equal to n).
def func_5(n, m):
    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x].append(y)
        
        l[y].append(x)
        
    #State: `n` and `m` remain unchanged; `l` is a list of `n + 1` lists where each list contains integers that represent the vertices or edges connected to the corresponding index. The total number of elements in all lists combined is `2 * m` because each connection is added to two lists.
    return l
    #The program returns `l`, which is a list of `n + 1` lists. Each of these lists contains integers representing the vertices or edges connected to the corresponding index. The total number of elements across all lists in `l` is `2 * m`, reflecting that each connection is counted twice, once in each of the two lists it connects.
#Overall this is what the function does:The function `func_5` accepts two parameters, `n` and `m`, where `n` is a non-negative integer representing the number of sides of a regular polygon, and `m` is a non-negative integer representing the number of connections to be made. The function returns a list `l` of `n + 1` lists, where each inner list contains integers representing the vertices or edges connected to the corresponding index. The total number of elements across all lists in `l` is `2 * m`, indicating that each connection is counted twice, once in each of the two lists it connects. The original values of `n` and `m` remain unchanged.

#State of the program right berfore the function call: n is an integer such that 4 <= n <= 10^9, and m is an integer such that 2 <= m <= min(n, 2 * 10^5).
def func_6(n, m):
    l = [[(0) for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x][y] = 1
        
        l[y][x] = 1
        
    #State: `n` is an integer such that 4 <= n <= 10^9, `m` is an integer such that 2 <= m <= min(n, 2 * 10^5), `l` is a 2D list of size (n + 1) x (n + 1) with all elements set to 0 except for the elements at positions (x, y) and (y, x) for each pair (x, y) returned by `func_1()` during the loop, which are set to 1.
    return l
    #The program returns a 2D list `l` of size (n + 1) x (n + 1) where all elements are initially set to 0. For each pair (x, y) returned by `func_1()` during the loop, the elements at positions (x, y) and (y, x) in the list `l` are set to 1.
#Overall this is what the function does:The function `func_6` accepts two integers `n` and `m` and returns a 2D list `l` of size (n + 1) x (n + 1) initialized to 0. For each of the `m` iterations, it calls `func_1()` to get a pair of integers (x, y), and sets the elements at positions (x, y) and (y, x) in the list `l` to 1. After the function concludes, the list `l` contains 1s at the specified positions and 0s elsewhere.

#State of the program right berfore the function call: l is a list of integers.
def func_7(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    #State: `l` is a list of integers, `d` is a dictionary where each key is an integer from the list `l` and each value is the count of how many times that integer appears in the list `l`.
    return d
    #The program returns the dictionary `d` where each key is an integer from the list `l` and each value is the count of how many times that integer appears in the list `l`.
#Overall this is what the function does:The function `func_7` accepts a list of integers `l` and returns a dictionary `d` where each key is an integer from the list `l`, and each value is the count of how many times that integer appears in the list `l`. The input list `l` remains unchanged after the function call.

#State of the program right berfore the function call: l is a 2D list of integers, where each sublist has the same length.
def func_8(l):
    n = len(l)
    m = len(l[0])
    p = [[(0) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
        
    #State: `p` is a 2D list of integers with dimensions `(n + 1) x (m + 1)`, where `p[i][j]` contains the sum of all elements in the submatrix of `l` from the top-left corner `(0, 0)` to the position `(i-1, j-1)`. The values of `n` and `m` remain unchanged.
    return p
    #The program returns the 2D list `p` of integers with dimensions `(n + 1) x (m + 1)`, where each element `p[i][j]` contains the sum of all elements in the submatrix of `l` from the top-left corner `(0, 0)` to the position `(i-1, j-1)`. The values of `n` and `m` remain unchanged.
#Overall this is what the function does:The function `func_8` accepts a 2D list `l` of integers, where each sublist has the same length. It returns a 2D list `p` of integers with dimensions `(n + 1) x (m + 1)`, where `n` is the number of rows in `l` and `m` is the number of columns in `l`. Each element `p[i][j]` in the returned list contains the sum of all elements in the submatrix of `l` from the top-left corner `(0, 0)` to the position `(i-1, j-1)`. The original list `l` remains unchanged.

#State of the program right berfore the function call: x is a positive integer such that 2 <= x <= 2 * 10^5.
def func_9(x):
    return max(1 - (x & x - 1), 0)
    #The program returns 1 if x is a power of 2, otherwise it returns 0.
#Overall this is what the function does:The function `func_9` accepts a positive integer `x` within the range 2 to 2 * 10^5. It returns 1 if `x` is a power of 2, and 0 otherwise.

#State of the program right berfore the function call: l is a list of integers.
def func_10(l):
    a = 0
    for i in l:
        a = gcd(a, i)
        
    #State: `a` is the greatest common divisor (GCD) of all integers in the list `l`.
    return a
    #The program returns the greatest common divisor (GCD) of all integers in the list `l`.
#Overall this is what the function does:The function `func_10` accepts a list `l` of integers and returns the greatest common divisor (GCD) of all the integers in the list. After the function concludes, the list `l` remains unchanged, and the returned value `a` is the GCD of the integers in `l`.

#State of the program right berfore the function call: num is a non-negative integer such that 1 <= num <= 10^9.
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
        
    #State: `prime` is a list where `prime[i]` is `True` if `i` is a prime number and `False` otherwise, `Highest_Prime` is a list where `Highest_Prime[i]` is the highest prime factor of `i`, `Lowest_Prime` is a list where `Lowest_Prime[i]` is the lowest prime factor of `i`, and `p` is `num + 1`.
    p = []
    for i in range(num + 1):
        if prime[i]:
            p.append(i)
        
    #State: `p` is a list containing all the prime numbers up to and including `num`, while the values of `prime`, `Highest_Prime`, and `Lowest_Prime` remain unchanged.
    return p
    #The program returns the list `p` containing all the prime numbers up to and including `num`. The values of `prime`, `Highest_Prime`, and `Lowest_Prime` remain unchanged.
#Overall this is what the function does:The function `func_11` accepts a non-negative integer `num` (1 <= num <= 10^9) and returns a list `p` containing all the prime numbers up to and including `num`. The function internally generates three lists: `prime`, `Highest_Prime`, and `Lowest_Prime`. The `prime` list indicates whether each number up to `num` is a prime number, `Highest_Prime` contains the highest prime factor for each number, and `Lowest_Prime` contains the lowest prime factor for each number. These internal lists are not returned or modified after the function concludes.

#State of the program right berfore the function call: num is a positive integer, and Prime_array is a list or dictionary where keys are integers and values are their smallest prime factors, such that Prime_array[num] is defined and num can be reduced to 1 by repeatedly dividing it by its smallest prime factor found in Prime_array.
def func_12(num, Prime_array):
    d = {}
    while num != 1:
        x = Prime_array[num]
        
        d[x] = d.get(x, 0) + 1
        
        num //= x
        
    #State: `num` is 1, and `d` is a dictionary where each key is a prime factor of the initial `num`, and the value associated with each key is the count of how many times that prime factor divides the initial `num`.
    return d
    #The program returns an empty dictionary `d` because the initial `num` is 1, which has no prime factors.
#Overall this is what the function does:The function `func_12` accepts a positive integer `num` and a dictionary `Prime_array` where keys are integers and values are their smallest prime factors. It returns a dictionary `d` where each key is a prime factor of the initial `num`, and the value associated with each key is the count of how many times that prime factor divides the initial `num`. If `num` is 1, the function returns an empty dictionary.

#State of the program right berfore the function call: n is a positive integer such that 4 <= n <= 10^9.
def func_13(n):
    d = {}
    x = 2
    while x * x <= n:
        while n % x == 0:
            d[x] = d.get(x, 0) + 1
            n //= x
        
        x += 1
        
    #State: `n` is the largest prime factor of the initial `n`, `d` is a dictionary containing the prime factors of the initial `n` and their respective counts, and `x` is the smallest integer greater than the square root of the initial `n` that is also greater than the largest prime factor of `n`.
    if (n > 1) :
        d[n] = d.get(n, 0) + 1
    #State: *`n` is the largest prime factor of the initial `n`, `d` is a dictionary containing the prime factors of the initial `n` and their respective counts, and `x` is the smallest integer greater than the square root of the initial `n` that is also greater than the largest prime factor of `n`. If `n` > 1, the count of the largest prime factor `n` in the dictionary `d` is increased by 1. If `n` is not greater than 1, the values of `n`, `d`, and `x` remain unchanged.
    return d
    #The program returns the dictionary `d` containing the prime factors of the initial `n` and their respective counts, with the count of the largest prime factor `n` increased by 1 if `n` > 1. If `n` is not greater than 1, the dictionary `d` remains unchanged.
#Overall this is what the function does:The function `func_13` accepts a positive integer `n` (4 <= n <= 10^9) and returns a dictionary `d` containing the prime factors of `n` and their respective counts. After the function concludes, `d` will include all prime factors of the initial `n` and their counts. If `n` is greater than 1 after the factorization process, the count of the largest prime factor in `d` is increased by 1. If `n` is not greater than 1, the dictionary `d` remains unchanged.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are positive integers.
def func_14(d):
    s = 0
    for i in d:
        s += pow(i, d[i] - 1) * (i - 1)
        
    #State: `s` is the sum of `pow(i, d[i] - 1) * (i - 1)` for each key `i` in the dictionary `d`.
    return s
    #The program returns the sum of `pow(i, d[i] - 1) * (i - 1)` for each key `i` in the dictionary `d`.
#Overall this is what the function does:The function `func_14` accepts a dictionary `d` where keys are integers and values are positive integers. It calculates the sum of `i` raised to the power of `d[i] - 1`, multiplied by `i - 1`, for each key `i` in the dictionary `d`. The function returns this sum.

#State of the program right berfore the function call: n is a non-negative integer, and mod is a positive integer.
def func_15(n, mod):
    f = [1]
    for i in range(1, n + 1):
        f.append(f[i - 1] * i % mod % mod)
        
    #State: `n` is a non-negative integer, `mod` is a positive integer, `f` is a list containing `n + 1` integers where each element `f[i]` is the result of `(i! % mod) % mod` for `i` ranging from 0 to `n`.
    return f
    #The program returns a list `f` containing `n + 1` integers, where each element `f[i]` is the result of `(i! % mod) % mod` for `i` ranging from 0 to `n`.
#Overall this is what the function does:The function `func_15` accepts two parameters, `n` and `mod`, where `n` is a non-negative integer and `mod` is a positive integer. It returns a list `f` of `n + 1` integers, where each element `f[i]` is the factorial of `i` modulo `mod`. The final state of the program is that `f` contains the computed factorials modulo `mod` for all integers from 0 to `n`.

#State of the program right berfore the function call: n is a positive integer, and mod is an integer that can be -1 or a positive integer.
def func_16(n, mod):
    if (mod == -1) :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) * (dearr[i - 1] + dearr[i - 2]))
            
        #State: Output State: `n` is a positive integer, `mod` is -1, `dearr` is a list containing the first `n+1` terms of the derangement sequence.
    else :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod)
            
        #State: `dearr` is a list containing the first `n + 1` elements of a sequence where each element is calculated as `(i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod` for `i` from 2 to `n`, and `n` and `mod` remain unchanged.
    #State: *`n` is a positive integer, and `mod` is an integer that can be -1 or a positive integer. If `mod` is -1, `dearr` is a list containing the first `n+1` terms of the derangement sequence. Otherwise, `dearr` is a list containing the first `n + 1` elements of a sequence where each element is calculated as `(i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod` for `i` from 2 to `n`, and `n` and `mod` remain unchanged.
    return dearr
    #The program returns the list `dearr` which contains the first `n+1` terms of either the derangement sequence if `mod` is -1, or a custom sequence where each element is calculated as `(i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod` for `i` from 2 to `n`, depending on the value of `mod`. The values of `n` and `mod` remain unchanged.
#Overall this is what the function does:The function `func_16` accepts two parameters, `n` (a positive integer) and `mod` (an integer that can be -1 or a positive integer). It returns a list `dearr` containing the first `n+1` terms of a sequence. If `mod` is -1, the sequence is the derangement sequence. If `mod` is a positive integer, each term in the sequence is calculated as `(i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod` for `i` from 2 to `n`. The values of `n` and `mod` remain unchanged after the function execution.

#State of the program right berfore the function call: p is a sorted list of distinct integers, and x is an integer.
def func_17(p, x):
    i = bisect_left(p, x)
    if (i != len(p) and p[i] == x) :
        return i
        #The program returns the index `i` of the first element in the sorted list `p` that is equal to the integer `x`.
    else :
        return -1
        #The program returns -1.
#Overall this is what the function does:The function `func_17` accepts a sorted list `p` of distinct integers and an integer `x`. It returns the index of the first occurrence of `x` in `p` if `x` is found; otherwise, it returns -1. After the function concludes, the input list `p` remains unchanged, and the integer `x` is not modified.

#State of the program right berfore the function call: p is a list of distinct integers sorted in non-decreasing order, and x is an integer such that p[0] <= x <= p[-1].
def func_18(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[0] > x) :
        return -1
        #The program returns -1.
    #State: *`p` is a list of distinct integers sorted in non-decreasing order, `x` is an integer such that `p[0] <= x <= p[-1]`, `n` is the length of the list `p`, `l` is 0, `r` is `n - 1`, and `p[0]` is less than or equal to `x`
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
        
    #State: `l` is the smallest index such that `p[l] > x`, or `l` is `n` if `x` is greater than or equal to all elements in `p`. `r` is the largest index such that `p[r] <= x`, or `r` is `l - 1` if `l` is `n`. `mid` is the index of the last element checked, which is either the largest index such that `p[mid] <= x` or `n - 1` if `x` is greater than or equal to all elements in `p`.
    return mid
    #The program returns the index of the last element checked, which is either the largest index such that `p[mid] <= x` or `n - 1` if `x` is greater than or equal to all elements in `p`.
#Overall this is what the function does:The function `func_18` accepts a sorted list of distinct integers `p` and an integer `x` within the range of `p`. It returns `-1` if `x` is less than the smallest element in `p`. Otherwise, it returns the index of the largest element in `p` that is less than or equal to `x`, or the last index of the list if `x` is greater than or equal to all elements in `p`.

#State of the program right berfore the function call: p is a list of distinct integers sorted in non-decreasing order, and x is an integer such that the elements in p are in the range from 1 to n, where n is the number of sides of the polygon.
def func_19(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[-1] < x) :
        return n
        #The program returns the length of the list `p`
    #State: `p` is a list of distinct integers sorted in non-decreasing order, `x` is an integer such that the elements in `p` are in the range from 1 to `n`, `n` is the length of `p`, `l` is 0, `r` is `n - 1`, and the last element of `p` is greater than or equal to `x`.
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
        
    #State: `l` is the smallest index such that `p[l]` is greater than or equal to `x`, `r` is `l - 1`, `mid` is `l`, and `p` and `n` remain unchanged.
    return mid
    #The program returns the smallest index `l` such that `p[l]` is greater than or equal to `x`.
#Overall this is what the function does:The function `func_19` accepts a sorted list of distinct integers `p` and an integer `x`. It returns the length of the list `p` if `x` is greater than the last element in `p`. Otherwise, it returns the smallest index `l` such that `p[l]` is greater than or equal to `x`. The function does not modify the input list `p` or any other variables.

#State of the program right berfore the function call: x is a non-negative integer.
def func_20(x):
    if (x == 0 or x == 1) :
        return x
        #The program returns the value of x, which is either 0 or 1.
    #State: x is a non-negative integer, and x is not equal to 0 or 1.
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
        
    #State: `l` is the largest integer such that `l * l` ≤ `x`, and `r` is `l - 1`.
#Overall this is what the function does:The function `func_20` accepts a non-negative integer `x` and returns the largest integer `l` such that `l * l` is less than or equal to `x`. If `x` is 0 or 1, it returns `x` directly.

#State of the program right berfore the function call: a and b are integers, and mod is a positive integer.
def func_21(a, b, mod):
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        
        a = a * a % mod
        
        b >>= 1
        
    #State: `ans` is `a` raised to the power of `b` (initial value of `b`), modulo `mod`. `a` is the square of its initial value, raised to the power of the number of times `b` was right-shifted, modulo `mod`. `b` is 0.
    return ans
    #The program returns the value of `ans`, which is the result of `a` raised to the power of the initial value of `b`, modulo `mod`. After the calculation, `a` is updated to the square of its initial value, raised to the power of the number of times `b` was right-shifted, modulo `mod`. However, since `b` is 0, the value of `ans` remains the same as the initial calculation.
#Overall this is what the function does:The function `func_21` accepts three parameters: `a`, `b`, and `mod`, where `a` and `b` are integers, and `mod` is a positive integer. It returns the result of `a` raised to the power of `b`, modulo `mod`. The function does not modify the input parameters `a` and `b` outside of the function scope. After the function concludes, the value of `a` within the function is updated to the square of its initial value, raised to the power of the number of times `b` was right-shifted, modulo `mod`, but this updated value is not returned or accessible outside the function. The value of `b` is reduced to 0 during the function's execution. If `b` is 0 initially, the function returns 1 modulo `mod`.

#State of the program right berfore the function call: a and b are lists of integers or characters, and both are non-empty.
def func_22(a, b):
    dp = [([0] * (len(b) + 1)) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
    #State: The `dp` list will contain the lengths of the longest common subsequences (LCS) for all prefixes of `a` and `b`. Specifically, `dp[len(a)][len(b)]` will hold the length of the LCS of the entire lists `a` and `b`. The values of `a` and `b` remain unchanged.
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
        
    #State: `i` is 0, `j` is 0, `l` contains the elements of the longest common subsequence (LCS) of `a` and `b` in reverse order.
    s = ''.join(l)
    return s[::-1]
    #The program returns the string 's' formed by joining the elements of the longest common subsequence (LCS) of `a` and `b` in the correct order.
#Overall this is what the function does:The function `func_22` accepts two non-empty lists `a` and `b` of integers or characters. It computes the longest common subsequence (LCS) of `a` and `b` and returns this LCS as a string `s` in the correct order. The input lists `a` and `b` remain unchanged after the function execution.

#State of the program right berfore the function call: arr is a list of integers.
def func_23(arr):
    l = []
    for i in arr:
        pos = bisect_left(l, i)
        
        if pos == len(l):
            l.append(i)
        else:
            l[pos] = i
        
    #State: `l` is a list containing the elements of `arr` in non-decreasing order, but only the elements that form the longest increasing subsequence of `arr`.
    return len(l)
    #The program returns the length of the longest increasing subsequence of `arr`
#Overall this is what the function does:The function `func_23` accepts a list of integers `arr` and returns the length of the longest increasing subsequence within `arr`. After the function concludes, the list `l` contains the elements of `arr` that form the longest increasing subsequence, in non-decreasing order. The function does not modify the input list `arr`.

#State of the program right berfore the function call: ver is an integer representing a vertex in a graph, and graph is a dictionary or list of lists where each element is a list of integers representing the vertices connected to the corresponding vertex. vis is a list of integers or booleans where vis[i] is 1 or True if vertex i has been visited, and 0 or False otherwise.
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
        
    #State: The `stack` is empty, and the `vis` list has been updated to mark all vertices that were reachable from the initial `ver` as visited (True or 1). The `ver` variable holds the last vertex that was popped from the stack and processed, which is the last vertex printed.
#Overall this is what the function does:The function `func_24` accepts an integer `ver` representing a vertex in a graph. It updates the `vis` list to mark all vertices that are reachable from `ver` as visited (True or 1). The function prints each visited vertex in the order they are processed. After the function concludes, the `stack` is empty, and the `vis` list reflects the visitation status of all reachable vertices from the initial `ver`. The function does not return any value.

#State of the program right berfore the function call: ver is an integer representing a vertex in a graph, and graph and vis are global variables where graph is a dictionary representing an adjacency list of the graph, and vis is a list or dictionary used to track visited vertices.
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
        
    #State: The deque `q` is empty, and the vertices that were processed are printed in the order they were visited. The `vis` list or dictionary has been updated to mark all visited vertices as 1.
#Overall this is what the function does:The function `func_25` performs a breadth-first traversal of a graph starting from the vertex `ver`. It prints each visited vertex in the order they are processed and updates the `vis` variable to mark these vertices as visited (1). The function does not return any value. After the function concludes, the deque `q` is empty, all reachable vertices from `ver` have been printed, and their corresponding entries in `vis` are set to 1.

