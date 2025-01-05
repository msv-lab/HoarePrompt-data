#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 10^5. hi and pi are distinct integers in ascending order such that 1 <= hi, pi <= 10^10 and hi < hi + 1, pi < pi + 1.**
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
        
    #State of the program after the loop has been executed: `n` and `m` are positive integers, `hi` and `pi` are distinct integers in ascending order, `h` is a list of integers, `p` is a list of integers created from user input, `ss` is 0, `ll` is equal to the final calculated `avg`, `avg` is the final calculated value after the loop execution, `works` is either True or False, `hidx` is equal to the length of `h`, `pidx` is not equal to the length of `p`
    print(ss)
#Overall this is what the function does:The function `func_1` reads input data for integers `n`, `m`, lists `h` and `p`, and performs a complex computational process involving binary search and nested loops to determine certain conditions based on the input values. The function outputs the value of `ss` after the loop execution. However, the specific purpose or outcome of this computational process is not explicitly defined in the code or annotations.

