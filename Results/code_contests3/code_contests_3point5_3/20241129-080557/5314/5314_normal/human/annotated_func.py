#State of the program right berfore the function call: n and t are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^6. Each ai is a non-negative integer such that 0 <= ai <= 86400.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: 'n' and 't' are positive integers within the specified ranges, 'a' is a list of strings obtained by splitting the input, 'i' is equal to the total number of elements in 'a', 't' is updated based on the calculation mentioned above
    print(i)
#Overall this is what the function does:The function `func` reads input values for `n` and `t`, and a list of integers `a`. It then iterates through the elements of `a` subtracting each from `t` until `t` becomes zero or negative. The function prints the total number of elements processed (variable `i`). The function does not return any value. Potential edge cases or missing functionality: If the sum of elements in `a` exceeds `t` before iterating through all elements, the loop will exit prematurely, and `i` might not represent the total number of elements processed. Additionally, the function does not handle cases where the input values do not meet the specified constraints.

