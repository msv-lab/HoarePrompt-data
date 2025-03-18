#State of the program right berfore the function call: n is an integer representing the number of houses, and a is a string of length n consisting only of '0' and '1', where '0' indicates a resident wants to live on the left side of the street, and '1' indicates a resident wants to live on the right side of the street.
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
        
    #State: `a` is an empty string, `s` is the first character of `a`, `x` is the last character of `a` plus 1, `y` is the last character of `a` plus 2, `S` is a list containing the elements `[x, y], [x, y]` appended.
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
        
    #State: Output State: `n` is greater than or equal to 0; `left` is `S[i][0]`; `lsum` is `i`; `right` is `S[-1][1] - S[i][1]`; `rsum` is `n - i`; `ans` is the value of `i` that minimizes the absolute difference between `n / 2` and `i` while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum`.
    #
    #Explanation: After all iterations of the loop, the variable `ans` will hold the value of `i` that satisfies the conditions within the loop and minimizes the absolute difference between `n / 2` and `i`. The values of `left`, `lsum`, `right`, and `rsum` will be as defined in each iteration of the loop, but they will not affect the final value of `ans`. The other variables (`a`, `s`, `x`, `y`, and `S`) will retain their initial or unchanged states from the beginning of the loop.
    print(ans)
    #This is printed: ans (where ans is the value of i that minimizes |n/2 - i| and satisfies left * 2 >= lsum and right * 2 >= rsum)
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing the number of houses, and `a`, a string of length `n` consisting only of '0' and '1'. It calculates and prints the optimal position `i` such that the number of residents preferring to live on the left side up to position `i` is at least half of those up to `i`, and the number of residents preferring to live on the right side from position `i` to the end is also at least half of those from `i` to the end. If no such position exists, it prints -1.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: `func_1()` has already been called three times.
    #
    #Explanation: The loop runs for a number of iterations specified by the user input. Based on the provided output states, each iteration of the loop calls `func_1()`. After the loop executes 3 times, `func_1()` has been called twice. Therefore, if the loop were to run to completion, `func_1()` would be called as many times as the loop iterates. Since no further information about the changes inside `func_1()` or any other variables outside the loop is given, we can conclude that `func_1()` will be called one more time if the loop completes all its iterations.
#Overall this is what the function does:The function does not accept any parameters and does not return anything. It reads an integer from user input, which specifies the number of times to call `func_1()`. After reading the input, it calls `func_1()` exactly three times. The final state of the program is that `func_1()` has been called three times.

