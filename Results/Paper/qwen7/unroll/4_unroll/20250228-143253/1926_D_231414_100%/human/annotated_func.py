#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the list of integers a_1, \ldots, a_n consists of non-negative integers less than 2^{31}. The sum of n over all test cases in a test does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: `times` is the number of test cases; for each test case, `check` is 2147483647, and `ans` is the count of elements in the data list that do not have their bitwise XOR with `check` present in the dictionary `dic`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer `t` representing the number of subsequent test cases, then for each of these test cases, it reads another positive integer `n` and a list of `n` non-negative integers. It calculates the count of elements in the list that do not have their bitwise XOR with `2^31 - 1` present in a dictionary. Finally, it prints the count for each test case.

