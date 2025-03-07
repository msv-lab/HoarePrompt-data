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
        
    #State: The variable `times` is decremented to 0. The variable `check` is reset to 2147483647 at the start of each iteration. The variable `ans` is printed after each iteration and is reset to 0 for the next iteration. The dictionary `dic` is cleared at the end of each iteration. The variables `n` and `data` are updated with new input values in each iteration. The sum of `n` over all test cases does not exceed 2 · 10^5.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 2 · 10^5) and a list of `n` integers `a` (0 ≤ a_j < 2^31). The function then computes the number of unique integers in the list `a` after applying a specific transformation (XOR with `2^31 - 1`) and prints the result for each test case. The function does not return any value; it only prints the results. After processing all test cases, the function concludes with no remaining state.

