#State of the program right berfore the function call: The function `func` is expected to take input parameters, but the function definition provided does not include them. For the problem to be solved, the function should accept parameters `t` (number of test cases), `n` and `k` (integers for each test case representing the number of distinct types of cards and the number of coins), and a list `a` of length `n` containing integers representing the number of cards of each type. The constraints are 1 ≤ t ≤ 100, 1 ≤ n ≤ 2 · 10^5, 0 ≤ k ≤ 10^12, and 1 ≤ a_i ≤ 10^12. The sum of n over all test cases does not exceed 5 · 10^5.
def func():
    ans_list = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = a[0]
        
        res = n - 1
        
        for i in range(n - 1):
            dif = a[i + 1] - a[i]
            if dif == 0:
                res -= 1
            if dif != 0:
                if k >= dif * (i + 1):
                    ans += dif
                    k -= dif * (i + 1)
                    res -= 1
                else:
                    ans += k // (i + 1)
                    if i != 0:
                        res += k % (i + 1)
                    k = 0
                    break
                if k == 0:
                    break
        
        if k != 0:
            ans += k // n
            res += k % n
        
        ans += (ans - 1) * (n - 1)
        
        ans += res
        
        ans_list.append(ans)
        
    #State: `ans_list` contains the final `ans` value for each test case, and all other initial conditions remain unchanged.
    for a in ans_list:
        print(a)
        
    #State: `ans_list` contains the final `ans` value for each test case, and all elements in `ans_list` have been printed.
#Overall this is what the function does:The function `func` reads input from the user, processes multiple test cases, and prints the result for each test case. Each test case involves the number of distinct types of cards `n`, the number of coins `k`, and a list `a` of integers representing the number of cards of each type. The function calculates and prints the maximum number of cards that can be bought with `k` coins for each test case. After processing all test cases, the function does not return any value, but it prints the results to the console. The state of the program after the function concludes is that all test cases have been processed, and the results have been printed.

