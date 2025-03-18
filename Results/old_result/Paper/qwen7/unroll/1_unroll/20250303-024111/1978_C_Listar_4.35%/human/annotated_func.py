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
        
    #State: Output State: `l` is a list where the last element of the original list moves to the front, and this process repeats until `k` becomes 0 or we can't satisfy the condition `1 + i > k`. If `k` becomes 0 before completing all iterations, the list remains unchanged from its final state just before the return statement. If the loop completes all iterations without `k` becoming 0, the list will be reversed.
#Overall this is what the function does:The function accepts two parameters, `n` (an integer between 1 and 2 * 10^5 inclusive) and `k` (an integer between 0 and 10^12 inclusive). It manipulates a list `l` containing integers from 1 to `n` by moving the last element to the front repeatedly until `k` becomes 0 or the operation cannot be performed due to the value of `k`. If `k` becomes 0 before completing all iterations, the list remains unchanged from its final state just before the return statement. If the loop completes all iterations without `k` becoming 0, the list will be reversed. The function returns the modified list `l`.

#State of the program right berfore the function call: (n, k) are integers such that 1 ≤ n ≤ 2 \cdot 10^{5} and 0 ≤ k ≤ 10^{12}.
def func_2():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two zeros (0, 0)
    #State: `n` is an integer input from the user, `k` is an integer input from the user, and both are within the specified ranges. The value of `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: Postcondition: `n` and `k` are integers. If `n` is odd, `max_k` is calculated as `(n * n + k) / 2`. If `n` is even, `max_k` is set to `n`.
    if (max_k < k) :
        return 0, 0
        #The program returns 0, 0
    #State: Postcondition: `n` and `k` are integers, `max_k` is set to `n` (since `n` is even), and `max_k` is not less than `k`.
    return n, k
    #The program returns n and k, where n is an integer and k is an integer, and max_k is set to n (since n is even) and is not less than k.
#Overall this is what the function does:The function reads two integers, \( n \) and \( k \), from the user. It then checks if \( k \) is odd and returns (0, 0) if true. If \( k \) is even, it calculates \( max_k \) based on whether \( n \) is odd or even. If \( max_k \) is less than \( k \), it returns (0, 0). Otherwise, it returns \( n \) and \( k \). The function can return either (0, 0) or a pair consisting of \( n \) and \( k \).

#State of the program right berfore the function call: l is a list of integers where each integer represents a position in the permutation. The length of the list is equal to the required Manhattan value k, and the values in the list are such that they can form a valid permutation of length n.
def func_3(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: 1 2 3 ... (n-1) n
    print()
    #This is printed: an empty line
    return
    #The program returns None
#Overall this is what the function does:The function accepts a list of integers `l` representing positions in a permutation and prints "YES" followed by the elements of the list on a single line separated by spaces. It then prints an empty line and returns nothing (`None`).

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2·10^5, and k is an integer such that 0 ≤ k ≤ 10^12.
def func_4():
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: `n` is an integer such that 1 ≤ n ≤ 2·10^5, `k` is an integer such that 0 ≤ k ≤ 10^12, and `n, k = func_2()` has been called, and `n` is not equal to 0
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns the value returned by func_3(l), where l is the return value of func_1(n, k)
#Overall this is what the function does:The function first calls `func_2()` to get values for `n` and `k`. If `n` is 0, it prints 'NO' and returns None. Otherwise, it calculates a value `l` using `func_1(n, k)` and then calls `func_3(l)`, returning whatever `func_3(l)` returns. If `func_3(l)` returns something, the function returns that value; otherwise, it returns None.

