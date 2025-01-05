#State of the program right berfore the function call: n and t are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^6. The list ai contains n non-negative integers where each element is less than or equal to 86400.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: n is a positive integer, ai contains n non-negative integers where each element is less than or equal to 86400, i is equal to the number of elements in ai, t is a positive integer
    print(i)
#Overall this is what the function does:The function `func` reads input values `n` and `t`, then processes a list `ai` containing `n` non-negative integers where each element is less than or equal to 86400. It iterates through the list `ai` decrementing `t` by 86400 minus the current element until `t` becomes non-positive. The function prints the number of elements processed `i`. It does not explicitly return any value. There is a missing edge case where `t` might become negative before processing all elements of `ai`.

