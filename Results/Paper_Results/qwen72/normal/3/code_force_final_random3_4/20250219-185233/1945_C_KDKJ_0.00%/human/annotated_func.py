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
        
    #State: `n` is the input integer, `a` is the input string, `S` is a list containing `[0, 0]` followed by `len(a)` sublists, each representing the cumulative count of '0's and '1's up to that point in the string `a`. The last sublist in `S` contains the total count of '0's and '1's in the entire string `a`.
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
        
    #State: `n` is the input integer, `a` is the input string, `S` is a list containing `[0, 0]` followed by `len(a)` sublists, each representing the cumulative count of '0's and '1's up to that point in the string `a`. The last sublist in `S` contains the total count of '0's and '1's in the entire string `a`. `ans` is the index `i` that satisfies the conditions `left * 2 >= lsum` and `right * 2 >= rsum` and is closest to `n / 2` in absolute value, or remains 0 if no such index is found. `satisfy` is 0.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans`.
    #   - Since the exact values of `a` and `n` are not provided, we cannot compute the exact numerical value of `ans`.
    #   - However, based on the conditions and the structure of the problem, the print statement will output the index `i` that satisfies the given conditions and is closest to `n / 2`, or 0 if no such index is found.
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `a` of length `n` consisting only of '0' and '1'. It computes the cumulative counts of '0's and '1's at each position in the string `a` and stores these counts in a list `S`. The function then finds the index `i` in the string `a` such that the cumulative count of '0's in the left part of the string up to index `i` is at least half of the total count of characters in that part, and the cumulative count of '1's in the right part of the string from index `i` to the end is at least half of the total count of characters in that part. The index `i` that is closest to `n / 2` in absolute value and satisfies these conditions is printed. If no such index is found, the function prints `0`.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: `int(input())` iterations have completed, `_` is `int(input()) - 1`, and `func_1()` has been called `int(input())` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It reads an integer from the user input, and then calls the function `func_1` that many times. After the function concludes, the specified number of iterations have completed, and `func_1` has been called the same number of times as the input integer.

