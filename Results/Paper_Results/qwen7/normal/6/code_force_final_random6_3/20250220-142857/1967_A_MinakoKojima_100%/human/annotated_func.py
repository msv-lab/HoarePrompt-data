#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of type i initially.
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
        
    #State: `ans_list` contains the sum of `ans` values calculated for each iteration, with each `ans` value being computed based on the logic within the loop. The final `ans` value after all iterations is the last element in `ans_list`.
    for a in ans_list:
        print(a)
        
    #State: Output State: `ans_list` must have as many elements as there are iterations of the loop, with each element being the value of `a` from each respective iteration of the loop.
    #
    #In natural language, this means that after the loop has executed all its iterations, `ans_list` will contain a list where each element corresponds to the value of `a` printed during each iteration of the loop. The length of `ans_list` will be equal to the total number of iterations the loop ran.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it calculates a value `ans` based on the number of cards (`n`), the number of operations allowed (`k`), and the initial distribution of card types (`a`). It then appends each calculated `ans` value to a list `ans_list`. After processing all test cases, it prints each value in `ans_list`. The final state of the program is that `ans_list` contains the calculated `ans` values for each test case, and these values are printed out.

