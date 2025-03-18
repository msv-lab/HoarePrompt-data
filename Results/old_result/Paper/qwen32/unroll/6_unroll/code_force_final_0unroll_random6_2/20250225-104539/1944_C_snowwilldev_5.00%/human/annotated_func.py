#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array a, and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the elements of the array. The function will be called multiple times with t (1 ≤ t ≤ 2 · 10^4) test cases, and the sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for tc in range(int(input())):
        N = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = defaultdict(int)
        
        for i in range(N):
            cnt[a[i]] += 1
        
        t = 0
        
        for i in range(N):
            if cnt[i] == 1:
                t += 1
            if t >= 2 or cnt[i] == 0:
                print(i)
                break
        
    #State: the first index `i` in the range from `0` to `N-1` for each test case where either `cnt[i] == 0` or `t >= 2` is true.
#Overall this is what the function does:For each test case, the function processes an array of integers and prints the first index `i` in the range from `0` to `N-1` where either the count of `i` in the array is `0` or there are at least two unique elements in the array that appear exactly once.

