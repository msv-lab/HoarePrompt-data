#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and k is an integer such that 0 ≤ k ≤ 10^12.
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
        
    #State: Output State: `l` is a list where the elements are rotated to the left by `k` positions. If `k` is greater than the length of the list, the rotation wraps around. The list initially contains integers from 1 to `n` inclusive.
#Overall this is what the function does:The function accepts two parameters, `n` (an integer between 1 and 200,000) and `k` (an integer between 0 and 1,000,000,000,000), and returns a list of integers from 1 to `n` inclusive, rotated to the left by `k` positions. If `k` is greater than `n`, the rotation wraps around.

#State of the program right berfore the function call: (n, k) are integers such that 1 ≤ n ≤ 2 \cdot 10^{5} and 0 ≤ k ≤ 10^{12}.
def func_2():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two zeros (0, 0)
    #State: `n` is an integer obtained from the first number input, `k` is an integer obtained from the second number input, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: Postcondition: `n` is an integer, `k` is an even integer. If `n` is odd, `max_k` is set to `n`. If `n` is even, `max_k` is also set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns two zeros (0, 0)
    #State: Postcondition: `n` is an integer, `k` is an even integer. `max_k` is set to `n`.
    return n, k
    #The program returns n and k, where n is an integer and k is an even integer.
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from the user. It then checks if \( k \) is even and if \( n \) is odd or even, setting a maximum value for \( k \) based on \( n \). If \( k \) exceeds this maximum value, it returns (0, 0). Otherwise, it returns \( n \) and \( k \). The function can return either (0, 0) or (n, k), where \( n \) is an integer and \( k \) is an even integer.

#State of the program right berfore the function call: l is a list of integers representing a valid permutation of length n such that the Manhattan value of the permutation is equal to k.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The elements of the list l printed in the same order, separated by spaces.
    print()
    #This is printed: ''
    return
    #The program returns nothing
#Overall this is what the function does:The function accepts a list `l` of integers representing a valid permutation of length `n` such that the Manhattan value of the permutation is equal to `k`. It prints "YES" followed by the elements of the list `l` separated by spaces. After printing, the function returns nothing.

#State of the program right berfore the function call: (n, k) are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: `n` is an integer such that 1 <= n <= 2 * 10^5; `k` is an integer such that 0 <= k <= 10^12. `n` is not equal to 0
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns the result of calling function `func_3(l)`, where `l` is the result of the function call `func_1(n, k)`
#Overall this is what the function does:The function accepts no parameters and returns either `None` or the result of calling `func_3(l)`, where `l` is the result of the function call `func_1(n, k)`. If `n` is 0, the function prints 'NO' and returns `None`. Otherwise, it proceeds to call `func_1(n, k)` with the given constraints on `n` and `k`, then calls `func_3(l)` with the result of `func_1(n, k)`, and returns the result of this call.

