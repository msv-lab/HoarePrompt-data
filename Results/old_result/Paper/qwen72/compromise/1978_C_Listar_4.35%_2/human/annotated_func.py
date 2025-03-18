#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
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
        
    #State: `n` remains the same, `k` is reduced to a value that satisfies the loop conditions, and `l` is a modified list with elements rearranged.
#Overall this is what the function does:The function `func_1` accepts two integer parameters `n` and `k`, where `1 <= n <= 2 * 10^5` and `0 <= k <= 10^12`. It modifies a list `l` of integers from 1 to `n` by rearranging its elements based on the value of `k`. The function returns the modified list `l` after performing the rearrangement. The final state of the program is that `n` remains unchanged, `k` is reduced through the loop, and `l` is a list with elements rearranged according to the specified logic.

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
    #State: *`n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is equal to (n^2 - 1) // 2. If `n` is even, `max_k` is equal to n^2 // 2.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: `n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is equal to (n^2 - 1) // 2. If `n` is even, `max_k` is equal to n^2 // 2. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the integers `n` and `k`, where `n` is an integer between 1 and 200,000 (inclusive), and `k` is an even integer between 0 and 1,000,000,000,000 (inclusive). Additionally, if `n` is odd, `max_k` is equal to (n^2 - 1) // 2, and if `n` is even, `max_k` is equal to n^2 // 2, with `max_k` being greater than or equal to `k`.
#Overall this is what the function does:The function `func_2` reads two integers, `n` and `k`, from user input where `1 <= n <= 200,000` and `0 <= k <= 1,000,000,000,000`. It returns `0, 0` if `k` is odd or if `k` is greater than the maximum allowed value (`max_k`). If `k` is even and within the allowed range, it returns the original values of `n` and `k`. The maximum allowed value of `k` (`max_k`) is calculated as `(n^2 - 1) // 2` if `n` is odd, or `n^2 // 2` if `n` is even.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n where 1 ≤ n ≤ 2 · 10^5, and the Manhattan value of the permutation is equal to k.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The elements of the list l are printed in the same order as they appear in the list, separated by spaces. The list l remains unchanged.
    print()
    #This is printed: (a blank line)
    return
    #The program returns nothing, but the elements of the list 'l' are printed in the same order as they appear in the list, separated by spaces. The list 'l' remains unchanged.
#Overall this is what the function does:The function `func_3` accepts a list `l` of integers representing a permutation. It prints "YES" followed by the elements of the list `l` in the same order, separated by spaces. It then prints a blank line. The function does not return any value, and the list `l` remains unchanged.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: *`n` and `k` are updated to the values returned by `func_2()`. The new values of `n` and `k` are unknown, but they still satisfy the conditions 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12. Additionally, `n` is not equal to 0.
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns nothing. It retrieves two integers `n` and `k` from the function `func_2`. If `n` is 0, it prints 'NO' and exits. Otherwise, it calls `func_1` with `n` and `k` as arguments, and then calls `func_3` with the result of `func_1`. The final state of the program is that `func_4` has either printed 'NO' and returned, or it has called `func_1` and `func_3` without printing anything.

