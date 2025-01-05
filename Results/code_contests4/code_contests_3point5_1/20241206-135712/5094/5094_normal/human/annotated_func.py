#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2*10^5 and n ≤ k ≤ 10^9. The list of initial heights h_i contains n integers where each integer is between 1 and 2*10^5.**
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
        
    #State of the program after the  for loop has been executed: `h` is a Counter object containing the counts of integers from the input, `tot` has been updated based on the iteration of the loop, `cnt` is assigned the value of `tot` if `cnt + tot` is greater than `k`, otherwise `cnt` is incremented by the value of `tot`, `slices` is the number of times `cnt + tot` exceeds `k`, `min(h)` is greater than 200001, and `i` is updated based on the loop iteration.
    print(slices)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, creates a Counter object `h` from a list of integers, and then iterates through a range of numbers. It updates `tot`, `cnt`, and `slices` based on certain conditions within the loop. After the loop, it prints the value of `slices`. However, the loop logic seems incorrect as it may not behave as per the annotations provided. It lacks clarity in terms of achieving the desired functionality based on the annotations.

