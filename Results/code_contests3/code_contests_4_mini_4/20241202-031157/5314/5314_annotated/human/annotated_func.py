#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100), t is a positive integer (1 ≤ t ≤ 10^6), and ai is a list of n integers where each integer represents the time in seconds Luba has to spend on work during each day (0 ≤ ai ≤ 86400).
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` is a new positive integer (1 ≤ n ≤ 100), `t` is updated to `t - sum(86400 - int(a[j]) for j in range(n))`, `ai` is a list of n integers where each integer represents the time in seconds Luba has to spend on work during each day (0 ≤ ai ≤ 86400), `a` is a list of strings resulting from the split of the input, `i` is `n`
    print(i)
#Overall this is what the function does:The function accepts two positive integers `n` (1 ≤ n ≤ 100) and `t` (1 ≤ t ≤ 10^6), and a list of `n` integers `a`, where each integer represents the time in seconds Luba has to spend on work during each day (0 ≤ ai ≤ 86400). It calculates how many full days Luba can work given the total available time `t`, and prints the number of days (represented by `i`) it takes until the time `t` is no longer sufficient to cover the remaining work time. The function does not return a value but prints the result. If `t` is exhausted before all days are accounted for, `i` will equal `n`, indicating that all available days were processed.

