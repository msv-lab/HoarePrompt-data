#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000) representing the number of towers, k is an integer (n ≤ k ≤ 1,000,000,000) representing the maximum allowed cost for slices, and h is a list of n integers (1 ≤ h_i ≤ 200,000) representing the heights of the towers.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ `n` ≤ 200,000), `k` is an integer (`n` ≤ `k` ≤ 1,000,000,000), `h` is a Counter object with at least one key value ≤ 200,000; `tot` is the total occurrences counted from `h`, `cnt` is the total occurrences that do not exceed `k`, and `slices` is the number of times the accumulated count has exceeded `k`.
    print(slices)
#Overall this is what the function does:The function accepts two integers, `n` (the number of towers) and `k` (the maximum allowed cost for slices), and a list `h` representing the heights of the towers. It calculates the number of slices required based on the heights of the towers such that the accumulated count of heights does not exceed `k`. The function prints the number of slices needed when the total count exceeds `k`. It does not return any value; it only prints the result.

