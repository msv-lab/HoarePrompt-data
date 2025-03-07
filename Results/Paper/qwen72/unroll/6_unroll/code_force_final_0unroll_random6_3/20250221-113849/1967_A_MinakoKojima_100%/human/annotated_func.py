#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^12, representing the number of cards of each type. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: `ans_list` is a list containing the final answers for each test case, where each answer is an integer representing the maximum number of cards that can be made equal by spending the given number of coins, and the sum of `n` over all test cases does not exceed 5 · 10^5.
    for a in ans_list:
        print(a)
        
    #State: The `ans_list` remains unchanged, and the values in `ans_list` have been printed to the console, one per line.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the number of distinct types of cards (`n`), the number of coins (`k`), and a list of integers (`a`) representing the number of cards of each type. For each test case, it calculates the maximum number of cards that can be made equal by spending the given number of coins and stores these results in a list `ans_list`. After processing all test cases, it prints each result in `ans_list` to the console, one per line. The final state of the program is that `ans_list` remains unchanged, and the values in `ans_list` have been printed to the console.

