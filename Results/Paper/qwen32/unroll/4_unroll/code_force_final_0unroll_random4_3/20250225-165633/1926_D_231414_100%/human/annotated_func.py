#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_j satisfies 0 ≤ a_j < 2^31. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is the initial value of t, times is the initial value of times, n is the value of n from the last test case, a is the list of integers from the last test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers, where each integer is between 0 and 2^31 - 1. It then performs operations on the list and prints the result for each test case, which is the count of unique elements after a specific transformation involving bitwise XOR with 2^31 - 1.

