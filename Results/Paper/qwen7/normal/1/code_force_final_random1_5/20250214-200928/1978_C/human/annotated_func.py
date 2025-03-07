#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2⋅10^5, and k is an integer such that 0 ≤ k ≤ 10^12.
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
        
    #State: Output State: `c` is equal to the total number of iterations the loop executed, `n` is an integer such that \(1 \leq n \leq 2 \cdot 10^5\), `i` is `n - 2 * (number_of_iterations - 1)`, `k` is reduced by the sum of all `i` values minus the number of iterations plus 1, and `l` is the result of repeatedly applying `func_3(c, l)` for each iteration of the loop.
    #
    #In simpler terms, after the loop completes all its iterations, `c` will be the total number of times the loop ran, which is determined by the value of `n` and how many times the loop condition `range(n, -1, -2)` holds true. The variable `i` will be `n` minus twice the number of iterations minus 2. The variable `k` will be reduced by the sum of all `i` values minus the number of iterations plus 1. Finally, `l` will be the result of repeatedly applying `func_3(c, l)` for each iteration of the loop.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 1 and 200,000 inclusive, and `k` is an integer between 0 and 10^12 inclusive. It processes these inputs through a series of operations, including updating `k` and calling other functions (`func_2` and `func_3`). Depending on the conditions met during its execution, it may return either the result of `func_2(c, k, l)` with `c` being 1 or 2, or the result of `func_3(3, l)`. If `k` reaches 0 before the loop completes, it returns `l` directly. The final state of the program includes the count of loop iterations (`c`), the adjusted value of `k`, and the transformed list `l` resulting from repeated applications of `func_3`.

#State of the program right berfore the function call: c is a non-negative integer such that c < len(l), k is an integer such that 0 <= k <= c, and l is a list of integers representing a permutation of length n.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` which is a permutation of length `n`
#Overall this is what the function does:The function accepts three parameters: `c` (a non-negative integer less than the length of the list `l`), `k` (an integer between 0 and `c` inclusive), and `l` (a list of integers representing a permutation of length `n`). It swaps the elements at positions `c` and `c - k` in the list `l`. After performing the swap, it returns the modified list `l`, which remains a permutation of length `n`.

#State of the program right berfore the function call: c is a positive integer such that 1 <= c <= len(l)/2, and l is a list of integers representing a permutation of length n.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns list `l` with the elements at index `c - 1` and `-c` swapped.
#Overall this is what the function does:The function accepts two parameters: `c`, a positive integer within the range 1 to half the length of the list `l`, and `l`, a list of integers representing a permutation. It returns the list `l` with the elements at index `c - 1` and `-c` swapped.

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 \cdot 10^{5} and 0 ≤ k ≤ 10^{12}.
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
    #State: Postcondition: `n` is an integer obtained from the first input split, `k` is an integer obtained from the second input split and is divisible by 2, and `max_k` is set to `n` if `n` is even, otherwise `max_k` is set to the value of `n` plus 5.
    if (max_k < k) :
        return 0, 0
        #The program returns 0 and 0
    #State: Postcondition: `n` is an integer obtained from the first input split, `k` is an integer obtained from the second input split and is divisible by 2, and `max_k` is set to `n` plus 5 if `n` is odd, otherwise `max_k` is set to `n`.
    return n, k
    #The program returns n and k, where n is an integer obtained from the first input split and k is an integer obtained from the second input split and is divisible by 2.
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from the input, where \( 1 \leq n \leq 2 \cdot 10^5 \) and \( 0 \leq k \leq 10^{12} \). It then checks if \( k \) is divisible by 2. If \( k \) is not divisible by 2, it returns two zeros (0, 0). If \( k \) is divisible by 2, it calculates a maximum value \( max_k \) based on \( n \). If \( max_k \) is less than \( k \), it returns two zeros (0, 0). Otherwise, it returns \( n \) and \( k \).

#State of the program right berfore the function call: l is a list of integers representing a valid permutation of length n such that the Manhattan value of this permutation is equal to k.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: Output State: The loop has executed all its iterations, printing each element of the list `l` exactly once in the order they appear. `l` is a list of integers representing a valid permutation of length `n` such that the Manhattan value of this permutation is equal to `k`.
    #
    #In simpler terms, the loop has printed every number in the list `l` from start to end, one by one, without repeating any numbers.
    print()
    #This is printed: \n
    return
    #The program does not return any value since there is no return statement in the given code snippet.
#Overall this is what the function does:The function accepts a list of integers `l` representing a valid permutation of length `n` such that the Manhattan value of this permutation is equal to `k`. It prints "YES" followed by each element of the list `l` on the same line separated by spaces. After executing the loop, it prints a newline character. The function does not return any value.

#State of the program right berfore the function call: (n, k) are integers where 1 ≤ n ≤ 2 \cdot 10^{5} and 0 ≤ k ≤ 10^{12}.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value since there is no return statement in the provided code snippet.
    #State: `n` is an integer where 1 ≤ n ≤ 2 \cdot 10^{5}; `k` is an integer where 0 ≤ k ≤ 10^{12}; `n` and `k` are the results of `func_4()` call, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns the value of `l` which is the result of `func_5(func_1(n, k))`
#Overall this is what the function does:The function does not accept any parameters. It first calls `func_4()` to get values for `n` and `k`. If `n` is 0, it prints 'NO' and does not return any value. Otherwise, it calculates a value `l` using `func_1(n, k)` and then processes `l` using `func_5(l)`. Finally, it returns the value of `l`, which is the result of `func_5(func_1(n, k))` if `n` is not 0.

