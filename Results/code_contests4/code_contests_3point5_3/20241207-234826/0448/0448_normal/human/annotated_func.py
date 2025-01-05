#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 10^5. The lists hi and pi contain distinct integers in ascending order, where 1 ≤ hi, pi ≤ 10^10 and hi < hi + 1, pi < pi + 1 respectively.**
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
        
    #State of the program after the loop has been executed: `n` and `m` are positive integers, `h` is a non-empty list of integers, `p` is a non-empty list of integers obtained from the input, `ss` is updated to the final value of `avg + 1`, `ll` is equal to the final value of `avg`, `works` is True if the conditions are met, all other variables retain their final values after the loop execution
    print(ss)
#Overall this is what the function does:The function `func_1` reads input values and performs a complex calculation involving multiple conditions and loops to determine a specific value. It iteratively refines a range of values until a specific condition is met. However, the exact purpose or outcome of this calculation is not explicitly stated in the code or annotations. The function does not accept any parameters, and it prints a final value after the calculations.

