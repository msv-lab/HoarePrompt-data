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
        
    #State: 
#Overall this is what the function does:The function accepts two parameters, `n` (a positive integer between 1 and 200,000) and `k` (a non-negative integer between 0 and 1 trillion). It returns a list `l` which is initially a range from 1 to `n`. The function modifies this list based on the value of `k` and returns it. If `k` is reduced to zero during the process, the current state of the list `l` is returned. If `k` is less than `i - 1` at any point, the function calls `func_2` with the current count `c`, the remaining `k`, and the list `l`. The list `l` is also modified by calling `func_3` with the count `c` in each iteration of the loop. The final state of the program is the returned list `l` after all modifications.

#State of the program right berfore the function call: c and k are non-negative integers, and l is a list of integers with a length sufficient to support indexing with -c and -c-k without going out of bounds.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` which contains integers and has a length sufficient to support indexing with `-c` and `-c-k` without going out of bounds.
#Overall this is what the function does:The function takes three parameters: `c` and `k`, which are non-negative integers, and `l`, which is a list of integers. It swaps the elements at the positions `-c` and `-c-k` in the list `l` and returns the modified list.

#State of the program right berfore the function call: c is a positive integer, and l is a list of integers such that 0 < c <= len(l).
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` of integers such that 0 < `c` <= len(`l`).
#Overall this is what the function does:The function accepts a positive integer `c` and a list of integers `l` such that `0 < c <= len(l)`. It returns the list `l` with the elements at positions `c-1` and `-c` swapped.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), and `k` is a non-negative integer (0 ≤ k ≤ 10^12). Additionally, `k` is even (k % 2 == 0).
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), and `k` is a non-negative integer (0 ≤ k ≤ 10^12) and `k` is even (k % 2 == 0). `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `k` is a non-negative integer (0 ≤ k ≤ 10^12) and `k` is even (k % 2 == 0). `max_k` is set to `n`. Additionally, `max_k` is not less than `k`, which means `n` is greater than or equal to `k`.
    return n, k
    #The program returns a tuple containing the positive integer `n` (1 ≤ n ≤ 2 · 10^5) and the even non-negative integer `k` (0 ≤ k ≤ 10^12), where `n` is greater than or equal to `k`.
#Overall this is what the function does:The function reads two integers `n` and `k` from the input. It returns `(0, 0)` if `k` is odd or if `k` is greater than the maximum possible value of `k` based on `n`. Otherwise, it returns the tuple `(n, k)` where `n` is a positive integer and `k` is a non-negative even integer such that `n` is greater than or equal to `k`.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where each integer is distinct and in the range from 1 to n.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: the integers in the list l are printed in the same order, separated by spaces.
    print()
    #This is printed: (newline)
    return
    #The program returns None.
#Overall this is what the function does:The function `func_5` accepts a list `l` of integers representing a permutation of length `n`, where each integer is distinct and in the range from 1 to `n`. It prints the integers in the list `l` in the same order, separated by spaces, followed by a newline. The function returns `None`.

#State of the program right berfore the function call: n is a positive integer (1 <= n <= 2 * 10^5) and k is a non-negative integer (0 <= k <= 10^12).
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: `n` and `k` are the values returned by `func_4()`. `n` is not equal to 0.
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_6` retrieves values `n` and `k` from `func_4()`. If `n` is 0, it prints 'NO' and returns `None`. Otherwise, it processes these values using `func_1(n, k)` and then calls `func_5()` with the result, ultimately returning `None`.

