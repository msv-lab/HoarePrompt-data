#State of the program right berfore the function call: Each test case contains two integers n (1 ≤ n ≤ 2 · 10^5) and k (0 ≤ k ≤ 10^12) representing the number of distinct types of cards and the number of coins, respectively. Additionally, the test case contains a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^12) representing the number of cards of type i initially available. The total number of test cases t (1 ≤ t ≤ 100) is given at the beginning, and the sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: [result1, result2, ..., resultt]
    for a in ans_list:
        print(a)
        
    #State: [result1, result2, ..., resultt]
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of card types `n`, a number of coins `k`, and a list of integers representing the initial count of each card type. For each test case, it calculates and prints a result based on the distribution of coins among the card types, aiming to maximize the minimum number of cards of any type by using the coins.

