#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 2 · 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n). The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: the value of `cur` after processing the last test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it computes and prints a specific integer value `cur` based on the provided integers. The value `cur` is determined by sorting the list of integers and analyzing their frequencies and values, ultimately reflecting a condition related to the distribution of unique and repeated numbers in the list.

