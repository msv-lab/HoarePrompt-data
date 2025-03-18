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
        
    #State: 
#Overall this is what the function does:The function `func_1` takes two parameters: `n`, a positive integer representing the length of the permutation, and `k`, a non-negative integer representing the required Manhattan value. It processes these inputs and returns either a list `l` containing integers from 1 to `n`, or the result of calling other functions (`func_2` or `func_3`) with specific arguments, depending on the values of `n` and `k`.

#State of the program right berfore the function call: c and k are non-negative integers, and l is a list of integers such that c and k are within the bounds that allow valid indexing into l without causing an out-of-range error. Specifically, c and c+k should be less than the length of l.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` which is a list of integers.
#Overall this is what the function does:The function takes a list `l` of integers and two non-negative integers `c` and `k`. It swaps the elements at positions `-c` and `-c-k` in the list `l` and returns the modified list.

#State of the program right berfore the function call: c is a positive integer such that 1 <= c <= len(l)//2, and l is a list of length at least 2*c containing distinct integers.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` after swapping the `c`-th element from the end (`x`) with the element at index `c-1` (`y`). The element at index `c-1` is now `x`, and the element at index `-c` is now `y`.
#Overall this is what the function does:The function takes a positive integer `c` and a list `l` of length at least `2*c` containing distinct integers. It swaps the `c`-th element from the end of the list with the element at index `c-1` and returns the modified list.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and k is a non-negative integer (0 ≤ k ≤ 10^12).
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns (0, 0)
    #State: `n` is the first integer from the input, `k` is the second integer from the input, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: `n` is the first integer from the input, `k` is the second integer from the input, and `k` is even. If `n` is odd, `max_k` is calculated as `n + k`. If `n` is even, `max_k` is calculated as `n - k`.
    if (max_k < k) :
        return 0, 0
        #The program returns (0, 0)
    #State: `n` is the first integer from the input, `k` is the second integer from the input, and `k` is even. If `n` is odd, `max_k` is calculated as `n + k`. If `n` is even, `max_k` is calculated as `n - k`. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the tuple (n, k), where n is the first integer from the input and k is the second even integer from the input.
#Overall this is what the function does:The function accepts two integers, `n` and `k`, where `n` is a positive integer and `k` is a non-negative integer. It returns `(0, 0)` if `k` is odd or if `k` exceeds the maximum possible value based on `n`. Otherwise, it returns the tuple `(n, k)` if `k` is even and within the allowed range.

#State of the program right berfore the function call: l is a list of integers representing a valid permutation of length n, where each integer is distinct and within the range 1 to n.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: the elements of list `l` printed in sequence, each followed by a space.
    print()
    #This is printed: (newline)
    return
    #The program does not return any value.
#Overall this is what the function does:The function takes a list `l` of integers representing a valid permutation of length `n`, where each integer is distinct and within the range 1 to `n`. It prints "YES" followed by the elements of the list `l` in sequence, each separated by a space, and then prints a newline. The function does not return any value.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is a non-negative integer representing the required Manhattan value.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: `n` is a positive integer, `k` is a non-negative integer, as returned by `func_4()`. `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_6` takes no direct input parameters. It retrieves values `n` and `k` from `func_4`, where `n` is a positive integer and `k` is a non-negative integer. If `n` is zero, it prints 'NO' and returns `None`. Otherwise, it uses these values to generate a list `l` via `func_1(n, k)` and then passes `l` to `func_5`. The function always returns `None`.

