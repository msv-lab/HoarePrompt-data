#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2*10^5 and n ≤ k ≤ 10^9. h_i are integers representing the initial heights of towers such that 1 ≤ h_i ≤ 2*10^5.**
def func_1():
    n, k = map(int, input().split(' '))
    h = Counter(map(int, input().split(' ')))
    tot, cnt = 0, 0
    slices = 0
    for i in range(200000, min(h) - 1, -1):
        if i in h:
            tot += h[i]
        
        if cnt + tot > k:
            cnt = tot
            slices += 1
        else:
            cnt += tot
        
    #State of the program after the  for loop has been executed: `n`, `k`, `cnt`, `tot`, `slices`, `i` will have their final values based on the conditions in the loop. If the loop executes, the variables will be adjusted accordingly after all iterations. If the loop does not execute, `cnt`, `tot`, `slices`, `i` will remain 0.
    print(slices)
#Overall this is what the function does:The function func_1 reads input data about tower heights and target height, then calculates the minimum number of bricks required to make all towers reach the target height. It iterates over the tower heights, adjusting the total brick count and number of slices based on certain conditions. The final number of slices required is printed as the output. However, the code does not handle cases where there are no tower heights provided or if the loop does not execute due to certain conditions, potentially leading to incorrect output in those scenarios.

