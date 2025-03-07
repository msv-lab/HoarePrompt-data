#State of the program right berfore the function call: None, as the function `func_1` does not take any parameters and reads input directly from the user.
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
        
    #State: `n` is an integer value input by the user, `a` is a string input by the user that must have at least `n` characters, `S` is a list containing `n + 1` sublists. The first sublist is `[0, 0]`, and each subsequent sublist `[x, y]` represents the cumulative count of '0's and non-'0's (respectively) in the string `a` up to that point.
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
        
    #State: `n` is an integer value input by the user that must be at least 0, `i` is `n + 1`, `a` is a string input by the user that must have at least `n` characters, `S` is a list containing `n + 1` sublists, and `ans` is the index `i` (0 ≤ `i` ≤ `n`) that minimizes the absolute difference between `n / 2` and `i` while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum`. If no such index exists, `ans` remains -1.
    print(ans)
    #This is printed: ans (where ans is the index i (0 ≤ i ≤ n) that minimizes the absolute difference between n / 2 and i while satisfying the conditions left * 2 >= lsum and right * 2 >= rsum, or -1 if no such index exists)
#Overall this is what the function does:The function `func_1` reads two inputs from the user: an integer `n` and a string `a`. It then processes the string `a` to find an index `i` (0 ≤ `i` ≤ `n`) that minimizes the absolute difference between `n / 2` and `i`, while ensuring that the cumulative count of '0's in the first `i` characters is at least half of `i`, and the cumulative count of non-'0's in the remaining characters is at least half of the remaining length. If no such index exists, the function prints -1. Otherwise, it prints the found index.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The loop has completed all iterations, `int(input())` must be greater than or equal to the number of iterations, `_` is the last index of the loop (which is `int(input()) - 1`), and `func_1()` has been called the number of times equal to `int(input())`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It reads an integer from the user input, and then calls the function `func_1` that many times. After the function concludes, the loop has completed all iterations, and `func_1` has been called the number of times equal to the integer input by the user.

