#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the integers a_1, a_2, ..., a_n are non-negative and less than 2^{31}. The sum of all n across all test cases does not exceed 2 \cdot 10^5.
def func():
    times = int(input())
    check = 2 ** 31 - 1
    for _ in range(times):
        n = int(input())
        
        data = list(map(int, input().split()))
        
        dic = dict()
        
        ans = n
        
        check = 2 ** 31 - 1
        
        for i in data:
            s = i ^ check
            if s in dic:
                dic[s] -= 1
                ans -= 1
                if dic[s] == 0:
                    del dic[s]
            elif i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            print(ans)
        
    #State: Output State: `check` is 2147483647; `times` is 0.
    #
    #Explanation: The loop runs `times` number of times. After each iteration of the loop, `times` is decremented by 1. Since `times` starts as a positive integer (1 ≤ `times` ≤ 10^4) and is decremented by 1 in each iteration, after all iterations, `times` will be 0. The value of `check` remains unchanged at 2147483647 because it is not modified within the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t` (1 ≤ t ≤ 10^4) and a list of `n` non-negative integers `a_1, a_2, ..., a_n` (1 ≤ n ≤ 2 * 10^5, and each `a_i` < 2^31). For each test case, it calculates and prints the maximum possible count of unique integers that can be obtained by performing bitwise XOR operations between any two integers in the list. After processing all test cases, the function sets `times` to 0 and leaves `check` unchanged at 2147483647.

