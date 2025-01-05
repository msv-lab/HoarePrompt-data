#State of the program right berfore the function call: n is an integer representing the number of towers (1 ≤ n ≤ 200,000), k is an integer representing the maximum cost of slices (n ≤ k ≤ 1,000,000,000), and h is a list of n integers representing the heights of the towers (1 ≤ h_i ≤ 200,000).
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
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of towers, `k` is an integer representing the maximum cost of slices, `h` is a Counter object holding the heights of the towers and their respective counts, `tot` is the total number of towers up to the minimum height in `h`, `cnt` is the last total that caused `cnt + tot` to exceed `k` or the accumulated count, and `slices` is the total number of slices created.
    print(slices)
#Overall this is what the function does:The function accepts an integer `n` representing the number of towers, an integer `k` representing the maximum cost of slices, and a list `h` (which is transformed into a Counter object) representing the heights of the towers. It calculates how many slices can be created without exceeding the cost `k`. The function iterates from the maximum height down to the minimum height in `h`, accumulating tower counts until the total exceeds `k`, at which point it increments the slice count and resets the accumulated count. Finally, it prints the total number of slices created.

