#State of the program right berfore the function call: n is a positive integer, and k is a non-negative integer such that 0 <= k <= 10^12.
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
        
    #State: The list `l` is modified such that the last element is moved to the position `-k` (if `1 + i > k`) or to the beginning of the list (if `1 + i <= k`). The value of `k` is updated to `k - i + 1` in each iteration until the loop completes.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a non-negative integer `k` (0 <= k <= 10^12). It returns a modified list `l` of integers from 1 to `n` where the last element of the list is moved to a new position based on the value of `k`. If `k` is 0, the function returns the list `l` unchanged. If `1 + i > k` for any iteration, the last element is moved to the position `-k` in the list, and the function returns the modified list. Otherwise, the last element is repeatedly moved to the beginning of the list until the loop completes, and the function returns the final modified list.

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
    #State: *`n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is calculated as (n^2 - 1) // 2. If `n` is even, `max_k` is equal to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: *`n` and `k` are integers provided by the user input, where 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is calculated as (n^2 - 1) // 2. If `n` is even, `max_k` is equal to `n`. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns `n` and `k`, where `n` is an integer between 1 and 200,000 (inclusive), and `k` is an even integer between 0 and 1,000,000,000,000 (inclusive). Additionally, if `n` is odd, `k` is less than or equal to `(n^2 - 1) // 2`, and if `n` is even, `k` is less than or equal to `n`.
#Overall this is what the function does:The function `func_2` reads two integers `n` and `k` from user input, where `1 <= n <= 2 * 10^5` and `0 <= k <= 10^12`. If `k` is odd, the function returns `(0, 0)`. If `k` is even, the function calculates a maximum value `max_k` based on `n` (if `n` is odd, `max_k = (n^2 - 1) // 2`; if `n` is even, `max_k = n^2 // 2`). If `k` exceeds `max_k`, the function returns `(0, 0)`. Otherwise, it returns the original values of `n` and `k`.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where n is a positive integer.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The list l remains unchanged, and the integers in l are printed in the same order they appear in the list, separated by spaces.
    print()
    #This is printed: (an empty line)
    return
    #The program returns nothing, but the integers in the list `l` are printed in the same order they appear in the list, separated by spaces.
#Overall this is what the function does:The function `func_3` accepts a list `l` of integers representing a permutation. It prints "YES" followed by the integers in the list `l` in the same order they appear, separated by spaces, and then prints an empty line. The function does not modify the list `l` and returns nothing.

#State of the program right berfore the function call: n and k are non-negative integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as the return statement is empty. The values of `n` and `k` have been updated to the specific values returned by `func_2()`, but these values are not returned by the current code snippet.
    #State: `n` and `k` are updated to the values returned by `func_2()`. The values of `n` and `k` are now the specific values returned by `func_2()`, and they still adhere to the constraints 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12. Additionally, `n` is not equal to 0.
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_4` updates the values of `n` and `k` internally by calling `func_2()`. If `n` is 0, it prints 'NO' and returns without performing any further actions. If `n` is not 0, it calls `func_1` with `n` and `k` as arguments, and then calls `func_3` with the result of `func_1`. The function does not return any value.

