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
        
    #State: The loop has completed all iterations, and the list `l` is now a permutation of the integers from 1 to `n` inclusive, with the last element of the list `l` being moved to the front of the list `k // 2` times, and `k` is now 0.
#Overall this is what the function does:The function `func_1` takes two parameters, `n` and `k`, where `n` is a positive integer (1 ≤ n ≤ 2 · 10^5) and `k` is a non-negative integer (0 ≤ k ≤ 10^12). It returns a list `l` of integers from 1 to `n` inclusive, modified based on the value of `k`. If `k` is 0, the list `l` remains unchanged and contains integers from 1 to `n` in ascending order. If `k` is not 0, the function repeatedly moves the last element of the list `l` to a new position in the list, either at the front or at a specific index determined by `k`, until `k` is reduced to 0. The final state of the list `l` is a permutation of the integers from 1 to `n` inclusive, with the last element of the list being moved to the front or a specific position in the list `k // 2` times.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_2():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0.
    #State: `n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is equal to (n^2 - 1) // 2. If `n` is even, `max_k` is equal to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: *`n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is equal to (n^2 - 1) // 2. If `n` is even, `max_k` is equal to `n`. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the values of `n` and `k`, where `n` is an integer between 1 and 200,000 (inclusive) and `k` is an even integer between 0 and 1,000,000,000,000 (inclusive). If `n` is odd, `k` is guaranteed to be less than or equal to \((n^2 - 1) // 2\). If `n` is even, `k` is guaranteed to be less than or equal to `n`.
#Overall this is what the function does:The function `func_2` reads two integers `n` and `k` from user input, where `1 <= n <= 2 * 10^5` and `0 <= k <= 10^12`. It returns `0, 0` if `k` is odd or if `k` is greater than the maximum allowed value based on `n`. If `k` is even and within the allowed range, it returns the values of `n` and `k`. The maximum allowed value for `k` is \((n^2 - 1) // 2\) if `n` is odd, and `n` if `n` is even.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where n is a positive integer.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: `l` is a list of integers representing a permutation of length `n` where `n` is a positive integer, and all elements in `l` have been printed in the order they appear in the list.
    print()
    #This is printed: (a blank line)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_3` accepts a list `l` of integers representing a permutation of length `n`, where `n` is a positive integer. It prints "YES" followed by the elements of `l` in the order they appear, separated by spaces, and then prints a blank line. The function does not return any value. After the function concludes, the list `l` remains unchanged.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: *`n` and `k` are the values returned by `func_2()`, and `n` is not equal to 0
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns nothing. It retrieves two integers `n` and `k` from the function `func_2`. If `n` is 0, it prints 'NO' and exits. Otherwise, it calls `func_1` with `n` and `k` as arguments, and then calls `func_3` with the result of `func_1`. The function does not modify any global state or return any values.

