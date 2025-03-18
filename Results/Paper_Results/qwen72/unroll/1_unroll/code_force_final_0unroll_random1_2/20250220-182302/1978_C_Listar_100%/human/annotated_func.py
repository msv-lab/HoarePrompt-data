#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_1(n, k):
    k = k // 2
    l = list(range(1, n + 1))
    c = 0
    for i in range(n, -1, -2):
        c += 1
        
        if k == 0:
            return l
        
        if k < i - 1:
            return func_2(c, k, l)
        
        k = k - i + 1
        
        l = func_3(c, l)
        
    #State: `c` is `(n // 2) + 1` if `n` is odd, or `n // 2` if `n` is even. `k` is the final value after all updates, and `l` is the result of applying `func_3` multiple times.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is a positive integer between 1 and 200,000, and `k` is a non-negative integer up to 1,000,000,000,000. It returns a list `l` which is initially a sequence of integers from 1 to `n`. The function modifies `l` and `k` through a series of operations, and the final state of `l` depends on the value of `k` and the number of iterations. If `k` becomes 0 during the loop, the function returns the current state of `l`. If `k` is less than `i - 1` at any point, the function calls `func_2` and returns its result. Otherwise, it continues to modify `l` using `func_3` and decrements `k` until the loop completes. The final value of `c` is `(n // 2) + 1` if `n` is odd, or `n // 2` if `n` is even, and `k` is the remaining value after all updates.

#State of the program right berfore the function call: c and k are non-negative integers, l is a list of integers of length n, and c + k < len(l).
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` where the integer at index `-c - k` has been assigned to `x` and the integer at index `-c` has been assigned to `y`. The list `l` remains unchanged in length and contains the same integers, but the values at the specified indices have been reassigned.
#Overall this is what the function does:The function `func_2` accepts three parameters: `c`, `k`, and `l`, where `c` and `k` are non-negative integers, and `l` is a list of integers. It swaps the elements at indices `-c` and `-c - k` in the list `l`. The function returns the modified list `l`, which remains the same length and contains the same integers, but the values at the specified indices have been swapped.

#State of the program right berfore the function call: c is a positive integer, l is a list of integers of length n where n >= 2 * c, and the elements in l are distinct integers from 1 to n.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` where the (c-1)-th element and the c-th last element have been swapped. The (c-1)-th element is now `y`, and the c-th last element is now `x`.
#Overall this is what the function does:The function `func_3` accepts a positive integer `c` and a list `l` of distinct integers of length `n` (where `n` is at least twice `c`). It swaps the (c-1)-th element and the c-th last element of the list `l` and returns the modified list. After the function call, the (c-1)-th element of `l` is the value that was originally at the c-th last position, and the c-th last element of `l` is the value that was originally at the (c-1)-th position.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0.
    #State: `n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: *`n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns `n` and `k`, where `n` is an integer between 1 and 200,000 (inclusive), and `k` is an even integer between 0 and 1,000,000,000,000 (inclusive). Additionally, `max_k` is set to `n` and is greater than or equal to `k`.
#Overall this is what the function does:The function `func_4` reads two integers `n` and `k` from user input, where `1 <= n <= 2 * 10^5` and `0 <= k <= 10^12`. If `k` is odd, the function returns `(0, 0)`. If `k` is even, it calculates `max_k` based on whether `n` is odd or even. If `max_k` is less than `k`, the function returns `(0, 0)`. Otherwise, it returns the input values `n` and `k`. In the final state, if the function does not return `(0, 0)`, `n` and `k` are returned unchanged, with `n` being an integer between 1 and 200,000 (inclusive), and `k` being an even integer between 0 and 1,000,000,000,000 (inclusive), and `max_k` is greater than or equal to `k`.

#State of the program right berfore the function call: l is a list of integers where each integer is unique and within the range [1, n], and n is the length of the list l.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The integers in the list l are printed in the same order as they appear in the list, separated by spaces. The list l remains unchanged.
    print()
    #This is printed: (a blank line)
    return
    #The program returns None, and the integers in the list 'l' are printed in the same order as they appear in the list, separated by spaces. The list 'l' remains unchanged.
#Overall this is what the function does:The function `func_5` accepts a list `l` of unique integers within the range [1, n], where n is the length of the list. It prints "YES" followed by the integers in the list in the same order, separated by spaces, and then a blank line. The function returns `None`, and the list `l` remains unchanged.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: *`n` and `k` are updated to the values returned by `func_4()`, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_6` does not accept any parameters and does not return any value. It retrieves two integers `n` and `k` from the function `func_4`. If `n` is 0, it prints 'NO' and exits. Otherwise, it calls `func_1` with `n` and `k`, and then passes the result to `func_5`.

