#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a list of n integers a_1, a_2, ..., a_n where each a_j is a non-negative integer such that 0 ≤ a_j < 2^31. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; times is an input integer; check is 2147483647.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` non-negative integers. For each test case, it processes the list and prints the number of unique elements remaining after each element is processed, considering the operation `i ^ 2147483647` (where `^` is the bitwise XOR operation) to determine uniqueness.

