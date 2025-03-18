#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2 * 10^5, and k is an integer such that 0 <= k <= 10^12.
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
        
    #State: Output State: `l` is a list where the last element is moved to the front, repeated until `k` becomes zero or less, and the process stops early if the condition `1 + i > k` is met for any iteration.
#Overall this is what the function does:The function accepts two parameters, `n` (an integer between 1 and 2 * 10^5) and `k` (an integer between 0 and 10^12). It manipulates a list `l` containing integers from 1 to `n` by moving the last element to the front repeatedly until `k` becomes zero or less. If the condition `1 + i > k` is met during the iteration, the function stops early. The final state of the list `l` is returned.

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 \cdot 10^{5} and 0 ≤ k ≤ 10^{12}.
def func_2():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two zeros (0, 0)
    #State: `n` is an integer such that 1 ≤ n ≤ 2 * 10^5, `k` is an integer such that 0 ≤ k ≤ 10^12, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: Postcondition: `n` is an integer such that 1 ≤ n ≤ 2 * 10^5, `k` is an integer such that 0 ≤ k ≤ 10^12, and `k` is even. If `n` is odd, `max_k` is (n - 1) / 2. If `n` is even, `max_k` is `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns two zeros (0, 0)
    #State: Postcondition: `n` is an integer such that 1 ≤ n ≤ 2 * 10^5, `k` is an integer such that 0 ≤ k ≤ 10^12, and `k` is even, and `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns n, which is an integer such that 1 ≤ n ≤ 2 * 10^5, and k, which is an integer such that 0 ≤ k ≤ 10^12 and k is even.
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from the input, where \( 1 \leq n \leq 2 \times 10^5 \) and \( 0 \leq k \leq 10^{12} \). It then checks if \( k \) is even. If \( k \) is odd, it returns two zeros (0, 0). Otherwise, it calculates the maximum possible value of \( k \) based on \( n \), and if \( k \) exceeds this maximum, it also returns two zeros (0, 0). If \( k \) is within the valid range, it returns \( n \) and \( k \).

#State of the program right berfore the function call: l is a list of integers representing a valid permutation of length n such that the Manhattan value of the permutation is equal to k.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The elements of the list l printed in the same order they appear in the list, separated by a space.
    print()
    #This is printed: ''
    return
    #The program returns an empty value since there is no value being returned in the given code.
#Overall this is what the function does:The function accepts a list of integers `l` representing a valid permutation of length `n` with a Manhattan value equal to `k`. It prints "YES" followed by each element of the list `l` separated by a space. After printing, the function concludes without returning any value.

#State of the program right berfore the function call: (n, k) are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ 10^12. n is the length of the permutation, and k is the required Manhattan value.
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: 'NO'
        return
        #The program returns 0 for `n` and an integer `k` such that 0 ≤ k ≤ 10^12
    #State: `n` is an integer such that 1 ≤ n ≤ 2⋅10^5; `k` is an integer such that 0 ≤ k ≤ 10^12; `n` and `k` are the return values of `func_2()`. `n` is not equal to 0
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns None
#Overall this is what the function does:The function accepts no direct parameters but uses values `n` and `k` obtained from `func_2()`. If `n` is not zero, it calls `func_1(n, k)` and then `func_3(l)`, where `l` is the result of `func_1(n, k)`. If `n` is zero, it prints 'NO' and returns immediately. The function returns 0 under certain conditions or None otherwise.

