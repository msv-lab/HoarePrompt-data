#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_j satisfies 0 <= a_j < 2^31. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is the number of integers in the last test case; `a` is the list of integers in the last test case; `times` is the input integer representing the number of test cases; `check` is 2147483647; `dic` is a dictionary reflecting the counts of `s` values from the last test case; `ans` is the final count of unique `s` values encountered in the last test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of integers. For each test case, it calculates and prints the number of unique values obtained by XORing each integer in the list with the value 2^31 - 1, after accounting for the cancellation of pairs of identical integers.

