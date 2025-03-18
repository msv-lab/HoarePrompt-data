#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^12, representing the number of cards of type i. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `n` is the input integer greater than 0 for the last test case, `k` is the input integer greater than or equal to 0 for the last test case, `a` is a sorted list of integers where each element is greater than 0 for the last test case, `ans` is the final updated value after all iterations of the loop for the last test case, `res` is the final updated value after all iterations of the loop for the last test case, and `ans_list` is a list that contains the final updated value of `ans` for each of the `t` test cases.
    for a in ans_list:
        print(a)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `n` is the input integer greater than 0 for the last test case, `k` is the input integer greater than or equal to 0 for the last test case, `a` is a sorted list of integers where each element is greater than 0 for the last test case, `ans` is the final updated value after all iterations of the loop for the last test case, `res` is the final updated value after all iterations of the loop for the last test case, `ans_list` is a list that contains the final updated value of `ans` for each of the `t` test cases, and all elements in `ans_list` have been printed.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of distinct types of cards (`n`), the number of coins (`k`), and a list of the number of cards of each type (`a`). For each test case, it calculates a final value (`ans`) based on the inputs and prints this value. The function does not return any value; it only prints the results of all test cases. After the function concludes, the state includes the number of test cases (`t`), the inputs for the last test case (`n`, `k`, and `a`), and the results of all test cases having been printed.

