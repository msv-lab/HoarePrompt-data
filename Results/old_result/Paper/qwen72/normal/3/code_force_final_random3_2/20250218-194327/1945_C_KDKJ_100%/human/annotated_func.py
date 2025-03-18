#State of the program right berfore the function call: None, as the function `func_1` does not take any parameters and instead reads input directly from the standard input.
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
        
    #State: `n` is an integer value input by the user, `a` is a string input by the user that must have at least `n` characters, `S` is a list containing `n + 1` sublists. The first sublist is `[0, 0]`, and each subsequent sublist `[x, y]` in `S` represents the cumulative count of '0's and non-'0's (respectively) in the string `a` up to the corresponding character.
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
        
    #State: `n` must be at least 0, `i` is `n + 1`, `a` is a string input by the user that must have at least `n` characters, `S` is a list containing `n + 1` sublists, `ans` is the index `i` where the absolute difference between `n / 2` and `i` is minimized, given that `left * 2 >= lsum` and `right * 2 >= rsum` for each `i` in the range.
    print(ans)
    #This is printed: ans (where ans is the index closest to n / 2 that satisfies the conditions left * 2 >= lsum and right * 2 >= rsum)
#Overall this is what the function does:The function `func_1` reads two inputs from the standard input: an integer `n` and a string `a`. It then processes the string `a` to find an index `i` (0 ≤ i ≤ n) such that the number of '0's in the first `i` characters of `a` is at least half of `i`, and the number of non-'0's in the remaining characters of `a` is at least half of `n - i`. The function prints the index `i` that minimizes the absolute difference between `n / 2` and `i`, while satisfying the above conditions. If no such index exists, it prints -1.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: `int(input())` must be greater than or equal to the number of iterations, `_` is equal to the number of iterations minus 1, and `func_1()` has been called the number of times equal to the number of iterations.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer from the user input, and then calls the function `func_1` that many times. The function does not return any value. After the function concludes, `func_1` has been called the number of times specified by the user input.

