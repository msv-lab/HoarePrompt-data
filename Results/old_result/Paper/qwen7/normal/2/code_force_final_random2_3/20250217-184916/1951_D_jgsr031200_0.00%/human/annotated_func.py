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
        #The program returns k, which is equal to n since both are positive integers such that 1 ≤ n, k ≤ 10^18.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^18, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^18, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: Output State: `costs` is a list containing the element 1, `h` is the sum of `n // i` for each `i` in `costs` until `n` becomes less than `i`, `n` is reduced to 0.
    #
    #Explanation: After all iterations of the loop, `n` will eventually become less than the smallest value in `costs`, which is `1`. At this point, the loop terminates. The variable `h` accumulates the value of `n // i` for each iteration, where `i` is an element from `costs`. Since `costs` contains `n - k + 1` and `1`, the loop will continue to decrement `n` by `curr` (which is `n // i`) and add `curr` to `h` until `n` is less than `1`. At the end, `n` will be 0, and `h` will hold the total sum of `n // i` for all valid iterations.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: 1
    #State: `costs` is a list containing the element 1, `h` is the sum of `n // i` for each `i` in `costs` until `n` becomes less than `i`, `n` is reduced to 0, and if `h` is less than `k`, the function does not perform any additional operation; if `h` is greater than or equal to `k`, the function ensures that `h` remains greater than or equal to `k` after the operations.
#Overall this is what the function does:The function accepts two parameters, n and k, which are positive integers such that 1 ≤ n, k ≤ 10^18. If n equals k, the function prints 'YES' followed by 1 twice and returns k. If n is less than k, the function prints 'NO' and returns None. If n is greater than or equal to k, the function calculates the sum of n divided by each element in a list containing n - k + 1 and 1, and checks if this sum is at least k. If the sum is less than k, the function prints 'NO'. Otherwise, it prints 'YES', 2, and the list [1].

