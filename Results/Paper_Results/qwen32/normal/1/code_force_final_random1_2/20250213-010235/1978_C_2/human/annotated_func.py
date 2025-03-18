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
        
    #State: `c` is the total number of iterations completed, `k` is `0` or less than `i - 1` for the last iteration, and `l` is the list after being modified by `func_3` for each iteration.
#Overall this is what the function does:The function `func_1` takes a positive integer `n` and a non-negative integer `k` as input. It initializes a list `l` with integers from 1 to `n`. Depending on the value of `k`, it either returns the list `l` directly, calls `func_2` with specific arguments, or modifies `l` using `func_3`. The final output is either the original list `l`, a modified version of `l`, or the result of calling `func_2` with certain parameters.

#State of the program right berfore the function call: c and k are non-negative integers, and l is a list of integers such that c and k are within the bounds that allow valid indexing and swapping within the list l. Specifically, c should be less than the length of l, and c + k should also be a valid index within l (i.e., c + k < len(l)).
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` which contains integers, with `c` being a non-negative integer less than the length of `l`, and `c + k` also a valid index within `l`. The elements `x` and `y` are defined as `x = l[-c - k]` and `y = l[-c]`.
#Overall this is what the function does:The function `func_2` takes a list `l` of integers and two non-negative integers `c` and `k` as input. It swaps the elements at the positions `-c - k` and `-c` in the list `l` and returns the modified list.

#State of the program right berfore the function call: c is a positive integer, and l is a list of integers such that c <= len(l).
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` which contains integers where the c-th element is `y` and the c-th last element is `x`.
#Overall this is what the function does:The function takes a positive integer `c` and a list of integers `l` such that `c` is less than or equal to the length of `l`. It swaps the c-th element with the c-th last element in the list and returns the modified list.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns (0, 0)
    #State: `n` is the first integer read from the input, `k` is the second integer read from the input, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: `n` is the first integer read from the input, `k` is the second integer read from the input, and `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0
    #State: `n` is the first integer read from the input, `k` is the second integer read from the input, and `k` is even. `max_k` is set to `n`. `max_k` is not less than `k`.
    return n, k
    #The program returns the tuple (n, k) where n is the first integer read from the input and k is the second even integer read from the input.
#Overall this is what the function does:The function reads two integers, `n` and `k`, from the input. It returns `(0, 0)` if `k` is odd or if `k` exceeds the maximum possible value based on `n`. Otherwise, it returns the tuple `(n, k)` where `k` is even.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n where each integer is distinct and in the range from 1 to n.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: All elements of the list `l` have been printed in the order they appear in the list, separated by spaces.
    print()
    #This is printed: (newline)
    return
    #The program returns None
#Overall this is what the function does:The function takes a list `l` of integers representing a permutation of length `n` where each integer is distinct and in the range from 1 to `n`. It prints "YES" followed by the elements of the list `l` in their original order, separated by spaces, and then prints a newline. The function returns `None`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is a non-negative integer representing the required Manhattan value.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: `n` and `k` are the values returned by `func_4()`. `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program does not return any value.
#Overall this is what the function does:The function `func_6` determines whether a permutation of length `n` with a specific Manhattan value `k` can be constructed. If `n` is 0, it prints 'NO' and returns `None`. Otherwise, it processes the values using other functions (`func_1` and `func_5`) but does not return any value.

