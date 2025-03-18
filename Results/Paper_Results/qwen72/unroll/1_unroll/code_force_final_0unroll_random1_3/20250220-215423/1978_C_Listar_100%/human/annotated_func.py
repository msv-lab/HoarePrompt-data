#State of the program right berfore the function call: n is a positive integer, k is a non-negative integer such that 0 <= k <= 10^12.
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
        
    #State: `c` is \(\left\lceil \frac{n}{2} \right\rceil\), `k` is the result of the loop updates, and `l` is the result of applying `func_3` to `l` for each iteration or the result of `func_2` if the loop terminates early.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is a positive integer and `k` is a non-negative integer with a maximum value of \(10^{12}\). It modifies `k` by dividing it by 2 and initializes a list `l` containing integers from 1 to `n`. The function iterates over the range from `n` to 0 in steps of -2, incrementing a counter `c` at each step. If `k` becomes 0 during the iteration, the function returns the list `l`. If `k` is less than the current value of `i - 1`, the function returns the result of `func_2(c, k, l)`. Otherwise, it updates `k` and modifies `l` using `func_3(c, l)`. After the loop, the function returns the final state of `l`. The final state of the program is that `c` is \(\left\lceil \frac{n}{2} \right\rceil\), `k` is the result of the loop updates, and `l` is the result of applying `func_3` to `l` for each iteration or the result of `func_2` if the loop terminates early.

#State of the program right berfore the function call: c and k are non-negative integers, and l is a list of distinct integers from 1 to n, where n is the length of l, and 0 <= c < len(l) and 0 <= c + k < len(l).
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` which is a list of distinct integers from 1 to n, where n is the length of `l`. The list `l` contains the integers in some order, and the values of `x` and `y` are elements of `l` at the positions `-c - k` and `-c` respectively.
#Overall this is what the function does:The function `func_2` accepts three parameters: `c`, `k`, and `l`, where `c` and `k` are non-negative integers, and `l` is a list of distinct integers from 1 to n, with n being the length of `l`. It returns the list `l` with the elements at positions `-c - k` and `-c` swapped. The final state of the program is that the list `l` has the same elements but with the specified elements at the positions `-c - k` and `-c` exchanged.

#State of the program right berfore the function call: c is a positive integer, l is a list of integers of length n, and 1 <= c <= n/2.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` where the c-th element from the start has been replaced by the c-th element from the end, and the c-th element from the end has been replaced by the c-th element from the start.
#Overall this is what the function does:The function `func_3` accepts a positive integer `c` and a list of integers `l`. It returns the list `l` with the `c`-th element from the start and the `c`-th element from the end swapped. The original list `l` is modified in place.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns (0, 0)
    #State: `n` and `k` are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, `n` and `k` are assigned the values from the input, and `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, `k` is even. If `n` is odd, `max_k` is equal to (n^2 - 1) // 2. If `n` is even, `max_k` is equal to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: *`n` and `k` are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, `k` is even. If `n` is odd, `max_k` is equal to (n^2 - 1) // 2. If `n` is even, `max_k` is equal to `n`. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the integer `n` and the even integer `k`, where 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, and `max_k` is greater than or equal to `k`. If `n` is odd, `max_k` is equal to (n^2 - 1) // 2. If `n` is even, `max_k` is equal to `n`.
#Overall this is what the function does:The function `func_4` accepts no parameters and reads two integers `n` and `k` from user input. It returns `(0, 0)` if `k` is odd or if `k` is even but greater than the maximum allowed value `max_k`. If `k` is even and less than or equal to `max_k`, it returns the integers `n` and `k`. The value of `max_k` is calculated as `(n^2 - 1) // 2` if `n` is odd, and `n^2 // 2` if `n` is even. The function ensures that `1 <= n <= 2 * 10^5` and `0 <= k <= 10^12`.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n, where each integer is unique and in the range [1, n].
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The list l remains unchanged, and the integers in the list l are printed in the same order as they appear in the list, separated by spaces.
    print()
    #This is printed: (an empty line)
    return
    #The program returns nothing, but the integers in the list `l` are printed in the same order as they appear in the list, separated by spaces.
#Overall this is what the function does:The function `func_5` accepts a list `l` of unique integers in the range [1, n] and prints the string 'YES'. It then prints the integers in the list `l` in the same order as they appear, separated by spaces, followed by an empty line. The function does not modify the list `l` and returns nothing.

#State of the program right berfore the function call: n and k are non-negative integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns `None`.
    #State: *`n` and `k` are the values returned by `func_4()`, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_6` does not accept any parameters. It retrieves two non-negative integers `n` and `k` from the function `func_4`. If `n` is 0, it prints 'NO' and returns `None`. Otherwise, it calls `func_1` with `n` and `k` as arguments, and then calls `func_5` with the result of `func_1`. The function does not return any value in this case.

