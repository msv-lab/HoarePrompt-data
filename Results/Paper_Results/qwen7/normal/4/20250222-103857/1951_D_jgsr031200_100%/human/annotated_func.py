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
        #The program returns the integer n, which is equal to k.
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
        
    #State: Output State: After the loop executes all the iterations, `h` will be the sum of `curr` for each iteration, where `curr` is calculated as `n // i` for each `i` in `costs`. `n` will be reduced by `i * curr` for each iteration until `n` becomes less than the smallest value in `costs`.
    #
    #In more detail, `h` will accumulate the quotient of `n` divided by each element in `costs`, and `n` will be successively reduced by the product of each element in `costs` and its corresponding quotient, until `n` is no longer sufficient to divide by any element in `costs`.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: [list of elements in costs]
    #State: `h` is the sum of `curr` for each iteration, where `curr` is calculated as `n // i` for each `i` in `costs`. `n` is successively reduced by the product of each element in `costs` and its corresponding quotient, until `n` is no longer sufficient to divide by any element in `costs`. If `h` is less than `k` at the end of the process, the function continues as if `h` were less than `k`. Otherwise, the function ensures that `h` is at least `k` after the process completes.
#Overall this is what the function does:The function accepts two parameters, n and k, both of which are positive integers between 1 and 10^18. If n equals k, it prints 'YES' followed by 1, 1, and then returns n. If n is less than k, it prints 'NO' and returns None. If n is greater than or equal to k, it calculates the sum of quotients obtained by dividing n by each element in a list [n-k+1, 1], reducing n accordingly. If this sum is less than k, it prints 'NO' and returns None; otherwise, it prints 'YES', 2, and the list [n-k+1, 1].

