#State of the program right berfore the function call: n and t are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^6. The list ai contains n non-negative integers where each element ai is between 0 and 86400.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` and `t` are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^6, `a` is a list containing the input split values, `i` is the total number of times the loop executed, `t` is decreased by the sum of 86400 - int(a[j]) for all valid j indices
    print(i)
#Overall this is what the function does:The function `func` reads inputs n and t, and a list of n non-negative integers. It then iterates over the elements of the list subtracting each element from 86400 until t becomes non-positive. The function prints the total number of iterations performed during the loop. The function does not accept any parameters and operates solely based on the predefined variables n, t, and the list a.

