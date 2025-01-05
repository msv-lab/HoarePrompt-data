#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, t is an integer such that 1 ≤ t ≤ 10^6, and ai is an integer for each day i (1 ≤ i ≤ n) such that 0 ≤ ai ≤ 86400.
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is an integer such that 1 ≤ `t` ≤ 10^6 minus the sum of `86400 - int(a[0]), 86400 - int(a[1]), ..., 86400 - int(a[i-1])`, `i` is equal to the number of iterations executed (which is the minimum of the length of `a` and the maximum number of times the loop can execute before `t` becomes non-positive). If `t` reached 0 or less, the loop terminated; otherwise, `i` is equal to the length of `a` if all elements were processed.
    print(i)
#Overall this is what the function does:The function accepts no parameters directly but reads two integers, `n` (1 ≤ n ≤ 100) and `t` (1 ≤ t ≤ 10^6), from input, followed by a list of integers representing daily values `ai` (0 ≤ ai ≤ 86400) for each day. It calculates how many days can be processed before the total available time `t` becomes non-positive, deducting `86400 - ai` from `t` for each day processed. The function returns the count of days that can be processed before `t` is exhausted. If `t` reaches 0 or less, the loop stops, and `i` represents the number of days processed. If all days are processed and `t` is still positive, `i` will equal `n`.

