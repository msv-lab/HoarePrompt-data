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
        
    #State: Output State: The final output state after the loop executes all its iterations is as follows: `a` is an empty string (since each character in `a` is processed exactly once during the loop); `S` is a list where each sublist contains the cumulative count of '0's and '1's in the original string `a`. Specifically, `S[i][0]` represents the total count of '0's and `S[i][1]` represents the total count of '1's in `a`. The list `S` will have a length equal to `n + 1`, with the last element being the counts of '0's and '1's in the entire string `a`.
    #
    #In simpler terms, after processing all characters in the string `a`, `S` will contain the total counts of '0's and '1's in `a`, and `a` itself will be an empty string since all its characters have been processed.
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
        
    #State: Output State: `i` is `n-1`, `left` is `S[n-1][0]`, `lsum` is `S[n-1][0] + S[n-1][1]`, `rsum` is `n - (S[n-1][0] + S[n-1][1])`, and `ans` is the index `i` that satisfies the conditions within the loop after all iterations.
    #
    #Explanation: After all iterations of the loop, the variable `i` will have the value of `n-1` since the loop runs from `0` to `n-1`. The variables `left`, `lsum`, and `rsum` will hold the values corresponding to the last element in the list `S`. The variable `ans` will be the index `i` that meets the specified conditions during the loop's execution. Given the nature of the conditions checked within the loop, `ans` will be the index `i` that minimizes the absolute difference between `i` and `n/2` while also satisfying the balance condition involving `left`, `lsum`, `right`, and `rsum`.
    print(ans)
    #This is printed: n-1
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing the number of houses, and `a`, a string of length `n` consisting only of '0' and '1'. The function processes the string `a` to count the occurrences of '0' and '1' and stores these counts in a list `S`. After processing, it determines the optimal index `i` that minimizes the absolute difference between `i` and `n/2` while ensuring a balanced distribution of '0's and '1's on either side of `i`. Finally, it prints the index `i` that satisfies these conditions.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: `n` is an integer such that \(3 \leq n \leq 3 \cdot 10^5\), and `a` is a string of length `n` consisting only of '0' and '1', and `func_1()` has been called three times.
    #
    #In natural language: After the loop has executed all its iterations, `n` remains an integer within the range \(3 \leq n \leq 3 \cdot 10^5\), and `a` remains a string of length `n` consisting only of '0' and '1'. Additionally, `func_1()` has been called three times as specified by the loop condition. The state of these variables does not change during the loop's execution; they retain their initial conditions except for the number of times `func_1()` has been called, which is now three.
#Overall this is what the function does:The function does not accept any parameters and does not return any value. It reads an integer `n` and a binary string `a` of length `n` from standard input, then calls the function `func_1()` three times. After these operations, it leaves the values of `n` and `a` unchanged, except that `func_1()` has been called three times.

