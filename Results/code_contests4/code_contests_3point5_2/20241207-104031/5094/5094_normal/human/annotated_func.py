#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2 * 10^5 and n ≤ k ≤ 10^9. h_i are integers representing the heights of towers such that 1 ≤ h_i ≤ 2 * 10^5.**
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
        
    #State of the program after the  for loop has been executed: `n`, `k`, `tot`, `slices`, `i`, `h`, `cnt` are integers. The final values of `n`, `k`, `tot`, `slices`, `i`, `h`, `cnt` are determined by the conditions within the loop and the values in `h`. The loop will run until `i` reaches a value less than or equal to the minimum value in `h`. The final values will depend on the sum of `h[i]`, comparisons between `cnt + tot` and `k`, and the specific values present in `h`.
    print(slices)
#Overall this is what the function does:The function `func_1` reads input for `n` and `k`, then calculates the number of slices needed based on the heights of towers in `h`. It iterates over a range and updates the total height and slice count accordingly. The function prints the total number of slices required.

