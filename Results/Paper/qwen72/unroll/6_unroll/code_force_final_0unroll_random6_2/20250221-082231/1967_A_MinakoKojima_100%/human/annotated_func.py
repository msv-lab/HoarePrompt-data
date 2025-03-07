#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins available for buying new cards, respectively. a is a list of n integers such that 1 ≤ a_i ≤ 10^12, representing the number of cards of each type initially available. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: After all iterations of the loop, `ans_list` will contain the results of the computations for each test case, and the variables `t`, `n`, `k`, and `a` will no longer be in their initial states but will have been updated or redefined within the loop. The final state of `ans_list` will be a list of integers, each representing the final answer for the corresponding test case. The variables `t`, `n`, `k`, and `a` will have no meaningful values outside the context of the loop, as they are redefined for each test case.
    for a in ans_list:
        print(a)
        
    #State: The loop will print each element of `ans_list` on a new line. The final state of `ans_list` remains unchanged as a list of integers, each representing the final answer for the corresponding test case. The variables `t`, `n`, `k`, and `a` will have no meaningful values outside the context of the loop, as they are redefined for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of distinct types of cards (`n`), the number of coins available for buying new cards (`k`), and a list of integers (`a`) representing the initial number of cards of each type. For each test case, it calculates the maximum number of cards that can be made equal by spending the available coins and prints the result for each test case. The final state of the program is that `ans_list` contains the results for all test cases, and the variables `t`, `n`, `k`, and `a` are no longer meaningful outside the context of the loop.

