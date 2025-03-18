#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
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
        
    #State: `n` is unchanged, `k` is 0 or less than `i - 1` at termination, `c` is the count of iterations, and `l` is the final list after all updates by `func_3(c, l)`.
#Overall this is what the function does:The function `func_1` accepts two parameters: `n`, a positive integer, and `k`, a non-negative integer. It returns a list that has been modified based on the values of `n` and `k`. The final state of the program is a list `l` that has undergone transformations through iterations and calls to `func_3`. The function may also return early if `k` becomes 0 or less than `i - 1` during the process.

#State of the program right berfore the function call: c and k are non-negative integers, and l is a list of integers such that the indices -c and -c-k are valid within the bounds of the list l.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` of integers.
#Overall this is what the function does:The function takes a list of integers `l` and two non-negative integers `c` and `k`. It swaps the elements at the positions `-c` and `-c-k` in the list `l` and returns the modified list.

#State of the program right berfore the function call: c is a positive integer such that 1 <= c <= len(l) // 2, and l is a list of integers with at least 2*c elements.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` which contains at least `2*c` elements, with `c` being a positive integer such that `1 <= c <= len(l) // 2`. The value of `x` is `l[c-1]`, and the value of `y` is `l[-c]`.
#Overall this is what the function does:The function takes a positive integer `c` and a list `l` of integers with at least `2*c` elements. It then swaps the elements at positions `c-1` and `-c` in the list `l` and returns the modified list.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 \cdot 10^{5}), and k is a non-negative integer (0 ≤ k ≤ 10^{12}).
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is the first integer read from the input, `k` is the second integer read from the input, and `k` is an even number
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: `n` is the first integer read from the input and `k` is the second integer read from the input, with `k` being an even number. If `n` is odd, `max_k` is set to `n`. Otherwise, if `n` is even, `max_k` is also set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is the first integer read from the input and `k` is the second integer read from the input, with `k` being an even number. `max_k` is set to `n`. Additionally, `max_k` is not less than `k`.
    return n, k
    #The program returns the tuple (n, k), where n is the first integer read from the input and k is the second integer read from the input, with k being an even number.
#Overall this is what the function does:The function reads two integers `n` and `k` from the input. It returns `(0, 0)` if `k` is odd or if `k` is even but greater than the maximum possible value `max_k` (which depends on whether `n` is odd or even). Otherwise, it returns the tuple `(n, k)` where `k` is an even number.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where each integer is distinct and in the range from 1 to n.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The list `l` remains unchanged, and all elements of `l` are printed in a single line, separated by spaces.
    print()
    #This is printed: (an empty line)
    return
    #The program returns None
#Overall this is what the function does:The function `func_5` accepts a list `l` of integers representing a permutation of length `n`, where each integer is distinct and in the range from 1 to `n`. It prints "YES" followed by the elements of the list `l` on the same line, separated by spaces, and then prints an empty line. The function returns `None`.

#State of the program right berfore the function call: n is a positive integer (1 <= n <= 2 * 10^5) and k is a non-negative integer (0 <= k <= 10^12).
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing (None)
    #State: `n` and `k` are the values returned by `func_4()`. `n` is not equal to 0.
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_6` retrieves values `n` and `k` from `func_4()`. If `n` is 0, it prints 'NO' and returns nothing. Otherwise, it processes these values through `func_1()` and `func_5()`, and finally returns nothing.

