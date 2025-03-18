#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of n (1 ≤ n ≤ 2⋅10^5) integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all iterations, `t` will be equal to the total number of elements in `a`, `i` will be equal to `N + (N - 1)`, `N` will be the last value of `N` read from the input, `a` will be the list of integers obtained from the last input, `cnt` will be a defaultdict where each key from `0` to the maximum value in `a` will have a count corresponding to how many times that value appears in `a`. The loop will have processed all test cases, and once it processes the last test case, it will break out of the loop when `t >= 2` or `cnt[i] == 0` is met for the last time.
    #
    #In simpler terms, after all iterations of the loop, `t` will be the total count of unique non-zero elements in `a` across all test cases, `i` will be the index of the last element processed plus the length of the last array, and the loop will have printed the first index `i` where either `t` reaches 2 or `cnt[i]` becomes 0 for the last time before breaking.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of integers. For each test case, it counts the occurrences of each integer in the list and determines if there is an integer that appears exactly once. If such an integer is found, it prints the index of the first occurrence and breaks out of the loop. After processing all test cases, the function does not return any value.

