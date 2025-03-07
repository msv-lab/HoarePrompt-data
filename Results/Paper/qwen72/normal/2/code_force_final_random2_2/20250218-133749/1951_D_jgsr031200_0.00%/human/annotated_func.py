#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^18.
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
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^18, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^18, and n is not equal to k. Additionally, n is greater than or equal to k.
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: After the loop executes all iterations, `n` is 0, `k` remains a positive integer such that 1 ≤ k ≤ 10^18, `n` is not equal to `k`, `n` is less than `k`, `costs` is `[n - k + 1, 1]`, `h` is the sum of the quotients from dividing `n` by each element in `costs` during the loop, `i` is 1, and `curr` is 0.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: -k + 1, 1 (where k is a positive integer such that 1 ≤ k ≤ 10^18)
    #State: *After the loop executes all iterations, `n` is 0, `k` remains a positive integer such that 1 ≤ k ≤ 10^18, `n` is not equal to `k`, `n` is less than `k`, `costs` is `[n - k + 1, 1]`, `h` is the sum of the quotients from dividing `n` by each element in `costs` during the loop, `i` is 1, and `curr` is 0. If `h` is less than `k`, the condition `h < k` holds. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` takes two positive integers, `n` and `k`, both within the range 1 ≤ n, k ≤ 10^18, and performs the following actions based on their values:

1. If `n` equals `k`, it prints 'YES', followed by three lines each containing the number 1, and then exits without returning any value.
2. If `n` is less than `k`, it prints 'NO' and exits without returning any value.
3. If `n` is greater than or equal to `k` and not equal to `k`, it calculates a list `costs` with elements `[n - k + 1, 1]`. It then iterates over these costs, updating `n` and a variable `h` which accumulates the quotient of `n` divided by each cost. After the loop, if `h` is less than `k`, it prints 'NO'. Otherwise, it prints '2', 'YES', and the elements of `costs`.

In all cases, the function does not return any value.

