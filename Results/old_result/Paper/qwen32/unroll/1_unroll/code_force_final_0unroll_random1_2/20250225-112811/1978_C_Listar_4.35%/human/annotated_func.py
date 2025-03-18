#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
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
        
    #State: the list `l` with elements rearranged based on the value of `k` after it has been halved, until `k` becomes `0`.
#Overall this is what the function does:The function `func_1` takes a positive integer `n` and a non-negative integer `k`, and returns a rearranged list of integers from 1 to `n` based on the value of `k` after it has been halved. The rearrangement involves moving the last element of the list to a specific position determined by the value of `k`, potentially multiple times, until `k` is reduced to 0.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 ⋅ 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_2():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is the first input integer, `k` is the second input integer, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: `n` is the first input integer and `k` is the second input integer, where `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns (0, 0)
    #State: `n` is the first input integer and `k` is the second input integer, where `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`. Additionally, `max_k` is not less than `k`.
    return n, k
    #The program returns the tuple (n, k) where n is the first input integer and k is the second input integer, which is even.
#Overall this is what the function does:The function accepts two parameters, `n` (a positive integer) and `k` (a non-negative integer). It returns `(0, 0)` if `k` is odd or if `k` exceeds the maximum possible value for `k` based on `n`. If `k` is even and does not exceed the maximum possible value, it returns the tuple `(n, k)`.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where each integer is distinct and in the range from 1 to n.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The integers in the list l are printed in the same order as they appear in the list, separated by spaces.
    print()
    #This is printed: (newline)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_3` accepts a list of integers `l` representing a permutation of length `n`, where each integer is distinct and in the range from 1 to `n`. It prints "YES" followed by the integers in the list `l` in the same order, separated by spaces, and then prints a newline. The function returns nothing.

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 * 10^5, and k is a non-negative integer such that 0 <= k <= 10^12.
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing (None)
    #State: `n` and `k` are the values returned by `func_2()`. `n` is not equal to 0.
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_4` retrieves two values, `n` and `k`, from `func_2()`. If `n` is 0, it prints 'NO' and returns nothing. Otherwise, it calls `func_1(n, k)` to get a list `l`, then calls `func_3(l)`, and finally returns nothing.

