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
        
    #State: The list `l` is modified such that the last element is moved to the position `-k` (if `1 + i > k`) or to the beginning of the list (if `1 + i <= k`). The loop terminates after the first iteration where `1 + i > k` or when `k` becomes 0. The final value of `k` is 0, and the final value of `n` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is a positive integer (1 ≤ n ≤ 2 · 10^5) and `k` is a non-negative integer (0 ≤ k ≤ 10^12). It returns a modified list `l` that initially contains integers from 1 to `n` in ascending order. The function modifies `l` by moving the last element to a new position based on the value of `k`. If `k` is 0 at any point during the loop, the function returns `l` immediately. If `1 + i > k` for any iteration, the last element is moved to the position `-k` in the list and the function returns `l`. Otherwise, the last element is moved to the beginning of the list, and `k` is updated. The function continues this process until `k` becomes 0 or the loop completes. The final value of `k` is 0, and the final value of `n` remains unchanged.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_2():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0.
    #State: `n` and `k` are integers provided by the user, such that 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are integers provided by the user, such that 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is equal to (n^2 - 1) // 2. If `n` is even, `max_k` is equal to `n` squared divided by 2.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: *`n` and `k` are integers provided by the user, such that 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is equal to (n^2 - 1) // 2. If `n` is even, `max_k` is equal to `n` squared divided by 2. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the integers `n` and `k`, where `n` is an integer between 1 and 200,000 (inclusive), and `k` is an even integer between 0 and 1,000,000,000,000 (inclusive). Additionally, if `n` is odd, `max_k` is equal to (n^2 - 1) // 2, and if `n` is even, `max_k` is equal to n^2 / 2, with `max_k` being greater than or equal to `k`.
#Overall this is what the function does:The function `func_2` reads two integers `n` and `k` from user input, where `1 <= n <= 200,000` and `0 <= k <= 1,000,000,000,000`. If `k` is odd, the function returns `(0, 0)`. If `k` is even, it calculates `max_k` based on the parity of `n`: if `n` is odd, `max_k = (n^2 - 1) // 2`; if `n` is even, `max_k = n^2 // 2`. If `max_k` is less than `k`, the function returns `(0, 0)`. Otherwise, it returns the original values of `n` and `k`.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where n is a positive integer.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The list l remains unchanged, and the integers in l are printed in the same order as they appear in the list, separated by spaces.
    print()
    #This is printed: (an empty line)
    return
    #The program returns None, and the integers in list 'l' are printed in the same order as they appear in the list, separated by spaces.
#Overall this is what the function does:The function `func_3` accepts a list `l` of integers representing a permutation of length `n`, prints "YES" followed by the integers in the list in the same order, separated by spaces, and then prints an empty line. The function returns `None`, and the list `l` remains unchanged.

#State of the program right berfore the function call: n and k are non-negative integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: *`n` and `k` are assigned the values returned by `func_2()`. The returned values are non-negative integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12. `n` is not equal to 0.
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_4` does not accept any parameters and does not return any value. It retrieves two non-negative integers `n` and `k` from the function `func_2()`, where `1 <= n <= 2 * 10^5` and `0 <= k <= 10^12`. If `n` is 0, it prints 'NO' and terminates. Otherwise, it calls `func_1` with `n` and `k` as arguments, and then passes the result of `func_1` to `func_3`. The function ultimately has no return value.

