#State of the program right berfore the function call: The function should take two parameters: a list of integers `ratings` representing the Cowdeforces ratings of the cows, and an integer `k` representing the index of your cow. The list `ratings` contains `n` distinct integers where `2 <= n <= 10^5`, and `1 <= k <= n`. The integer `k` is the index (1-based) of your cow in the list `ratings`. The function should be able to handle multiple test cases, where the number of test cases `t` is an integer such that `1 <= t <= 10^4`.
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
        
    #State: The loop will execute for `t` test cases, and for each test case, it will print the maximum number of cows that can be placed before your cow (at index `k`) in the list `ratings` such that all these cows have a rating less than or equal to your cow's rating. The list `ratings` and the index `k` will not be modified after the loop execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of distinct integer ratings for cows and an index `k` (1-based) representing the position of your cow in the list. For each test case, the function calculates and prints the maximum number of cows that can be placed before your cow such that all these cows have a rating less than or equal to your cow's rating. The function does not modify the input list `ratings` or the index `k` after processing each test case.

