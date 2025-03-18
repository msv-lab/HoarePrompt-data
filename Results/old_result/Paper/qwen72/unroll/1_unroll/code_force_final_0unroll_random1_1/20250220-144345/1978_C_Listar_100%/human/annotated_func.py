#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), k is a non-negative integer (0 ≤ k ≤ 10^12), and k is divisible by 2.
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
        
    #State: `c` is `n // 2 + 1` if `n` is odd, or `n // 2` if `n` is even, `k` is the result of repeated subtractions, and `l` is the result of repeated calls to `func_3(c, l)`.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is a positive integer (1 ≤ n ≤ 200,000) and `k` is a non-negative integer (0 ≤ k ≤ 1,000,000,000,000) that is divisible by 2. The function returns a list `l` which initially contains integers from 1 to `n`. The function modifies `l` and `k` through a series of operations. If `k` becomes 0, the function returns the current state of `l`. If `k` is less than the current value of `i - 1` during the loop, the function returns the result of `func_2(c, k, l)`. Otherwise, it continues to modify `l` and `k` until the loop completes, at which point it returns the final state of `l`.

#State of the program right berfore the function call: c and k are non-negative integers, l is a list of distinct integers of length n, where 1 <= n <= 2 * 10^5, and 0 <= c < len(l), 0 <= k < len(l).
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` of distinct integers of length `n`, where 1 <= `n` <= 2 * 10^5, and the element at index `len(l) - c - 1` is `y`, and the element at index `len(l) - c - k - 1` is `x`.
#Overall this is what the function does:The function `func_2` accepts three parameters: `c`, `k`, and `l`. It swaps the elements at the positions `len(l) - c - 1` and `len(l) - c - k - 1` in the list `l`. The function returns the modified list `l`, which still contains distinct integers of length `n` (where 1 <= n <= 2 * 10^5). After the function concludes, the element at index `len(l) - c - 1` is the original element at index `len(l) - c - k - 1`, and the element at index `len(l) - c - k - 1` is the original element at index `len(l) - c - 1`.

#State of the program right berfore the function call: c is a positive integer, l is a list of integers of length n, where 1 <= c <= n/2.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` where the values at indices `c-1` and `-c` have been swapped.
#Overall this is what the function does:The function `func_3` accepts a positive integer `c` and a list of integers `l`. It swaps the values at indices `c-1` and `-c` in the list `l` and returns the modified list. The function ensures that the values at these specific indices are exchanged, leaving the rest of the list unchanged.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0.
    #State: `n` and `k` are assigned the integer values from the input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are assigned the integer values from the input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is assigned the value (n^2 - 1) // 2. If `n` is even, `max_k` is assigned the value of `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: `n` and `k` are assigned the integer values from the input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is assigned the value (n^2 - 1) // 2. If `n` is even, `max_k` is assigned the value of `n`. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the integer values of `n` and `k`, where 1 <= `n` <= 2 * 10^5, 0 <= `k` <= 10^12, and `k` is even. Additionally, if `n` is odd, `max_k` is (n^2 - 1) // 2, and if `n` is even, `max_k` is `n`. In both cases, `max_k` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_4` takes no parameters and reads two integers `n` and `k` from the user input. It returns `(0, 0)` if `k` is odd or if `k` is even but greater than the maximum possible value `max_k` (which is `(n^2 - 1) // 2` if `n` is odd, and `n^2 // 2` if `n` is even). Otherwise, it returns the input integers `n` and `k`, where `1 <= n <= 2 * 10^5`, `0 <= k <= 10^12`, and `k` is even. The function ensures that `max_k` is always greater than or equal to `k` when it returns `n` and `k`.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where n is a positive integer.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The list `l` remains unchanged, and the integers in `l` are printed in the order they appear in the list, separated by spaces.
    print()
    #This is printed: (a blank line)
    return
    #The program returns nothing, but the integers in the list `l` are printed in the order they appear, separated by spaces.
#Overall this is what the function does:The function `func_5` accepts a list `l` of integers representing a permutation of length `n` and prints "YES" followed by the integers in the list in the order they appear, separated by spaces. The list `l` remains unchanged. The function does not return any value.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: *`n` and `k` are the values returned by `func_4()`. The values of `n` and `k` are now updated to the specific values returned by the function, but the constraints 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12 still apply. Additionally, `n` is not equal to 0.
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_6` does not accept any parameters and does not return any value. It retrieves two integers `n` and `k` from the function `func_4`. If `n` is 0, it prints 'NO' and exits. Otherwise, it calls `func_1` with `n` and `k`, and then passes the result to `func_5`. The function ultimately does not return any value.

