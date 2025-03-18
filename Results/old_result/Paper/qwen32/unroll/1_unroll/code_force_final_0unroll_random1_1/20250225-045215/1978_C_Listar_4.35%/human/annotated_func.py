#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), k is a non-negative integer (0 ≤ k ≤ 10^12).
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
        
    #State: the list `l` is modified based on the value of `k` and the loop conditions.
#Overall this is what the function does:The function `func_1` takes a positive integer `n` and a non-negative integer `k` as inputs. It returns a list of integers from 1 to `n` that has been modified based on the value of `k`. The modifications involve rearranging the elements of the list according to specific conditions derived from the value of `k`. If `k` is 0, the function returns the list in its original order. Otherwise, elements are moved within the list following a specific pattern until `k` is reduced to 0 or all possible rearrangements are performed.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 * 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_2():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` and `k` are assigned the values of the two integers read from the input, where `n` is a positive integer (1 ≤ n ≤ 2 * 10^5) and `k` is a non-negative integer (0 ≤ k ≤ 10^12). Additionally, `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: `n` is a positive integer (1 ≤ n ≤ 2 * 10^5), and `k` is a non-negative even integer (0 ≤ k ≤ 10^12). If `n` is odd, `max_k` is set to `(n - 1) / 2`. If `n` is even, `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is a positive integer (1 ≤ n ≤ 2 * 10^5), and `k` is a non-negative even integer (0 ≤ k ≤ 10^12). If `n` is odd, `max_k` is set to `(n - 1) / 2`. If `n` is even, `max_k` is set to `n`. Additionally, `k` is less than or equal to `max_k`.
    return n, k
    #The program returns `n`, which is a positive integer (1 ≤ n ≤ 2 * 10^5), and `k`, which is a non-negative even integer (0 ≤ k ≤ 10^12) and less than or equal to `max_k`. If `n` is odd, `max_k` is set to `(n - 1) / 2`. If `n` is even, `max_k` is set to `n`.
#Overall this is what the function does:The function reads two integers `n` and `k` from the input. It returns `(0, 0)` if `k` is odd or if `k` is greater than a calculated maximum value `max_k`. Otherwise, it returns the original values of `n` and `k`. The maximum value `max_k` is `(n - 1) // 2` if `n` is odd, and `n // 2` if `n` is even.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where each integer is distinct and ranges from 1 to n.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The integers in the list l are printed in the order they appear, separated by spaces.
    print()
    #This is printed: (an empty line)
    return
    #The program returns None.
#Overall this is what the function does:The function `func_3` accepts a list `l` of integers representing a permutation of length `n`, where each integer is distinct and ranges from 1 to `n`. It prints the integers in the list in the order they appear, separated by spaces, followed by an empty line. The function does not return any value (returns `None`).

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 * 10^5, and k is a non-negative integer such that 0 <= k <= 10^12.
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value.
    #State: `n` is a positive integer such that 1 <= n <= 2 * 10^5, and `k` is a non-negative integer such that 0 <= k <= 10^12, and `n` is not equal to 0
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_4` takes no direct input parameters but implicitly receives values `n` and `k` from `func_2`. It checks if `n` is zero, in which case it prints 'NO' and terminates without returning any value. If `n` is not zero, it calls `func_1` with `n` and `k`, then passes the result to `func_3`. The function does not return any value.

