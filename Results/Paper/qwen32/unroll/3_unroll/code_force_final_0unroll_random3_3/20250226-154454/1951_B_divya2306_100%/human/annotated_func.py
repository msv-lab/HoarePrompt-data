#State of the program right berfore the function call: There are multiple test cases. Each test case consists of two integers n (2 ≤ n ≤ 10^5) and k (1 ≤ k ≤ n) representing the number of cows and the index of the cow owned by the player. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the Cowdeforces ratings of the cows, where all a_i values are distinct. The sum of n over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: - `n` and `k` remain unchanged as they are not modified within the loop.
    #   - `a` remains unchanged as the loop does not modify the list.
    #   - `wins` is the number of cows whose ratings are less than or equal to the player's cow's rating, up to the point where a cow with a higher rating is encountered or all cows are compared.
    #
    #Given this analysis, the output state is:
    #
    #Output State:
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of cows whose ratings are less than or equal to the player's cow's rating)
        return
        #The program returns nothing (None)
    #State: `n` and `k` remain unchanged as they are not modified within the loop. `a` remains unchanged as the loop does not modify the list. `wins` is the number of cows whose ratings are less than or equal to the player's cow's rating, up to the point where a cow with a higher rating is encountered or all cows are compared. Additionally, `wins` is less than `k`.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `n` and `k` remain unchanged as they are not modified within the loop. `a` remains unchanged as the loop does not modify the list. `wins` remains the number of cows whose ratings are less than or equal to the player's cow's rating, up to the point where a cow with a higher rating is encountered or all cows are compared. `win_with_swap` is the count of cows (including the player's cow) whose ratings are less than or equal to the player's cow's rating, up to the point where a cow with a higher rating is encountered or all cows are compared.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: max(wins - 1, win_with_swap - wins - 1 + (wins != 0)) (where `wins` is the count of cows with ratings less than or equal to the player's cow's rating, and `win_with_swap` is the count of cows including the player's cow with ratings less than or equal to the player's cow's rating)
#Overall this is what the function does:The function reads multiple test cases, each consisting of the number of cows `n`, the index `k` of the player's cow, and a list of distinct Cowdeforces ratings for the cows. It calculates and prints the maximum number of cows that can be beaten or tied by the player's cow, considering the player's cow's position and ratings. The function does not return any value.

