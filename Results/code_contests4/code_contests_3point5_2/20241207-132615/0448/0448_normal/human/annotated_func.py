#State of the program right berfore the function call: **Precondition**: **n and m are positive integers such that 1 <= n, m <= 10^5. hi and pi are distinct integers in ascending order such that 1 <= hi, pi <= 10^10 and hi < hi + 1, pi < pi + 1.**
def func_1():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))
    ss, ll = 0, int(21000000000.0)
    while ss < ll:
        avg = (ss + ll) // 2
        
        works = True
        
        hidx = 0
        
        pidx = 0
        
        while hidx < len(h) and pidx < len(p):
            leftget = p[pidx]
            curpos = h[hidx]
            if curpos - leftget > avg:
                works = False
                break
            getbacktime = max(0, 2 * (curpos - leftget))
            alsotoright = max(0, avg - getbacktime)
            leftime = max(0, curpos - leftget)
            remtime = max(0, (avg - leftime) // 2)
            furthestright = curpos + max(alsotoright, remtime)
            while pidx < len(p) and p[pidx] <= furthestright:
                pidx += 1
            hidx += 1
        
        if pidx != len(p):
            works = False
        
        if works:
            ll = avg
        else:
            ss = avg + 1
        
    #State of the program after the loop has been executed: If `works` is True and `pidx` is not equal to len(p), then `hidx`, `pidx`, `leftget`, `curpos`, `getbacktime`, `alsotoright`, `leftime`, `remtime`, `furthestright` maintain their previous values. If `works` is False, then `ss` is assigned the value of `avg + 1` and no other variables are affected. After the loop finishes, the final values of `ss`, `ll`, `avg`, `works`, `hidx`, `pidx`, `leftget`, `curpos`, `getbacktime`, `alsotoright`, `leftime`, `remtime`, `furthestright` will depend on the conditions met during the loop execution.
    print(ss)
#Overall this is what the function does:The function `func_1` reads input, performs a binary search algorithm to find a suitable value, and then prints the value of `ss`. The binary search algorithm involves checking certain conditions using the variables `works`, `hidx`, `pidx`, and various calculations. If the conditions are met, `ll` is updated to `avg`; otherwise, `ss` is updated to `avg + 1`. The loop continues until `ss` is no longer less than `ll`. The function does not accept any parameters and does not have a return value.

