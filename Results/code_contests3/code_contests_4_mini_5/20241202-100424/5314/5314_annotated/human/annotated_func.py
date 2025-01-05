#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, t is an integer such that 1 ≤ t ≤ 10^6, and ai is a list of n integers where each ai is between 0 and 86400 (inclusive).
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is decreased by the sum of values `86400 - int(a[j])` for each `j` from 0 to `i-1`, `i` is the number of iterations executed, which is equal to the total elements processed from the list `a` until `t` becomes non-positive, and `n` is an integer such that 1 ≤ `n` ≤ 100; `ai` is a list of `n` integers where each `ai` is between 0 and 86400 (inclusive).
    print(i)
#Overall this is what the function does:The function accepts an integer `n`, an integer `t`, and a list of `n` integers, then counts how many iterations it can perform by reducing `t` based on the values in the list until `t` is non-positive, and prints the count of iterations.

