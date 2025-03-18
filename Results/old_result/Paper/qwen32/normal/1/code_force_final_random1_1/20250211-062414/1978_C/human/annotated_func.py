#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is a non-negative integer representing the required Manhattan value.
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
        
    #State: `n` is a positive integer, `k` is `k - ((n // 2) * n + (3 * (n // 2)^2 + 5 * (n // 2) + 2) / 2)`, `l` is the result of `func_3((n // 2) + 1, l)` if `n` is odd, or `func_3(n // 2, l)` if `n` is even, `c` is `(n // 2) + 1` if `n` is odd, or `n // 2` if `n` is even.
#Overall this is what the function does:The function `func_1` generates a permutation of integers from 1 to `n` based on the given Manhattan value `k`. Depending on the value of `k`, it either returns a simple list of integers from 1 to `n`, or it calls other functions (`func_2` and `func_3`) to compute and return a modified permutation.

#State of the program right berfore the function call: c and k are non-negative integers, and l is a list of integers with at least c + k + 1 elements.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` which contains at least `c + k + 1` elements, with `x` being the element at index `-c - k` and `y` being the element at index `-c`.
#Overall this is what the function does:The function `func_2` takes three parameters: two non-negative integers `c` and `k`, and a list `l` of integers with at least `c + k + 1` elements. It swaps the elements at positions `-c` and `-c - k` in the list `l` and returns the modified list.

#State of the program right berfore the function call: c is a positive integer, l is a list of integers with at least c elements.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` which contains at least `c` elements, where `c` is a positive integer. The `c`-th element of `l` is `x`, and the `c`-th last element of `l` is `y`.
#Overall this is what the function does:The function takes a positive integer `c` and a list `l` of integers with at least `c` elements, and returns the list `l` with the `c`-th element and the `c`-th last element swapped.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 * 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is the first integer read from the input, `k` is the second integer read from the input, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: `n` is the first integer read from the input, `k` is the second integer read from the input, and `k` is even. If `n` is odd, `max_k` is calculated as `n`. If `n` is even, `max_k` is `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns (0, 0)
    #State: `n` is the first integer read from the input, `k` is the second integer read from the input, and `k` is even. `max_k` is calculated as `n` if `n` is odd, or `max_k` is `n` if `n` is even. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the tuple (n, k) where n is the first integer read from the input and k is the second even integer read from the input.
#Overall this is what the function does:The function reads two integers, `n` and `k`, from the input. If `k` is not an even integer, or if `k` exceeds the maximum possible value based on `n`, the function returns `(0, 0)`. Otherwise, it returns the tuple `(n, k)`.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n where each integer is distinct and within the range from 1 to n.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: All elements of the list `l` have been printed in order, separated by spaces.
    print()
    #This is printed: (newline)
    return
    #The program returns None
#Overall this is what the function does:The function accepts a list `l` of integers representing a permutation of length `n` where each integer is distinct and within the range from 1 to `n`. It prints "YES" followed by the elements of the list `l` on the same line, separated by spaces, and then prints a newline. The function returns `None`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is a non-negative integer representing the required Manhattan value.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value.
    #State: `n` and `k` are the values returned by `func_4()`. `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_6` determines whether a permutation of length `n` with a specific Manhattan value `k` can be constructed. If `n` is zero, it prints 'NO' and does not return any value. Otherwise, it processes the inputs using other functions (`func_1` and `func_5`) and ultimately returns `None`.

