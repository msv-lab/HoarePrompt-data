#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, t is an integer such that 1 ≤ t ≤ 10^6, and ai is a list of n integers where each ai (0 ≤ ai ≤ 86400) represents the time Luba has to spend working on the i-th day.
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is decremented by the total of `86400 - int(a[j])` for each `j` from 0 to `i-1`; `i` is the count of how many iterations the loop executed, which is equal to the number of elements processed from list `a` until `t` becomes non-positive; `n` is an integer such that 1 ≤ `n` ≤ 100; `ai` is a list of `n` integers.
    print(i)
#Overall this is what the function does:The function accepts two integers `n` and `t`, and a list of `n` integers representing the time Luba has to work each day. It calculates how many days can be processed before the total available time `t` becomes non-positive, by decrementing `t` with the difference between 86400 (total seconds in a day) and each day's work time. The function returns the count of how many days were processed before `t` runs out. If `t` starts high enough, it may process all `n` days; if `t` is low, it may process fewer. However, it does not handle cases where the list `a` has fewer elements than `n`, leading to potential index errors if `t` does not become non-positive before the list is exhausted.

