#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 ⋅ 10^5), k is an integer (n ≤ k ≤ 10^9), and h is a list of n integers where each integer h_i represents the height of a tower (1 ≤ h_i ≤ 2 ⋅ 10^5).
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 2 ⋅ 10^5), `k` is an integer (n ≤ k ≤ 10^9), `h` is a Counter of heights, `tot` is the total count of all heights from 200,000 down to the minimum height in `h`, `cnt` is the total count accumulated up to the last point it exceeded `k`, `slices` is the total number of times `cnt` exceeded `k`.
    print(slices)
#Overall this is what the function does:The function accepts two integers `n` and `k`, and a list of integers `h` representing the heights of towers. It counts how many times the cumulative height of towers, when processed from the tallest down to the shortest, exceeds the threshold `k`. The final output is the total number of slices, which indicates how many times the cumulative height surpassed `k`. The function does not return information about towers below the height limit, nor does it indicate the total number of towers; it only outputs the count of slices.

