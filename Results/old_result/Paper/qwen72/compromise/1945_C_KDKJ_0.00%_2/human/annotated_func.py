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
        
    #State: `S` is a list containing `n + 1` sublists, where each sublist `[x, y]` represents the cumulative count of '0's and '1's encountered in the string `a` up to that point. The last sublist in `S` will be `[count of '0's in a, count of '1's in a]`.
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
        
    #State: `S` remains unchanged, `ans` is the index `i` that satisfies the conditions `left * 2 < lsum` or `right * 2 < rsum` and `abs(n / 2 - i) <= abs(n / 2 - ans)`, or remains 0 if no such index is found, `satisfy` remains 0.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans`.
    #   - If no index `i` satisfies the conditions, `ans` will be 0.
    #   - If an index `i` satisfies the conditions, `ans` will be that index.
    #
    #Since the exact values of `left`, `lsum`, `right`, `rsum`, and `n` are not provided, we can only describe the output based on the given conditions.
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `a` of length `n` consisting only of '0' and '1'. It calculates the cumulative counts of '0's and '1's in the string `a` and stores them in a list `S`. The function then finds an index `i` (if any) such that the cumulative counts of '0's and '1's up to that index and from that index to the end of the string satisfy certain conditions. Specifically, it looks for an index where the number of '0's is less than half the total count up to that index, and the number of '1's is less than half the total count from that index to the end. If such an index is found, it prints that index; otherwise, it prints 0. The list `S` and the variable `satisfy` remain unchanged throughout the function.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: None of the variables are used in the function signature.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return a value. It reads an integer from the user input, and for each value in the range of this integer, it calls the function `func_1`. The final state of the program after `func_2` concludes is that `func_1` has been called a number of times equal to the user-provided integer.

