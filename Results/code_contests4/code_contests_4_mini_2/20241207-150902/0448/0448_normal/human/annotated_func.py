#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 100000; hi is a list of n distinct integers in ascending order with values such that 1 ≤ hi ≤ 10^10; and pi is a list of m distinct integers in ascending order with values such that 1 ≤ pi ≤ 10^10.
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
        
    #State of the program after the loop has been executed: `hidx` is equal to the length of `h`, `pidx` is equal to the length of `p`, `ss` is equal to `ll`, `ll` is the minimum value such that all conditions in the inner loop are satisfied, `works` is True, indicating that all elements of `p` have been accounted for within the calculated ranges.
    print(ss)
#Overall this is what the function does:The function accepts two lists `h` and `p` containing `n` and `m` distinct integers, respectively, both sorted in ascending order. It calculates the minimum average time required such that each position in `p` can be reached from the corresponding position in `h` based on specific movement rules. The function prints this minimum average time as an integer after processing the lists. It also handles cases where no valid average can be found, ensuring that all elements of `p` are accounted for within the calculated ranges.

