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
        #The program returns k, which is equal to n since both are positive integers such that 1 ≤ n, k ≤ 10^18.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: 'NO'
        return
        #The program returns None
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: Output State: `h` is 2, `n` is -1, `k` is a positive integer, `costs` is [1 - k, 1].
    #
    #Explanation: After the loop executes all its iterations, the value of `h` remains 2 because each iteration adds `n // i` to `h` and decreases `n` by `i * curr`. The loop terminates when `n` becomes less than the smallest element in `costs`, which is 1. Since `n` is reduced to -1, it means that the loop has completed all its iterations. The value of `k` remains unchanged as it was not modified within the loop. The `costs` list also remains unchanged as it was not modified during the loop's execution.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: 1 - k 1
    #State: `h` is 2, `n` is -1, `k` is a positive integer, `costs` is [1 - k, 1]. If `h` is less than `k`, no changes occur. If `h` is greater than or equal to `k`, no changes occur either since the loop does not modify these variables.
#Overall this is what the function does:The function accepts two parameters, n and k, which are positive integers such that 1 ≤ n, k ≤ 10^18. If n equals k, the function prints 'YES', then prints 1 three times, and returns k. If n is less than k, the function prints 'NO' and returns None. If n is greater than or equal to k, the function calculates the minimum number of operations required to reduce n to a non-positive value using the values in the list [n - k + 1, 1], and prints 'YES', 2, the list [n - k + 1, 1], and 'NO' if the calculated number of operations (h) is less than k. Otherwise, it prints 'YES'. The function returns None in all cases except when n equals k.

