#State of the program right berfore the function call: The function should take three parameters: t (an integer representing the number of test cases, 1 ≤ t ≤ 10^4), a list of tuples where each tuple contains two integers n and k (2 ≤ n ≤ 10^5, 1 ≤ k ≤ n) representing the number of cows and your cow's index, and a list of lists where each inner list contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the Cowdeforces ratings of the cows. The sum of n over all test cases does not exceed 10^5, and all a_i's are pairwise different.
def func():
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        
        s = list(map(int, input().split()))
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans = 0
        
        h = s[0]
        
        j = -1
        
        for i in s[1:]:
            j += 1
            if h < i:
                break
            else:
                ans += 1
        
        p = j + 1
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans1 = 0
        
        s[p], s[k - 1] = s[k - 1], s[p]
        
        z = 0
        
        for i in s:
            if i == h:
                if s[0] != h:
                    ans1 += 1
                z = 1
            elif i > h:
                break
            elif z == 1:
                ans1 += 1
        
        print(max(ans, ans1))
        
    #State: The loop iterates through each test case, and for each test case, it prints the maximum number of cows that can be in front of your cow (index k-1) without having a higher Cowdeforces rating than your cow. The variables `t`, `n`, `k`, and `s` are processed and their values are used to compute the result, but they are not retained between test cases. The final output state is the sequence of printed results for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it takes the number of cows `n` and the index of your cow `k-1`, along with a list of Cowdeforces ratings `s` for the cows. It calculates and prints the maximum number of cows that can be in front of your cow without any of them having a higher rating than your cow. The function does not return any value; it only prints the results for each test case. After processing all test cases, the function concludes, and the final state is the sequence of printed results, one for each test case.

