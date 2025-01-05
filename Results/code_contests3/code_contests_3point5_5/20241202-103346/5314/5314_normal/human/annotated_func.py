#State of the program right berfore the function call: n and t are integers such that 1 ≤ n ≤ 100 and 1 ≤ t ≤ 10^6. The list ai contains n integers where each ai is non-negative and does not exceed 86400.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: After the loop finishes executing, `i` is equal to the total number of elements in the list `ai`, `n` remains unchanged, and `t` is a non-negative integer less than 86400
    print(i)
#Overall this is what the function does:The function accepts user input for two integers n and t, and a list a containing n non-negative integers. It then iterates through the list elements subtracting each element from t until t becomes less than or equal to 0. The function prints the total number of elements processed before t becomes non-positive.

