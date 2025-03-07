#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of '0' and '1'.
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
        
    #State: `n` is an input integer, `a` is a non-empty input string with `n` characters, `S` is a list containing `n + 1` sublists. The first sublist is `[0, 0]`. Each subsequent sublist `[x, y]` in `S` represents the cumulative count of '0's and '1's (or any other character not '0') encountered in the string `a` up to that point.
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
        
    #State: `n` is a non-negative integer, `i` is `n + 1`, `a` is a non-empty input string with `n` characters, `S` is a list containing `n + 1` sublists, `ans` is the value of `i` that minimizes the absolute difference between `n / 2` and `i` while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum` for each iteration.
    print(ans)
    #This is printed: n + 1 (where n is the length of the input string `a` and `i` is `n + 1`, and `ans` is the value of `i` that minimizes the absolute difference between `n / 2` and `i` while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum`)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a string `a` of length `n` consisting only of '0' and '1' from the user. It then calculates and prints an integer `ans` which represents the index `i` (0 ≤ i ≤ n) that minimizes the absolute difference between `n / 2` and `i`, while ensuring that the number of '0's on the left side of `i` is at least half the length of the left side, and the number of '1's on the right side of `i` is at least half the length of the right side. The function does not return any value.

#State of the program right berfore the function call: None of the variables in the function signature.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: `int(input())` must be greater than or equal to the number of iterations, and `func_1()` has been called the number of times specified by `int(input())`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It reads an integer from the user input, and calls the function `func_1` that many times. After the function concludes, `func_1` has been called the number of times specified by the user input integer.

