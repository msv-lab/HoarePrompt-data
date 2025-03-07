#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5), followed by a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. It is also guaranteed that the sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: After the loop executes all iterations, `cur` will be set to the second smallest unique number that appeared in any of the lists `N` across all iterations if such a number exists. If there is no such unique number (i.e., all numbers either appear more than once or there are fewer than two unique numbers), `cur` will remain unchanged from its final value after the third iteration.
    #
    #This means that `cur` will reflect the second smallest distinct number seen in the lists `N` provided as inputs to each iteration of the loop, ensuring it has been incremented appropriately based on the conditions within the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) followed by a list of \( n \) integers. For each test case, it sorts the list of integers and then iterates through them to find the second smallest unique number. If such a number exists, it sets the variable `cur` to this number; otherwise, `cur` remains unchanged. Finally, it prints the value of `cur`.

