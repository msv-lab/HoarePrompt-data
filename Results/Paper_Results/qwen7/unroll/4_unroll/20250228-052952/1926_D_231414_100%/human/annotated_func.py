#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the integers a_1, a_2, ..., a_n are non-negative and less than 2^{31}; the sum of all n across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: `times` is an input integer, and `t` is a positive integer such that 1 ≤ t ≤ 10^4; `check` is 2147483647. After executing all iterations of the loop, the value of `ans` is the sum of the number of unique elements in each input list `data` after performing bitwise XOR with `check`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` non-negative integers. It then calculates the number of unique elements in the list after performing a bitwise XOR operation with `2^31 - 1` on each element. Finally, it prints the total count of such unique elements for all test cases.

