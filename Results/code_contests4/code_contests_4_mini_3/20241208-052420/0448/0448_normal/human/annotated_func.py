#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 100,000; h is a list of n distinct integers (1 ≤ hi ≤ 10^10) representing the initial positions of the heads in ascending order; p is a list of m distinct integers (1 ≤ pi ≤ 10^10) representing the tracks to read in ascending order.
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
        
    #State of the program after the loop has been executed: `hidx` is equal to the length of `h`, `pidx` is equal to the length of `p`, `furthestright` is the last computed value based on the final `curpos`, `ss` is greater than or equal to `ll`, and `ll` is the minimum average time that works for all positions.
    print(ss)
#Overall this is what the function does:The function accepts two integers `n` and `m`, a list `h` of `n` distinct integers representing head positions, and a list `p` of `m` distinct integers representing track positions. It calculates the minimum average time required for all head positions to reach their respective track positions and prints this value. If it is impossible for all heads to reach the tracks within a certain time, the function will adjust the average time until a valid solution is found. The function does not return a list of results but rather prints a single integer representing the minimum average time that works for all heads.

