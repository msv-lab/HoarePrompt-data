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
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^18, n is not equal to k, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: `n` is 0, `k` is a positive integer such that 1 ≤ k ≤ 10^18, `n` is not equal to `k`, `n` is less than `k`, `costs` is a list containing two elements: `[1 - k, 1]`, `h` is the sum of the initial value of `n` divided by each element in `costs`, and `curr` is 0.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: - The first element of `costs` is `1 - k`.
        #   - The second element of `costs` is `1`.
        #
        #Therefore, the output of the `print` statement will be:
        #Output:
    #State: *`n` is 0, `k` is a positive integer such that 1 ≤ k ≤ 10^18, `n` is not equal to `k`, `n` is less than `k`, `costs` is a list containing two elements: `[1 - k, 1]`, `h` is the sum of the initial value of `n` divided by each element in `costs`, and `curr` is 0. If `h` is less than `k`, the program follows the logic for the if part. If `h` is greater than or equal to `k`, the program follows the logic for the else part.
#Overall this is what the function does:The function `func_1` takes two positive integers `n` and `k` (both within the range 1 to 10^18) as input. It prints 'YES' and the number 1 three times if `n` equals `k`. If `n` is less than `k`, it prints 'NO'. If `n` is greater than or equal to `k`, it calculates a series of values and prints either 'NO' if the calculated sum `h` is less than `k`, or '2', 'YES', and the two elements of the list `costs` if `h` is greater than or equal to `k`. The function does not return any value in any case.

