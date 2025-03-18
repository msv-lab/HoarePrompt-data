#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 * 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
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
        
    #State: `c` is the number of iterations, `k` is the remaining value, `l` is the final modified list, and `n` and the original `k` (before `k // 2`) remain unchanged.
#Overall this is what the function does:The function `func_1` takes two parameters: `n`, a positive integer (1 ≤ n ≤ 2 * 10^5), and `k`, a non-negative integer (0 ≤ k ≤ 10^12). It performs a series of operations involving a list of integers from 1 to `n` and the value `k`, which is initially halved. The function either returns a modified list or calls another function `func_2` or `func_3` based on the relationship between `n` and `k`. The final output is a list of integers.

#State of the program right berfore the function call: c and k are non-negative integers, and l is a list of integers such that the indices -c and -c-k are valid indices within the list l.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` where the elements at indices `-c` and `-c-k` have been swapped.
#Overall this is what the function does:The function accepts three parameters: `c` and `k`, which are non-negative integers, and `l`, which is a list of integers. It returns the list `l` with the elements at indices `-c` and `-c-k` swapped.

#State of the program right berfore the function call: c is an integer such that 1 <= c <= len(l) // 2, and l is a list of integers.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` where the c-th element from the start has been replaced with `x` and the c-th element from the end has been replaced with `y`. Here, `x` is the original c-th element from the end of `l`, and `y` is the original c-th element from the start of `l`.
#Overall this is what the function does:The function takes an integer `c` and a list `l` as input, and returns the list `l` with the c-th element from the start and the c-th element from the end swapped.

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 * 10^5, and k is a non-negative integer such that 0 <= k <= 10^12.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` and `k` are integers as input where `n` is a positive integer such that 1 <= n <= 2 * 10^5, and `k` is a non-negative integer such that 0 <= k <= 10^12. Additionally, `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: `n` is a positive integer such that 1 <= n <= 2 * 10^5, and `k` is a non-negative even integer such that 0 <= k <= 10^12. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is a positive integer such that 1 <= n <= 2 * 10^5, and `k` is a non-negative even integer such that 0 <= k <= 10^12. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`. Additionally, `max_k` is not less than `k`
    return n, k
    #The program returns the tuple (n, k), where n is a positive integer such that 1 <= n <= 2 * 10^5, and k is a non-negative even integer such that 0 <= k <= 10^12.
#Overall this is what the function does:The function reads two integers, `n` and `k`, from input. If `k` is odd, or if `k` is greater than the maximum possible value of `k` based on whether `n` is odd or even, it returns `(0, 0)`. Otherwise, it returns the tuple `(n, k)`.

#State of the program right berfore the function call: l is a list of integers representing a valid permutation of length n, where each integer is distinct and in the range from 1 to n.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: the integers from the list l are printed in the order they appear, separated by spaces.
    print()
    #This is printed: (an empty line)
    return
    #The program returns None
#Overall this is what the function does:The function `func_5` takes a list `l` of integers representing a valid permutation of length `n`, where each integer is distinct and in the range from 1 to `n`. It prints "YES" followed by the integers in the list `l` separated by spaces, and then prints an empty line. The function returns `None`.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing (None).
    #State: `n` and `k` are assigned the values returned by `func_4()`. `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns None.
#Overall this is what the function does:The function `func_6` retrieves values for `n` and `k` from `func_4`. If `n` is 0, it prints 'NO' and returns `None`. Otherwise, it processes these values using `func_1` and `func_5`, and then returns `None`.

