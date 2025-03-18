#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2 * 10^5, and k is an integer such that 0 <= k <= 10^12.
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
        
    #State: c is 1, k is 0, l is a list containing integers from 1 to n inclusive.
#Overall this is what the function does:The function accepts two parameters, `n` (an integer between 1 and 2 * 10^5) and `k` (an integer between 0 and 10^12). It reduces `k` by half, initializes a list `l` with integers from 1 to `n`, and iterates over `l` in reverse order. If `k` becomes zero, it returns the list `l`. If `k` is less than the current index minus one, it calls another function `func_2` with parameters `c`, `k`, and `l`. Otherwise, it decrements `k` and calls another function `func_3` with parameters `c` and `l`. Finally, it returns the modified list `l` where `c` is 1, `k` is 0, and `l` contains integers from 1 to `n`.

#State of the program right berfore the function call: c is a non-negative integer less than the length of list l, k is a non-negative integer, and l is a list of integers representing a permutation of length n.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` where the elements at indices `-c` and `-c - k` have been swapped.
#Overall this is what the function does:The function accepts three parameters: `c` (a non-negative integer less than the length of list `l`), `k` (a non-negative integer), and `l` (a list of integers representing a permutation of length `n`). After executing, it returns the list `l` with the elements at indices `-c` and `-c - k` swapped.

#State of the program right berfore the function call: c is a positive integer such that 1 <= c <= len(l)/2, and l is a list of integers representing a permutation of length n.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` with the elements at indices -c and c-1 swapped.
#Overall this is what the function does:The function accepts a positive integer `c` and a list of integers `l`. It swaps the elements at indices `-c` and `c-1` in the list `l` and returns the modified list.

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 ⋅ 10^5 and 0 ≤ k ≤ 10^12.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two zeros, where both values are 0.
    #State: `n` is an integer between 1 and 2 * 10^5 (inclusive), `k` is an integer between 0 and 10^12 (inclusive). `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: Postcondition: `n` is an integer between 1 and 2 * 10^5 (inclusive), `k` is an integer between 0 and 10^12 (inclusive). If `n` is odd, `max_k` is `n`. If `n` is even, `max_k` is `k`.
    if (max_k < k) :
        return 0, 0
        #The program returns two values, both of which are 0.
    #State: Postcondition: `n` is an integer between 1 and 2 * 10^5 (inclusive), `k` is an integer between 0 and 10^12 (inclusive). If `n` is odd, `max_k` is `n`. If `n` is even, `max_k` is `k`, and `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns two values, `n` which is an integer between 1 and 2 * 10^5 (inclusive), and `k` which is an integer between 0 and 10^12 (inclusive). If `n` is odd, `k` is set to `n`. If `n` is even, `k` remains as the original value of `k`, but `k` is guaranteed to be greater than or equal to its original value.
#Overall this is what the function does:The function accepts no parameters and returns either two zeros or two values where `n` is an integer between 1 and 2 * 10^5 (inclusive) and `k` is an integer between 0 and 10^12 (inclusive). If `n` is odd, `k` is set to `n`. If `n` is even, `k` remains as the original value of `k`, but `k` is guaranteed to be greater than or equal to its original value.

#State of the program right berfore the function call: l is a list of integers where each integer represents a position in the permutation that satisfies the Manhattan value condition.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: the list of integers from the initial state, printed in the same order with spaces in between.
    print()
    #This is printed: None
    return
    #The program returns an empty list since there are no values being returned or calculated in the provided code.
#Overall this is what the function does:The function `func_5` accepts a list of integers `l`. It prints "YES" followed by each integer in the list separated by spaces. After printing, it returns an empty list.

#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and k is a non-negative integer such that 0 ≤ k ≤ 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns 0 for `n` and a non-negative integer `k` such that 0 ≤ k ≤ 10^12, both of which are the return values from `func_4()`
    #State: `n` is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, `k` is a non-negative integer such that 0 ≤ k ≤ 10^12, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns a value that is the result of calling func_5 with the argument l, where l itself is the result of calling func_1 with arguments n and k.
#Overall this is what the function does:The function does not accept any parameters directly but relies on the outputs of `func_4()` and `func_1()`. It first checks if `n` (obtained from `func_4()`) is zero. If so, it prints 'NO' and returns immediately. Otherwise, it calls `func_1()` with `n` and `k` (also obtained from `func_4()`), then calls `func_5()` with the result of `func_1()`, and finally returns the result of `func_5()`.

