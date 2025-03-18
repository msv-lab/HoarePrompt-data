#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is a non-negative integer representing the required Manhattan value such that 0 <= k <= 10^12.
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
        
    #State: After all iterations, `n` remains a positive integer, `k` is reduced by a series of subtractions based on the loop's decrement pattern, `l` is the result of multiple calls to `func_3` with increasing `c` values, `c` equals the number of iterations completed, and `i` is the final value of the loop counter which is `-1` or the last even number before `-1` depending on the initial value of `n`. The loop terminates when `k` is no longer greater than or equal to `i - 1`, or when `i` becomes `-1`.
#Overall this is what the function does:The function `func_1` takes two parameters, `n` (a positive integer) and `k` (a non-negative integer). It modifies a list `l` initially containing integers from 1 to `n` inclusive. Depending on the value of `k` and the internal logic, the function may return the list `l` directly, or it may return the result of calling either `func_2` or `func_3` with specific arguments. Specifically, if `k` is reduced to zero during the loop, the function returns the current state of `l`. If `k` is less than `i - 1` at any point, the function returns the result of `func_2(c, k, l)`. Otherwise, the function continues modifying `l` through calls to `func_3` and adjusting `k` until the loop terminates. The final state of the program includes a modified list `l` and a potentially reduced value of `k`.

#State of the program right berfore the function call: c is a non-negative integer, k is an integer, and l is a list of integers of length at least c + k + 1.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` where the elements at positions `-c - k` and `-c` have been swapped. The element originally at position `-c - k` is now at position `-c`, and the element originally at position `-c` is now at position `-c - k`.
#Overall this is what the function does:The function `func_2` accepts three parameters: `c` (a non-negative integer), `k` (an integer), and `l` (a list of integers with a length of at least `c + k + 1`). It swaps the elements at positions `-c - k` and `-c` in the list `l`. After the function executes, the list `l` is returned with these two elements swapped. The element originally at position `-c - k` is now at position `-c`, and the element originally at position `-c` is now at position `-c - k`.

#State of the program right berfore the function call: c is a positive integer, l is a list of integers with at least 2c elements.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` where the element at index `c - 1` is now the value of `x` (which was originally the element at index `-c`), and the element at index `-c` is now the value of `y` (which was originally the element at index `c - 1`). The rest of the elements in the list remain unchanged.
#Overall this is what the function does:The function `func_3` takes a positive integer `c` and a list of integers `l` with at least 2c elements. It swaps the elements at index `c - 1` and index `-c` in the list `l`. The function returns the modified list `l`, where the elements at these two indices have been swapped, while all other elements in the list remain unchanged.

#State of the program right berfore the function call: n is a positive integer, and k is a non-negative integer such that 0 <= k <= 10^12.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two zeros (0, 0).
    #State: `n` and `k` are integers provided by the user input, and `k` is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are integers provided by the user input, and `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0.
    #State: *`n` and `k` are integers provided by the user input, and `k` is even. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is set to `n`. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns the values of `n` and `k`, where `n` is an integer provided by the user, and `k` is an even integer also provided by the user. Additionally, `max_k` is set to `n` (regardless of whether `n` is odd or even), and `max_k` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_4` prompts the user to input two integers, `n` and `k`, where `n` is a positive integer and `k` is a non-negative integer. The function checks if `k` is even. If `k` is odd, the function returns `(0, 0)`. If `k` is even, the function calculates a maximum value `max_k` based on `n` and checks if `k` is less than or equal to `max_k`. If `k` exceeds `max_k`, the function returns `(0, 0)`. Otherwise, the function returns the original values of `n` and `k`.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n where 1 ≤ n ≤ 2 · 10^5.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: All elements of the list `l` have been printed in the order they appear in the list, separated by spaces. The list `l` remains unchanged.
    print()
    #This is printed: (a blank line)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_5` accepts a list `l` of integers representing a permutation of length `n` (where 1 ≤ n ≤ 2 · 10^5). It prints "YES" followed by the elements of the list `l` in the order they appear, separated by spaces. After printing the elements, it prints a blank line. The function does not modify the list `l` and does not return any value.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value.
    #State: *`n` and `k` are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, with new values assigned by `func_4()`. Additionally, `n` is not equal to 0.
    l = func_1(n, k)
    func_5(l)
    return
    #The program does not return any value.
#Overall this is what the function does:The function `func_6` does not accept any parameters and does not return any value. It retrieves two integers `n` and `k` from the function `func_4`. If `n` is 0, it prints 'NO' and terminates. Otherwise, it calls `func_1` with `n` and `k`, and then passes the result to `func_5`. In both cases, the function does not return any value.

