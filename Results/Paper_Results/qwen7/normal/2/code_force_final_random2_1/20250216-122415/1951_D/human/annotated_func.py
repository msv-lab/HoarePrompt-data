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
        #The program returns k, which is equal to n
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: Output State: `h` is the sum of all `curr` values calculated during the loop iterations, `n` is reduced to a non-positive value (since it keeps decreasing by `i * curr` in each iteration until it becomes zero or negative), `k` is a positive integer, `costs` is a list containing one element: `1`.
    #
    #In simpler terms, after all iterations of the loop have finished, `h` will be the total of all `curr` values calculated during each iteration, `n` will be reduced to zero or a negative number (depending on the values of `i` and `curr`), `k` remains unchanged as it is not affected by the loop, `costs` will be left with a single element `1` after the first element is consumed in the loop iterations.
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
    #State: `h` is the sum of all `curr` values calculated during the loop iterations, `n` is reduced to zero or a negative value (depending on the values of `i` and `curr`), `k` remains a positive integer, `costs` is left with a single element `1`.
#Overall this is what the function does:The function accepts two parameters, n and k, both of which are positive integers between 1 and 10^18. If n equals k, it prints 'YES' followed by 1 twice and returns k. If n is less than k, it prints 'NO' and returns None. If n is greater than or equal to k, it calculates the sum of certain values and prints 'NO' if this sum is less than k. Otherwise, it prints 'YES', 2, 'YES' again, and the list [1]. Regardless of the case, the function returns None.

