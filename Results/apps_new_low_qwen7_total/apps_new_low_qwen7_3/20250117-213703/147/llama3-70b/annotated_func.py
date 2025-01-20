#State of the program right berfore the function call: n and k are integers such that 2 ≤ k < n ≤ 100, and a list of integers of length n where each integer is either 1 or -1.
def func():
    n, k = map(int, input().split())

tabs = list(map(int, input().split()))

max_diff = 0
    for b in range(1, n + 1):
        e, s = 0, 0
        
        for i in range(1, n + 1):
            if (i - b) % k != 0:
                e += tabs[i - 1] == 1
                s += tabs[i - 1] == -1
        
        max_diff = max(max_diff, abs(e - s))
        
    #State of the program after the  for loop has been executed: n is 6, k is 3, tabs is [1, -1, 1, 1, -1, 1], max_diff is 2, b is > 6.
    print(max_diff)
#Overall this is what the function does:The function accepts a list of integers `tabs` of length `n` where each integer is either 1 or -1, and two integers `n` and `k` such that 2 ≤ k < n ≤ 100. It calculates the maximum difference between the count of 1s and -1s in any subarray of `tabs` with a sliding window size of `b` that is a multiple of `k`. The function then prints this maximum difference.

