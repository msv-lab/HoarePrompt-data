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
        
    #State: `n` is an integer input by the user, `a` is a string input by the user consisting only of '0' and '1' and must have `n` characters, `S` is a list containing `n + 1` sublists. The first sublist is `[0, 0]`, and each subsequent sublist `[x, y]` in `S` represents the cumulative count of '0's and '1's encountered in the string `a` up to that point.
    ans = 0
    satisfy = 0
    for i in range(n):
        left = S[i][0]
        
        lsum = S[i][0] + S[i][1]
        
        right = S[-1][1] - S[i][1]
        
        rsum = n - lsum
        
        if left * 2 < lsum or right * 2 < rsum:
            continue
        elif abs(n / 2 - i) <= abs(n / 2 - ans):
            ans = i
        
    #State: `n` remains the same, `i` is `n - 1`, `left` is `S[n-1][0]`, `lsum` is `S[n-1][0] + S[n-1][1]`, `right` is `S[-1][1] - S[n-1][1]`, `rsum` is `n - lsum`. If `left * 2 < lsum` or `right * 2 < rsum` for any iteration, the loop continues to the next iteration. Otherwise, if `abs(n / 2 - i) <= abs(n / 2 - ans)`, `ans` is set to the current `i`. If no such `i` satisfies the condition, `ans` remains 0.
    print(ans)
    #This is printed: - The value of `ans` is printed.
    #   - `ans` will be the value of `i` that satisfies the conditions `left * 2 >= lsum` and `right * 2 >= rsum`, and is closest to `n / 2` in terms of absolute difference.
    #   - If no such `i` is found, `ans` remains 0.
    #
    #Given the initial state and the loop conditions, the final value of `ans` depends on the specific values of `n` and the list `S`. However, without the exact values of `n` and `S`, we can only describe the output based on the conditions provided.
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `a` of length `n` consisting only of '0' and '1'. It calculates the cumulative counts of '0's and '1's at each position in the string `a` and stores these counts in a list `S`. The function then finds the index `i` (0-based) such that the cumulative count of '0's and '1's up to `i` and from `i+1` to the end of the string satisfy certain balance conditions, and this index is closest to `n / 2`. If no such index is found, the function prints 0. Otherwise, it prints the index `i` that satisfies the conditions.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: `int(input())` must return a value greater than or equal to the number of iterations, `func_1()` has been called the specified number of times.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer from the user input, and based on this integer, it calls the function `func_1` the specified number of times. The function does not return any value. After the function concludes, `func_1` has been called the number of times equal to the integer provided by the user.

