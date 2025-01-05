#State of the program right berfore the function call: n and b are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ b ≤ 10^12.**
def func():
    n, b = [int(x) for x in raw_input().split()]
    s = 0
    d_osn = defaultdict(int)
    cur = 2
    while b > 1:
        if b % cur == 0:
            d_osn[cur] += 1
            b /= cur
            continue
        elif cur == 2:
            cur = 3
        else:
            cur += 2
        
        if cur >= b ** 0.5:
            break
        
    #State of the program after the loop has been executed: `n` and `b` are integers within the specified ranges, `s` is 0. `d_osn` is a defaultdict with integer values. The loop has terminated, with `b` being less than or equal to 1. The values in `d_osn` have been updated based on the divisibility of `b` by `cur` during the loop iterations. The final value of `cur` is greater than or equal to the square root of the original value of `b`
    if (b > 2) :
        d_osn[b] += 1
    #State of the program after the if block has been executed: *`n` and `b` are integers within specified ranges, `s` is 0, `d_osn` is a defaultdict with integer values. The loop has terminated, with `b` being less than or equal to 1. The values in `d_osn` have been updated based on the divisibility of `b` by `cur` during the loop iterations. The final value of `cur` is greater than or equal to the square root of the original value of `b`. Additionally, if `b` is greater than 2, then `d_osn[b]` is incremented by 1.
    izv = defaultdict(int)
    res = -1
    for k in d_osn:
        izv = 0
        
        newk = k
        
        newn = n
        
        i = 0
        
        while True and i < 10:
            st = 0
            i += 1
            newizv = 0
            newnewk = newk
            while newnewk <= newn:
                newnewk *= newk
                st += 1
            if st == 0:
                break
            for i in range(st):
                newizv = newizv * 2 + 1
            while newn > newk ** st:
                izv += newizv
                newn = newn - newk ** st
        
        mlt = izv // d_osn[k]
        
        if res == -1:
            res = mlt
        elif mlt < res:
            res = mlt
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, the final values of `st`, `newnewk`, `newk`, `newizv`, `izv`, `newn`, `i`, `mlt`, `res` are all integers. The variables have been updated according to the loop code, and `res` will hold the minimum value of `mlt` calculated during the iterations of the loop. If the loop does not execute at all, the overall state will remain the same as the initial state.
    print(res)
#Overall this is what the function does:The function `func` reads input for two integers `n` and `b` within specified ranges. It then performs a series of calculations and iterations based on the values of `n` and `b`, ultimately calculating and printing a result. The exact nature of the calculation is not explicitly defined in the annotations. Additionally, the function initializes certain variables and data structures for these computations.

