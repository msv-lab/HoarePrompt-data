#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100), t is a positive integer (1 ≤ t ≤ 10^6), and a is a list of n integers where each integer ai represents the time Luba has to spend on work during the i-th day (0 ≤ ai ≤ 86400).
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is the remaining time after subtracting the total of (86400 - int(a[i])) for all valid indices i processed, `i` is equal to the number of elements processed from the list `a`, which is the value of the initial `n`, and `a` remains unchanged as a list of n integers.
    print(i)
#Overall this is what the function does:The function accepts two positive integers `n` and `t`, and a list of `n` integers representing work times. It calculates how many days Luba can work before the total available time `t` becomes non-positive and prints that count. If `t` is initially non-positive, it will print `0`.

