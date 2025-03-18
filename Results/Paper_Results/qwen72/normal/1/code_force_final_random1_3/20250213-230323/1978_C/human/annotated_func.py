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
        
    #State: After the loop executes all iterations, `c` will be the number of iterations the loop has run, which is `(n + 1) // 2`. The value of `k` will be reduced by the sum of the series of odd numbers from `n` down to 1 (or 0 if `n` is even), and then incremented by the number of iterations. The list `l` will be the result of applying `func_3` to the initial list `n` times, once for each iteration. The loop will terminate when `i` becomes -1, and the final value of `i` will be -1. If `k` becomes 0 during the loop, the function will return the current state of `l`. If `k` becomes less than `i - 1` during the loop, the function will return the result of `func_2(c, k, l)`.
#Overall this is what the function does:The function `func_1` takes two parameters, `n` and `k`, where `n` is a positive integer between 1 and 200,000, and `k` is a non-negative integer between 0 and 1,000,000,000,000. It modifies `k` by dividing it by 2 and initializes a list `l` containing integers from 1 to `n`. The function iterates over a range starting from `n` down to 0, decrementing by 2 in each step. During each iteration, it increments a counter `c` and checks conditions involving `k` and the current iteration index `i`. Depending on these conditions, the function may return the list `l`, call `func_2` with specific arguments, or update `l` using `func_3`. The final state of the program is determined by the value of `k` and the number of iterations completed. If `k` becomes 0, the function returns the current state of `l`. If `k` becomes less than `i - 1`, the function returns the result of `func_2`. Otherwise, it continues to update `k` and `l` until the loop completes, at which point it returns the final state of `l` or the result of `func_2` or `func_3`.

#State of the program right berfore the function call: c and k are non-negative integers, l is a list of integers of length at least c + k.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` which is a list of integers of length at least `c + k`. The elements at indices `-c - k` and `-c` in `l` are `x` and `y`, respectively.
#Overall this is what the function does:The function `func_2` accepts three parameters: `c`, `k`, and `l`. It swaps the elements at the positions `-c` and `-c - k` in the list `l` and returns the modified list. After the function executes, the list `l` has its elements at indices `-c` and `-c - k` swapped, while the rest of the list remains unchanged. The function ensures that the list `l` is of length at least `c + k`.

#State of the program right berfore the function call: c is a positive integer, l is a list of integers of length at least 2*c.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` where the elements at indices `c - 1` and `-c` have been swapped. The list `l` is of length at least 2*c, and `c` is a positive integer. The element originally at index `c - 1` is now at index `-c`, and the element originally at index `-c` is now at index `c - 1`.
#Overall this is what the function does:The function `func_3` accepts a positive integer `c` and a list `l` of integers with a length of at least 2*c. It swaps the elements at indices `c - 1` and `-c` in the list `l`. After the function executes, the list `l` is returned with these two elements swapped. The element originally at index `c - 1` is now at index `-c`, and the element originally at index `-c` is now at index `c - 1`.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns (0, 0)
    #State: *`n` and `k` are integers such that 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, `n` and `k` are updated to the values provided by the user input, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are integers such that 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: *`n` and `k` are integers such that 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the values of `n` and `k`, where `n` is an integer between 1 and 2 * 10^5, and `k` is an even integer between 0 and 10^12. Additionally, `max_k` is set to `n` (regardless of whether `n` is odd or even), and `max_k` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_4` reads two integers `n` and `k` from user input. It returns `(0, 0)` if `k` is odd or if `k` exceeds a calculated maximum value (`max_k`) based on `n`. If these conditions are not met, it returns the original values of `n` and `k`, where `n` is an integer between 1 and 2 * 10^5, and `k` is an even integer between 0 and 10^12. The maximum value `max_k` is determined based on whether `n` is odd or even.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n where 1 ≤ n ≤ 2·10^5.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: `l` is a list of integers representing a permutation of length `n` where 1 ≤ n ≤ 2·10^5, and all elements in `l` have been printed in the order they appear in the list.
    print()
    #This is printed: (a newline character)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_5` accepts a list `l` of integers representing a permutation of length `n` where 1 ≤ n ≤ 2·10^5. It prints "YES" followed by the elements of the list `l` in the order they appear, separated by spaces. After printing all elements, it prints a newline character. The function does not return any value.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns without any value.
    #State: *`n` and `k` are updated by `func_4()`, and 1 <= n <= 2 * 10^5, 0 <= k <= 10^12, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program does not return any value.
#Overall this is what the function does:The function `func_6` takes no parameters and does not return any value. It retrieves two integers `n` and `k` from the function `func_4`. If `n` is 0, it prints 'NO' and exits. Otherwise, it calls `func_1` with `n` and `k`, and then passes the result to `func_5`. The function does not modify any global state and does not return any value.

