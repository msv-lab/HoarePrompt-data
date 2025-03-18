#State of the program right berfore the function call: n is an integer representing the number of houses, and a is a string of length n consisting only of '0' and '1', where '0' indicates a resident prefers to live on the left side and '1' indicates a resident prefers to live on the right side.
def func_1():
    n = int(input())
    a = input()
    S = [[0, 0]]
    for s in a:
        x, y = S[-1]
        
        if s == '0':
            x += 1
        else:
            y += 1
        
        S.append([x, y])
        
    #State: Output State: The value of `n` is at least 1, `s` is the last character of the string `a`, `x` is the sum of the first elements of all sublists in `S` plus the number of '0's in `a`, `y` is the sum of the second elements of all sublists in `S` plus the number of '1's in `a`, and `S` is a list containing all the sublists generated during the iterations of the loop.
    #
    #In simpler terms, after the loop has executed all its iterations, `n` remains at least 1, `s` will be the last character of the string `a`. The variable `x` will be the count of '0's in the string `a`, and `y` will be the count of '1's in the string `a`. The list `S` will contain all the intermediate states `[x, y]` for each character in the string `a`, starting from `[0, 0]` and updating with each iteration based on whether the current character is '0' or '1'.
    ans = -1
    for i in range(n + 1):
        left = S[i][0]
        
        lsum = i
        
        right = S[-1][1] - S[i][1]
        
        rsum = n - i
        
        if left * 2 < lsum or right * 2 < rsum:
            continue
        elif abs(n / 2 - i) < abs(n / 2 - ans):
            ans = i
        
    #State: The final value of `ans` is the index `i` that minimizes the absolute difference between `n / 2` and `ans`, while satisfying the conditions `(left * 2 >= lsum)` and `(right * 2 >= rsum)` for all iterations of the loop.
    print(ans)
    #This is printed: ans (the index i that minimizes |n/2 - ans| and satisfies (left * 2 >= lsum) and (right * 2 >= rsum) for all iterations)
#Overall this is what the function does:The function accepts an integer `n` representing the number of houses and a string `a` of length `n` consisting only of '0' and '1'. It calculates and prints the optimal index `i` that minimizes the absolute difference between `n / 2` and `i`, while ensuring that the number of residents preferring to live on the left side up to index `i` is at least half of those positions, and the number of residents preferring to live on the right side from index `i` to the end is also at least half of those positions.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: `n` is an integer such that \(3 \leq n \leq 3 \cdot 10^5\)
#Overall this is what the function does:The function does not accept any parameters and does not return anything. It reads an integer `n` from user input, which must be between 3 and 300,000 inclusive, and then calls another function `func_1()` multiple times (specifically, the number of times equal to the value of `n`). After executing these calls, the function ends without returning any value.

