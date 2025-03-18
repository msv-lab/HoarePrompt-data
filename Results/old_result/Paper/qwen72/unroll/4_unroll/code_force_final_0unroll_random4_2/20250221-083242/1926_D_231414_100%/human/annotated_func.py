#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a_1, ..., a_n are integers such that 0 ≤ a_j < 2^31. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    times = int(input())
    check = 2 ** 31 - 1
    for _ in range(times):
        n = int(input())
        
        data = list(map(int, input().split()))
        
        dic = dict()
        
        ans = 0
        
        check = 2 ** 31 - 1
        
        for i in data:
            s = i ^ check
            if i in dic:
                dic[i] -= 1
                if dic[i] == 0:
                    del dic[i]
            else:
                if s not in dic:
                    dic[s] = 0
                dic[s] += 1
                ans += 1
        
        print(ans)
        
    #State: The loop executes `times` iterations, and for each iteration, it reads an integer `n` and a list of integers `data`. After processing `data` with the given algorithm, it prints the value of `ans` which represents the count of unique XOR results with `check` (2147483647) that are not already in the dictionary `dic`. The variables `t`, `n`, `a_1, ..., a_n`, and `check` remain unchanged as they are either input or constants.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It processes the list to count the number of unique XOR results with `2^31 - 1` (2147483647) that are not already in a dictionary. After processing, it prints the count for each test case. The function does not return any value. The variables `t`, `n`, and the list of integers are consumed during the function execution, and `check` is reset to `2^31 - 1` for each test case.

