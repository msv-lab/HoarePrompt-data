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
        
    #State: After all iterations of the loop, `n` remains a positive integer, `k` is reduced to a value that no longer satisfies the conditions for further loop execution (`k < i - 1` or `k == 0`), `l` is the result of applying `func_3` multiple times (specifically, `c` times, where `c` is the number of iterations the loop has run), and `c` is the total number of iterations the loop has executed. The value of `i` will be the last value decremented by 2 in the loop's range, which is either 0 or 1, depending on whether `n` is even or odd, respectively.
#Overall this is what the function does:The function `func_1` takes two parameters, `n` and `k`, where `n` is a positive integer representing the length of a permutation, and `k` is a non-negative integer representing a required Manhattan value. The function modifies the list `l`, which initially contains integers from 1 to `n` in ascending order. Depending on the value of `k`, the function may return the list `l` directly, or it may return the result of calling `func_2` or `func_3` with specific parameters. Specifically, the function can return `l` unchanged, the result of `func_2(c, k, l)`, or the result of `func_3(c, l)`, where `c` is the number of iterations the loop has executed. The final state of the program is such that `l` is either the original list or a modified version of it, and `k` is reduced to a value that no longer satisfies the conditions for further loop execution.

#State of the program right berfore the function call: c and k are non-negative integers, l is a list of integers of length at least c + k.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` where the integer at index `-c` and the integer at index `-c - k` have been swapped. The new value at index `-c` is the original value at index `-c - k`, and the new value at index `-c - k` is the original value at index `-c`. All other elements in the list remain unchanged.
#Overall this is what the function does:The function `func_2` accepts three parameters: `c`, `k`, and `l`. It swaps the elements at indices `-c` and `-c - k` in the list `l` and returns the modified list. The new value at index `-c` is the original value at index `-c - k`, and the new value at index `-c - k` is the original value at index `-c`. All other elements in the list remain unchanged.

#State of the program right berfore the function call: c is a positive integer, l is a list of integers with at least c elements.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l`, which is a list of integers with at least `c` elements. The element at index `c - 1` in `l` is `x`, and the element at index `-c` in `l` is `y`.
#Overall this is what the function does:The function `func_3` accepts a positive integer `c` and a list of integers `l` with at least `c` elements. It swaps the elements at indices `c - 1` and `-c` in the list `l`. The function returns the modified list `l`, where the elements at these indices have been swapped.

#State of the program right berfore the function call: n and k are non-negative integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns (0, 0)
    #State: `n` and `k` are non-negative integers such that 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `n` and `k` are updated to the values provided by the user. Additionally, `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are non-negative integers such that 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is set to `(n`. If `n` is even, `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: *`n` and `k` are non-negative integers such that 1 <= `n` <= 2 * 10^5 and 0 <= `k` <= 10^12, and `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the values of `n` and `k`, where `n` is a non-negative integer between 1 and 2 * 10^5, and `k` is an even non-negative integer less than or equal to 10^12. Additionally, `max_k` is set to `n` regardless of whether `n` is odd or even, and `max_k` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_4` reads two non-negative integers `n` and `k` from user input, where `1 <= n <= 2 * 10^5` and `0 <= k <= 10^12`. If `k` is odd, the function returns `(0, 0)`. If `k` is even, the function calculates `max_k` based on the parity of `n`: if `n` is odd, `max_k` is set to `(n^2 - 1) // 2`; if `n` is even, `max_k` is set to `n^2 // 2`. If `k` exceeds `max_k`, the function returns `(0, 0)`. Otherwise, the function returns the values of `n` and `k`.

#State of the program right berfore the function call: l is a list of integers representing a valid permutation of length n.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: `l` is a list of integers representing a valid permutation of length n, where all integers in the list have been printed in the order they appear in the list.
    print()
    #This is printed: (a blank line)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_5` accepts a list `l` of integers representing a valid permutation of length `n`. It prints "YES" followed by each integer in the list `l` in the order they appear, separated by spaces. After printing all the integers, it prints a blank line. The function does not return any value.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None.
    #State: *`n` and `k` are integers assigned by `func_4()`, and 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program does not return any value.
#Overall this is what the function does:The function `func_6` does not accept any parameters. It retrieves two integers `n` and `k` from the function `func_4`. If `n` is 0, it prints 'NO' and returns `None`. Otherwise, it calls `func_1` with `n` and `k`, passing the result to `func_5`. In both cases, the function either returns `None` or does not return any value.

