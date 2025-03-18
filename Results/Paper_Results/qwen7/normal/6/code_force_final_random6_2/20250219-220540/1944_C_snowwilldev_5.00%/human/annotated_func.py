#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5), an integer representing the size of the array a, followed by n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. It is also guaranteed that the sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: The loop has executed all its iterations, meaning all test cases have been processed. For each test case, the variable `t` represents the count of unique elements in the array `a` that appear exactly once. The variable `i` will be the first index where either `cnt[i]` is 0 or `t` becomes greater than or equal to 2, or it will be equal to `N` if no such index is found. The variable `tc` will be the total number of test cases plus one. The variable `N` will be the size of the array `a` for the last test case. The variable `a` will be the list of integers for the last test case. The variable `cnt` will be a defaultdict containing the count of each integer present in the array `a` for the last test case. If no element meets the condition to break the inner loop, `i` will be equal to `N`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an array `a` of length `n`. For each test case, it counts the number of unique elements that appear exactly once in the array. If there are at least two such elements or if an element does not appear at all, it prints the index of the first such element and breaks the loop. If no such element is found, it prints the length of the array. The function does not return any value but prints the result for each test case.

