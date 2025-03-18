#State of the program right berfore the function call: t is an integer such that 1 <= t <= 2 * 10^4, each test case consists of an integer n such that 1 <= n <= 2 * 10^5, and a list of n integers a where 0 <= a_i < n. The sum of n across all test cases does not exceed 2 * 10^5.
def func():
    T = int(input())
    for _ in range(T):
        S = int(input())
        
        N = list(map(int, input().split()))
        
        N.sort()
        
        cur = -1
        
        M = {}
        
        for num in N:
            if num > cur:
                if num > cur + 1:
                    cur += 1
                    break
                cur = num
                M[cur] = 1
            else:
                M[cur] += 1
        
        if sum([M[k] for k in M.keys()]) == S:
            cur += 1
        
        cnt = []
        
        for k in M.keys():
            if M[k] == 1:
                cnt.append(k)
        
        if len(cnt) >= 2:
            cur = cnt[1]
        
        print(cur)
        
    #State: The final value of `cur` for each test case, printed sequentially.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers `a`. For each test case, it calculates and prints a specific integer value `cur` based on the input list. The value of `cur` is determined by sorting the list and analyzing the frequency of each integer, ultimately selecting a value that meets certain conditions related to the sum of unique elements and their frequencies.

