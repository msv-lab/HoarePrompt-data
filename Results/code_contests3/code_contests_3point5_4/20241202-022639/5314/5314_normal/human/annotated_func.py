#State of the program right berfore the function call: n and t are integers such that 1 <= n <= 100 and 1 <= t <= 10^6. The list ai contains n integers where each integer ai is non-negative and less than or equal to 86400.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` and `t` are integers such that 1 <= `n` <= 100 and 1 <= `t` <= 10^6; `ai` contains n non-negative integers less than or equal to 86400, `i` is greater than the number of elements in `ai`
    print(i)
#Overall this is what the function does:The function `func` reads input values for `n` and `t`, as well as a list of `n` integers. It then iterates through the list, subtracting each element from `t` until `t` becomes non-positive. The function prints the index `i` at which `t` becomes non-positive. The function does not explicitly return a value but processes the input data accordingly. It is assumed that the elements in the list `ai` are being accessed correctly within the loop, but missing error handling for out-of-bounds access is a potential issue.

