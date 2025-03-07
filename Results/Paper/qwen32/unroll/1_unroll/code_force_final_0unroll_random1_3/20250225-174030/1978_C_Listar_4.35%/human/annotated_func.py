#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5) and k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_1(n, k):
    k = k // 2
    l = list(range(1, n + 1))
    for i in range(n - 1, -1, -1):
        if k == 0:
            return l
        
        if 1 + i > k:
            x = l[-1]
            l.pop(-1)
            l.insert(-k, x)
            return l
        
        k = k - i + 1
        
        x = l[-1]
        
        l.pop(-1)
        
        l.insert(0, x)
        
    #State: l is a rotated version of the initial list based on the value of k.
#Overall this is what the function does:The function `func_1` takes two parameters, `n` and `k`, where `n` is a positive integer and `k` is a non-negative integer. It returns a list that is a rotated version of the list `[1, 2, ..., n]` based on the value of `k`. The rotation is determined by a specific algorithm that manipulates the list elements according to the value of `k`.

#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer such that 0 <= k <= (n^2 // 2) if n is even, and 0 <= k <= ((n^2 - 1) // 2) if n is odd.
def func_2():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is a positive integer, `k` is a non-negative integer such that 0 <= k <= (n^2 // 2) if n is even, and 0 <= k <= ((n^2 - 1) // 2) if n is odd. Additionally, `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: `n` is a positive integer, `k` is a non-negative integer such that 0 <= k <= ((n^2 - 1) // 2) if `n` is odd, and 0 <= k <= (n^2 // 2) if `n` is even. Additionally, `k` is even. `max_k` is set to ((n^2 - 1) // 2) if `n` is odd, and `max_k` is set to (n^2 // 2) if `n` is even.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is a positive integer, `k` is a non-negative integer such that 0 <= k <= ((n^2 - 1) // 2) if `n` is odd, and 0 <= k <= (n^2 // 2) if `n` is even. Additionally, `k` is even. `max_k` is set to ((n^2 - 1) // 2) if `n` is odd, and `max_k` is set to (n^2 // 2) if `n` is even. `k` is less than or equal to `max_k`.
    return n, k
    #The program returns the positive integer `n` and the non-negative even integer `k` where `k` is less than or equal to `max_k`. `max_k` is set to ((n^2 - 1) // 2) if `n` is odd, and `max_k` is set to (n^2 // 2) if `n` is even.
#Overall this is what the function does:The function accepts two integers, `n` (a positive integer) and `k` (a non-negative integer). It returns `0, 0` if `k` is odd or if `k` exceeds the maximum allowed value `max_k`. Otherwise, it returns `n` and `k`, where `k` is a non-negative even integer and `k` is less than or equal to `max_k`. The value of `max_k` is calculated as ((n^2 - 1) // 2) if `n` is odd, and (n^2 // 2) if `n` is even.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where each integer is distinct and in the range from 1 to n.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: the integers in the list l are printed in the same order, separated by spaces.
    print()
    #This is printed: (newline)
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function accepts a list `l` of integers representing a permutation of length `n`, where each integer is distinct and in the range from 1 to `n`. It prints the integers in the list in the same order, separated by spaces, followed by a newline. The function returns nothing (None).

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5) and k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing (None)
    #State: `n` and `k` are the return values of `func_2()`. `n` is not equal to 0.
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_4` retrieves values `n` and `k` from `func_2`. If `n` is 0, it prints 'NO' and returns `None`. Otherwise, it processes `n` and `k` through `func_1` to get a list `l`, then passes `l` to `func_3`. The function `func_4` returns `None` in all cases.

