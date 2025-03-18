#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a_1, ..., a_n are integers such that 0 ≤ a_j < 2^31. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, `a_1, ..., a_n` are integers such that 0 ≤ a_j < 2^31. The sum of n over all test cases does not exceed 2 · 10^5. `times` is an input integer. `check` is 2147483647. `ans` is the number of unique integers in the final state of `data` after all iterations.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `data`. It then processes `data` to count and print the number of unique integers after each iteration, where an integer is considered unique if it does not have a pair that results in a specific XOR value with `2^31 - 1`. The function does not return any value but prints the count of unique integers for each test case. After the function concludes, `t` remains an integer within the range 1 to 10^4, `n` is an integer within the range 1 to 2 · 10^5, and `data` contains integers within the range 0 to 2^31 - 1. The sum of `n` over all test cases does not exceed 2 · 10^5.

