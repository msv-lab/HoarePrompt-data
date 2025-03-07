#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of n (1 ≤ n ≤ 2⋅10^5) integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of n (1 ≤ n ≤ 2⋅10^5) integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. The sum of all n across all test cases does not exceed 2⋅10^5. After executing the loop, for each test case, the output is the first index i where either the count of i in the list a is zero or the count of i is one and it's the second occurrence of such an index, or it prints the index and breaks the loop early if these conditions are met.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t and a list of n integers a. For each test case, it counts the occurrences of each integer in the list a. It then determines and outputs the first index i that meets one of two conditions: either the count of i is zero, or the count of i is one and it is the second occurrence of such an index. If no such index is found, it does not output anything for that test case.

