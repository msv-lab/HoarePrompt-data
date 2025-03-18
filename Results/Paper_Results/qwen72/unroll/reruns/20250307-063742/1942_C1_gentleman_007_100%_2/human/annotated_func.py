#State of the program right berfore the function call: None of the variables are passed as arguments to the function.
def func_1():
    return map(int, input().split())
    #The program returns an iterator that converts each input string (separated by spaces) into an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an iterator that converts each input string (separated by spaces) into an integer. After the function concludes, the user can iterate over the returned object to access the converted integers.

#State of the program right berfore the function call: None
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers, where each integer is converted from a string input provided by the user, and the strings are separated by spaces.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads a line of input from the user, splits the input into substrings based on spaces, converts each substring into an integer, and returns a list of these integers. The final state of the program after the function concludes is that it has a list of integers derived from the user's input.

#State of the program right berfore the function call: n is a non-negative integer, and v is a value of any type.
def func_3(n, v):
    return [v for i in range(n)]
    #The program returns a list containing `n` elements, each element being the value `v`.
#Overall this is what the function does:The function `func_3` accepts a non-negative integer `n` and a value `v` of any type. It returns a list containing `n` elements, where each element is the value `v`. If `n` is 0, the function returns an empty list.

#State of the program right berfore the function call: n and m are non-negative integers, and v is a value of any type.
def func_4(n, m, v):
    return [[v for i in range(m)] for i in range(n)]
    #The program returns a list of lists, where each inner list contains `m` copies of the value `v`, and there are `n` such inner lists.
#Overall this is what the function does:The function `func_4` accepts three parameters: `n`, `m`, and `v`. It returns a list of `n` inner lists, where each inner list contains `m` copies of the value `v`. The function does not modify the input parameters. After the function concludes, the program state includes the returned list of lists, which can be used for further operations.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, and m is an integer representing the number of edges (diagonals) to be added, where 0 <= m <= n.
def func_5(n, m):
    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x].append(y)
        
        l[y].append(x)
        
    #State: `n` remains the same, `m` is unchanged, and `l` is a list of `n + 1` lists where each list contains the integers that were appended to it during the loop iterations. Each integer `x` and `y` returned by `func_1()` will have `y` appended to `l[x]` and `x` appended to `l[y]`.
    return l
    #The program returns `l`, which is a list of `n + 1` lists. Each of these lists contains integers that were appended to it during the loop iterations. Specifically, for each integer `x` and `y` returned by `func_1()`, `y` is appended to `l[x]` and `x` is appended to `l[y]`.
#Overall this is what the function does:The function `func_5` accepts two integers, `n` and `m`, where `n` is the number of sides of a polygon and `m` is the number of edges (diagonals) to be added, with the constraint 0 <= m <= n. It returns a list `l` of `n + 1` lists. Each sublist in `l` contains integers that were appended to it during the loop iterations. Specifically, for each pair of integers `x` and `y` returned by `func_1()`, `y` is appended to `l[x]` and `x` is appended to `l[y]`. The values of `n` and `m` remain unchanged after the function execution.

#State of the program right berfore the function call: n is an integer such that 4 <= n <= 10^9, and m is an integer such that 0 <= m <= n.
def func_6(n, m):
    l = [[(0) for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x][y] = 1
        
        l[y][x] = 1
        
    #State: n remains an integer such that 4 <= n <= 10^9, m remains an integer such that 0 <= m <= n, l is a 2D list of size (n+1) x (n+1) where l[x][y] and l[y][x] are set to 1 for each (x, y) pair returned by func_1() during the m iterations. All other elements in l remain 0.
    return l
    #The program returns a 2D list `l` of size (n+1) x (n+1), where `l[x][y]` and `l[y][x]` are set to 1 for each (x, y) pair returned by `func_1()` during the m iterations. All other elements in `l` remain 0.
#Overall this is what the function does:The function `func_6` accepts two integers `n` and `m`, where `4 <= n <= 10^9` and `0 <= m <= n`. It returns a 2D list `l` of size `(n+1) x (n+1)`, where the elements at positions `(x, y)` and `(y, x)` are set to 1 for each `(x, y)` pair returned by `func_1()` during the `m` iterations. All other elements in `l` remain 0. The input parameters `n` and `m` are not modified.

#State of the program right berfore the function call: l is a list of integers, where each integer is a vertex number from 1 to n, and the list contains x distinct integers.
def func_7(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    #State: `l` is a list of integers, where each integer is a vertex number from 1 to n, and the list contains x distinct integers. `d` is a dictionary where each key is a distinct integer from the list `l`, and the value associated with each key is the count of how many times that integer appears in the list `l`.
    return d
    #The program returns a dictionary `d` where each key is a distinct integer from the list `l`, and the value associated with each key is the count of how many times that integer appears in the list `l`.
#Overall this is what the function does:The function `func_7` accepts a list `l` of integers, where each integer represents a vertex number from 1 to n, and the list contains x distinct integers. It returns a dictionary `d` where each key is a distinct integer from the list `l`, and the value associated with each key is the count of how many times that integer appears in the list `l`. The original list `l` remains unchanged.

#State of the program right berfore the function call: l is a 2D list of integers, where each sublist has the same length.
def func_8(l):
    n = len(l)
    m = len(l[0])
    p = [[(0) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
        
    #State: `p` is a 2D list of integers where `p[i][j]` contains the cumulative sum of the elements in `l` from the top-left corner (0,0) to the element at position (i-1,j-1), inclusive. The dimensions of `p` remain `(n + 1) x (m + 1)`. The values of `n` and `m` remain unchanged.
    return p
    #The program returns the 2D list `p` of integers, where `p[i][j]` contains the cumulative sum of the elements in `l` from the top-left corner (0,0) to the element at position (i-1,j-1), inclusive. The dimensions of `p` are `(n + 1) x (m + 1)`, and the values of `n` and `m` remain unchanged.
#Overall this is what the function does:The function `func_8` accepts a 2D list `l` of integers, where each sublist has the same length. It returns a 2D list `p` of integers with dimensions `(n + 1) x (m + 1)`, where `n` and `m` are the dimensions of `l`. The value `p[i][j]` contains the cumulative sum of the elements in `l` from the top-left corner (0,0) to the element at position (i-1,j-1), inclusive. The original list `l` remains unchanged.

#State of the program right berfore the function call: x is a non-negative integer such that 2 <= x <= 2 * 10^5.
def func_9(x):
    return max(1 - (x & x - 1), 0)
    #The program returns 1 if `x` is a power of two, otherwise it returns 0.
#Overall this is what the function does:The function `func_9` accepts a non-negative integer `x` within the range 2 to 2 * 10^5. It returns 1 if `x` is a power of two, and 0 otherwise.

#State of the program right berfore the function call: l is a list of positive integers.
def func_10(l):
    a = 0
    for i in l:
        a = gcd(a, i)
        
    #State: `a` is the greatest common divisor (GCD) of all the integers in the list `l`.
    return a
    #The program returns the greatest common divisor (GCD) of all the integers in the list `l`.
#Overall this is what the function does:The function `func_10` accepts a list `l` of positive integers and returns the greatest common divisor (GCD) of all the integers in the list. After the function concludes, the list `l` remains unchanged, and the returned value is the GCD of the integers in `l`.

#State of the program right berfore the function call: num is a non-negative integer such that 0 <= num.
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
        
    #State: `prime` is a list where `prime[i]` is `True` if `i` is a prime number and `False` otherwise, `Highest_Prime` is a list where `Highest_Prime[i]` is the highest prime factor of `i`, and `Lowest_Prime` is a list where `Lowest_Prime[i]` is the lowest prime factor of `i`. The variable `p` is equal to `num + 1`.
    p = []
    for i in range(num + 1):
        if prime[i]:
            p.append(i)
        
    #State: `p` is a list containing all the prime numbers from 0 to `num` (inclusive), and the states of `prime`, `Highest_Prime`, and `Lowest_Prime` remain unchanged.
    return p
    #The program returns the list `p` containing all the prime numbers from 0 to `num` (inclusive).
#Overall this is what the function does:The function `func_11` accepts a non-negative integer `num` and returns a list containing all prime numbers from 0 to `num` (inclusive). It also maintains two additional lists, `Highest_Prime` and `Lowest_Prime`, where `Highest_Prime[i]` is the highest prime factor of `i` and `Lowest_Prime[i]` is the lowest prime factor of `i` for each `i` in the range from 0 to `num`. However, these lists are not returned and are only used internally within the function. The final state of the program includes the returned list of prime numbers, and the internal lists `prime`, `Highest_Prime`, and `Lowest_Prime` are fully populated but not accessible outside the function.

#State of the program right berfore the function call: num is a positive integer greater than 1, and Prime_array is a list or dictionary where keys or indices are integers and values are prime factors of the corresponding key or index.
def func_12(num, Prime_array):
    d = {}
    while num != 1:
        x = Prime_array[num]
        
        d[x] = d.get(x, 0) + 1
        
        num //= x
        
    #State: d is a dictionary where each key is a prime factor of the initial num, and each value is the count of how many times that prime factor appears in the factorization of num. num is 1.
    return d
    #The program returns a dictionary `d` where each key is a prime factor of the initial `num`, and each value is the count of how many times that prime factor appears in the factorization of `num`. Since `num` is 1, the dictionary `d` will be empty.
#Overall this is what the function does:The function `func_12` accepts a positive integer `num` greater than 1 and a list or dictionary `Prime_array` where each key or index represents an integer and its value is the smallest prime factor of that integer. The function returns a dictionary `d` where each key is a prime factor of the initial `num`, and each value is the count of how many times that prime factor appears in the factorization of `num`. The input `num` is reduced to 1 during the function execution, and the final state of the program is that `d` contains the prime factorization of the initial `num` in the form of a dictionary.

#State of the program right berfore the function call: n is a positive integer such that 4 <= n <= 10^9.
def func_13(n):
    d = {}
    x = 2
    while x * x <= n:
        while n % x == 0:
            d[x] = d.get(x, 0) + 1
            n //= x
        
        x += 1
        
    #State: `n` is reduced to its largest prime factor (or 1 if it was a perfect power of a prime), `d` contains the prime factors of the original `n` and their respective powers, `x` is the smallest integer greater than the square root of the original `n` that is not a factor of `n`.
    if (n > 1) :
        d[n] = d.get(n, 0) + 1
    #State: *`n` is reduced to its largest prime factor (or 1 if it was a perfect power of a prime), `d` contains the prime factors of the original `n` and their respective powers, `x` is the smallest integer greater than the square root of the original `n` that is not a factor of `n`. If `n` is greater than 1, the value of `d[n]` is incremented by 1.
    return d
    #The program returns the dictionary `d` which contains the prime factors of the original `n` and their respective powers. If `n` is greater than 1, the value of `d[n]` is incremented by 1.
#Overall this is what the function does:The function `func_13` accepts a positive integer `n` (where 4 <= n <= 10^9) and returns a dictionary `d` containing the prime factors of `n` and their respective powers. After the function concludes, `n` is reduced to its largest prime factor (or 1 if it was a perfect power of a prime), and `d` contains the prime factors of the original `n` and their respective powers. If `n` is greater than 1 after the factorization process, the value of `d[n]` is incremented by 1.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are positive integers.
def func_14(d):
    s = 0
    for i in d:
        s += pow(i, d[i] - 1) * (i - 1)
        
    #State: s is the sum of `pow(i, d[i] - 1) * (i - 1)` for all keys `i` in the dictionary `d`.
    return s
    #The program returns the sum of `pow(i, d[i] - 1) * (i - 1)` for all keys `i` in the dictionary `d`.
#Overall this is what the function does:The function `func_14` accepts a dictionary `d` where the keys are integers and the values are positive integers. It calculates the sum of `i^(d[i] - 1) * (i - 1)` for each key `i` in the dictionary and returns this sum. The dictionary `d` remains unchanged after the function call.

#State of the program right berfore the function call: n is a non-negative integer, and mod is a positive integer.
def func_15(n, mod):
    f = [1]
    for i in range(1, n + 1):
        f.append(f[i - 1] * i % mod % mod)
        
    #State: `n` is a non-negative integer, `mod` is a positive integer, `f` is a list containing the first `n + 1` factorial values modulo `mod`.
    return f
    #The program returns a list `f` containing the first `n + 1` factorial values, each computed modulo `mod`.
#Overall this is what the function does:The function `func_15` accepts two parameters, `n` and `mod`, where `n` is a non-negative integer and `mod` is a positive integer. It returns a list `f` containing the first `n + 1` factorial values, each computed modulo `mod`. After the function concludes, the list `f` will have `n + 1` elements, where each element `f[i]` represents the factorial of `i` (for `i` from 0 to `n`) modulo `mod`.

#State of the program right berfore the function call: n is a positive integer, and mod is an integer which can be -1 or a positive integer.
def func_16(n, mod):
    if (mod == -1) :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) * (dearr[i - 1] + dearr[i - 2]))
            
        #State: Output State: `n` is a positive integer, `mod` is -1, `dearr` is a list with values [1, 0, 1, 2, 9, 44, ...] (the list will have `n+1` elements, where each element is calculated based on the formula `(i - 1) * (dearr[i - 1] + dearr[i - 2])` for `i` from 2 to `n`).
    else :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod)
            
        #State: `n` is a positive integer, `mod` is an integer which can be a positive integer, `dearr` is a list with values [1, 0, (1 * (1 + 0) % mod), (2 * (1 + (1 * (1 + 0) % mod) % mod) % mod), ..., (n-1 * (dearr[n-1] + dearr[n-2]) % mod) % mod].
    #State: *`n` is a positive integer, and `mod` is an integer which can be -1 or a positive integer. If `mod` is -1, `dearr` is a list with `n+1` elements, where each element is calculated based on the formula `(i - 1) * (dearr[i - 1] + dearr[i - 2])` for `i` from 2 to `n`. If `mod` is a positive integer, `dearr` is a list with `n+1` elements, where each element is calculated based on the formula `(i - 1) * (dearr[i - 1] + dearr[i - 2]) % mod` for `i` from 2 to `n`.
    return dearr
    #The program returns the list `dearr` which contains `n+1` elements. If `mod` is -1, each element from index 2 to `n` in `dearr` is calculated as `(i - 1) * (dearr[i - 1] + dearr[i - 2])`. If `mod` is a positive integer, each element from index 2 to `n` in `dearr` is calculated as `(i - 1) * (dearr[i - 1] + dearr[i - 2]) % mod`. The first two elements of `dearr` are 0 and 1, respectively.
#Overall this is what the function does:The function `func_16` accepts two parameters, `n` and `mod`. It returns a list `dearr` with `n+1` elements. The first two elements of `dearr` are 1 and 0, respectively. If `mod` is -1, each subsequent element from index 2 to `n` is calculated as `(i - 1) * (dearr[i - 1] + dearr[i - 2])`. If `mod` is a positive integer, each subsequent element from index 2 to `n` is calculated as `(i - 1) * (dearr[i - 1] + dearr[i - 2]) % mod`. The function does not modify the input parameters `n` or `mod`.

#State of the program right berfore the function call: p is a list of distinct integers sorted in non-decreasing order, x is an integer.
def func_17(p, x):
    i = bisect_left(p, x)
    if (i != len(p) and p[i] == x) :
        return i
        #The program returns the index `i` of the first element in the list `p` that is not less than `x`, and `p[i]` is equal to `x`.
    else :
        return -1
        #The program returns -1.
#Overall this is what the function does:The function `func_17` accepts a sorted list of distinct integers `p` and an integer `x`. It returns the index of the first occurrence of `x` in the list `p` if `x` is present. If `x` is not found in the list, it returns -1.

#State of the program right berfore the function call: p is a list of integers sorted in non-decreasing order, x is an integer such that the elements in p are distinct and within the range from 1 to n, where n is the number of sides of the polygon.
def func_18(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[0] > x) :
        return -1
        #The program returns -1.
    #State: `p` is a list of integers sorted in non-decreasing order, `x` is an integer such that the elements in `p` are distinct and within the range from 1 to `n`, `n` is the length of the list `p`, `l` is 0, `r` is `n - 1`, and the first element of `p` is less than or equal to `x`
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
        
    #State: `l` is the smallest index such that `p[l]` is greater than `x`, or `l` is `n` if all elements in `p` are less than or equal to `x`. `r` is the largest index such that `p[r]` is less than or equal to `x`, or `r` is `l - 1` if `l` is `n`. `mid` is the index of the last element in `p` that is less than or equal to `x`, or `n - 1` if all elements in `p` are less than or equal to `x`.
    return mid
    #The program returns the index of the last element in `p` that is less than or equal to `x`, or `n - 1` if all elements in `p` are less than or equal to `x`.
#Overall this is what the function does:The function `func_18` accepts a sorted list of integers `p` and an integer `x`. If `x` is less than the first element in `p`, the function returns -1. Otherwise, it returns the index of the last element in `p` that is less than or equal to `x`, or `n - 1` if all elements in `p` are less than or equal to `x`.

#State of the program right berfore the function call: p is a list of distinct integers sorted in non-decreasing order, x is an integer such that the minimum value in p <= x <= the maximum value in p.
def func_19(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[-1] < x) :
        return n
        #The program returns the length of the list `p`
    #State: `p` is a list of distinct integers sorted in non-decreasing order, `x` is an integer such that the minimum value in `p` <= `x` <= the maximum value in `p`, `n` is the length of `p`, `l` is 0, `r` is `n - 1`, and the last element of `p` is greater than or equal to `x`.
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
        
    #State: `l` is the smallest index in `p` such that `p[l] >= x`, `r` is `l - 1`, `mid` is `l`, and the values of `p`, `x`, and `n` remain unchanged.
    return mid
    #The program returns the smallest index `l` in list `p` such that `p[l] >= x`.
#Overall this is what the function does:The function `func_19` accepts a sorted list of distinct integers `p` and an integer `x` within the range of the minimum and maximum values in `p`. It returns the length of the list `p` if `x` is greater than the maximum value in `p`. Otherwise, it returns the smallest index `l` in `p` such that `p[l]` is greater than or equal to `x`. The input list `p` and the integer `x` remain unchanged.

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
        
    #State: The loop returns the largest integer `mid` such that `mid * mid` is less than or equal to `x`.
#Overall this is what the function does:The function `func_20` accepts a non-negative integer `x` and returns the largest integer `y` such that `y * y` is less than or equal to `x`. If `x` is 0 or 1, it returns `x` itself.

#State of the program right berfore the function call: a and b are integers, and mod is a positive integer.
def func_21(a, b, mod):
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        
        a = a * a % mod
        
        b >>= 1
        
    #State: `ans` is `a` raised to the power of `b` (initial `b`), modulo `mod`. `a` is the square of the initial `a`, raised to the highest power of 2 that is less than or equal to the initial `b`, modulo `mod`. `b` is 0.
    return ans
    #The program returns the value of `ans`, which is the result of `a` raised to the power of the initial `b`, modulo `mod`.
#Overall this is what the function does:The function `func_21` accepts three parameters: `a`, `b`, and `mod`, where `a` and `b` are integers and `mod` is a positive integer. It returns the result of `a` raised to the power of `b`, modulo `mod`. After the function concludes, the value of `ans` is the result of this computation, and the input parameters `a` and `b` are not modified.

#State of the program right berfore the function call: a and b are lists of integers or characters, and both a and b are non-empty.
def func_22(a, b):
    dp = [([0] * (len(b) + 1)) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
    #State: The `dp` list is updated such that `dp[i][j]` contains the length of the longest common subsequence (LCS) of the first `i` elements of `a` and the first `j` elements of `b`. The values of `a` and `b` remain unchanged.
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
        
    #State: `i` is 0, `j` is 0, and `l` contains the characters of the longest common subsequence (LCS) of `a` and `b` in reverse order.
    s = ''.join(l)
    return s[::-1]
    #The program returns the string formed by joining the characters in `l` in the correct order, which is the longest common subsequence (LCS) of `a` and `b`.
#Overall this is what the function does:The function `func_22` accepts two non-empty lists `a` and `b` of integers or characters. It computes the longest common subsequence (LCS) of `a` and `b` and returns this LCS as a string. The original lists `a` and `b` remain unchanged.

#State of the program right berfore the function call: arr is a list of integers.
def func_23(arr):
    l = []
    for i in arr:
        pos = bisect_left(l, i)
        
        if pos == len(l):
            l.append(i)
        else:
            l[pos] = i
        
    #State: `l` is a list containing the elements of `arr` in non-decreasing order, and the length of `l` is the length of the longest non-decreasing subsequence in `arr`.
    return len(l)
    #The program returns the length of the longest non-decreasing subsequence in the list `arr`.
#Overall this is what the function does:The function `func_23` accepts a list of integers `arr` and returns the length of the longest non-decreasing subsequence in the list. The function does not modify the input list `arr` and the returned value is the length of the longest subsequence where each element is greater than or equal to the previous element.

#State of the program right berfore the function call: ver is an integer representing a vertex in a graph, and graph and vis are not defined within the function but are assumed to be a graph represented as an adjacency list and a list of visited nodes, respectively.
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
        
    #State: The `stack` is empty, and the `vis` list has been updated to mark all reachable nodes from the initial `ver` as visited (value 1). The `graph` remains unchanged. The printed output is a sequence of integers representing the vertices visited in the order they were processed.
#Overall this is what the function does:The function `func_24` accepts an integer `ver` representing a vertex in a graph. It performs a depth-first search (DFS) starting from the vertex `ver`, marking all reachable vertices as visited in the `vis` list and printing them in the order they are processed. The function does not return any value. After the function concludes, the `stack` is empty, the `vis` list has been updated to mark all reachable nodes from the initial `ver` as visited (value 1), and the `graph` remains unchanged. The printed output is a sequence of integers representing the vertices visited.

#State of the program right berfore the function call: ver is an integer representing a vertex in a graph, and graph is a dictionary or list of lists where each element is a list of integers representing the neighbors of the vertex. vis is a list of integers where vis[i] is 1 if vertex i has been visited, and 0 otherwise.
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
        
    #State: - The deque `q` will be empty after the loop finishes, as all elements are popped off and processed.
    #   - The list `vis` will have 1s for all vertices that were visited during the loop.
    #   - The variable `ver` will hold the last vertex that was processed and printed.
    #
    #Given this, the output state after the loop executes all iterations is:
    #
    #Output State:
#Overall this is what the function does:The function `func_25` performs a breadth-first search (BFS) starting from the vertex `ver` in a graph represented by `graph`. It marks each visited vertex in the list `vis` and prints each visited vertex. After the function concludes, the deque `q` is empty, the list `vis` contains 1s for all vertices that were visited, and the variable `ver` holds the last vertex that was processed and printed. The function does not return any value.

