#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and k is an integer such that 0 ≤ k ≤ 10^12.
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
        
    #State: The loop will continue to decrement `i` by 2 until `i` is no longer less than or equal to -1. At that point, the loop will terminate. Since `i` starts from `n` and decreases by 2 each iteration, eventually `i` will reach -1 or less. The final value of `c` will be `n // 2`, as `i` decreases by 2 each time and the loop runs `n // 2` times. `k` will be adjusted in each iteration according to the rule `k = k - i + 1`, and `l` will be updated to the return value of `func_3(c, l)` after each adjustment of `k`.
#Overall this is what the function does:The function `func_1` accepts two parameters `n` and `k`, where `n` is an integer between 1 and 2 * 10^5, and `k` is an integer between 0 and 10^12. It may return an undefined value, call `func_2` with specific arguments, call `func_3` with specific arguments, return the value of `l`, return `i - 2`, or call `func_2` with the current values of `c`, `k`, and `l` based on certain conditions involving `c`, `i`, and `k`. The function iteratively updates `k` and `l` by calling `func_3` and adjusts `i` by decrementing it by 2 in each iteration. The loop continues until `i` is no longer less than or equal to -1.

#State of the program right berfore the function call: c is a non-negative integer such that 0 <= c < len(l), k is an integer such that 0 <= k < len(l), and l is a list of integers representing a permutation of length n.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` with the elements at indices `-c` and `-c - k` swapped.
#Overall this is what the function does:The function accepts three parameters: `c` (a non-negative integer), `k` (an integer), and `l` (a list of integers representing a permutation). After executing, it returns the list `l` with the elements at indices `-c` and `-c - k` swapped.

#State of the program right berfore the function call: c is an integer such that 1 <= c <= len(l)/2, and l is a list of integers representing a permutation of length n.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` unchanged.
#Overall this is what the function does:The function accepts an integer `c` and a list `l` of integers. It swaps the elements at positions `c-1` and `len(l)-c` in the list `l`, then returns the modified list. However, due to the swap operation, the returned list is identical to the input list `l`.

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 0 ≤ k ≤ 10^{12}.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two zeros (0, 0)
    #State: `n` is an integer obtained from the first input split, `k` is an integer obtained from the second input split, and `k` is divisible by 2
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: Postcondition: `n` is an integer obtained from the first input split, and `k` is an integer obtained from the second input split, and is divisible by 2. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is also set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns two values both as 0.
    #State: Postcondition: `n` is an integer obtained from the first input split, and `k` is an integer obtained from the second input split, and is divisible by 2. `max_k` is set to `n`, and `max_k` is not less than `k`.
    return n, k
    #The program returns n and k, where n is an integer obtained from the first input split, and k is an integer obtained from the second input split and is divisible by 2.
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from input, where \( 1 \leq n \leq 2 \cdot 10^5 \) and \( 0 \leq k \leq 10^{12} \). It then checks if \( k \) is divisible by 2. If \( k \) is not divisible by 2, it returns two zeros (0, 0). If \( k \) is divisible by 2, it calculates \( max_k \) based on whether \( n \) is odd or even. If \( max_k \) is less than \( k \), it returns two zeros (0, 0). Otherwise, it returns \( n \) and \( k \).

#State of the program right berfore the function call: l is a list of integers where each integer represents a permutation of length n (1 ≤ n ≤ 2 \cdot 10^{5}) that has been determined to have a Manhattan value equal to k (0 ≤ k ≤ 10^{12}). Each integer in the list is a valid permutation and is distinct.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: Output State: The loop will have printed all elements of the list `l` separated by spaces.
    #
    #Explanation: Given that the loop iterates over each element in the list `l` and prints them one by one using `print(i, end=' ')`, after all iterations of the loop have finished, it means every integer (permutation) in the list `l` has been printed exactly once, with no newline character (`\n`) added between them due to the `end=' '` parameter in the `print` function. Therefore, the output will be a single line containing all the elements of `l` in the order they were originally listed, separated by spaces.
    print()
    #This is printed: \n
    return
    #The program returns nothing
#Overall this is what the function does:The function accepts a list of integers, where each integer represents a permutation of length n (1 ≤ n ≤ 2 ⋅ 10^5) with a Manhattan value equal to k (0 ≤ k ≤ 10^12). It prints each permutation on the same line, separated by spaces, and then returns nothing.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and k is an integer such that 0 ≤ k ≤ 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns the new values of `n` and `k` after the function `func_4()` has been called.
    #State: `n` is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and `k` is an integer such that 0 ≤ k ≤ 10^12, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns the result of `func_5(func_1(n, k))`
#Overall this is what the function does:The function does not accept any parameters and returns either the new values of `n` and `k` after calling `func_4()`, or the result of `func_5(func_1(n, k))` based on whether `n` is zero. If `n` is zero, the function prints 'NO' and returns immediately. Otherwise, it calculates `l` using `func_1(n, k)`, calls `func_5(l)`, and then returns the result of `func_5(func_1(n, k))`.

