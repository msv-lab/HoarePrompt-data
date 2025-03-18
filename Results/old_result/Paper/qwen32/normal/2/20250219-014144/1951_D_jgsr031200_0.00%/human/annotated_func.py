#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
def func_1(n, k):
    if (n == k) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(1)
        #This is printed: 1
        return
        #The program does not return any value.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, n is not equal to k, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: n is 0, k is a positive integer such that \(1 \leq k \leq 10^{18}\), costs is a list containing \([n - k + 1, 1]\), h is \(n // (n - k + 1) + n\), curr is 0, i is 1.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: -k + 1 1
    #State: `n` is 0, `k` is a positive integer such that \(1 \leq k \leq 10^{18}\), `costs` is a list containing \([n - k + 1, 1]\), `curr` is 0, `i` is 1. If `h` is less than `k`, then `h` remains as \(n // (n - k + 1) + n\) which simplifies to 0. If `h` is greater than or equal to `k`, then `h` remains as \(n // (n - k + 1) + n\) which also simplifies to 0.
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `n` and `k` within the range 1 to \(10^{18}\). It prints 'YES' and additional information if `n` can be reduced to 0 by subtracting multiples of `n - k + 1` and 1, such that the total number of subtractions is at least `k`. Otherwise, it prints 'NO'. The function does not return any value.

