#State of the program right berfore the function call: No variables are passed to the function `func_1()`. The function reads `n` and `a` from the standard input, where `n` is an integer representing the number of houses (3 ≤ n ≤ 3·10^5), and `a` is a string of length `n` consisting only of '0' and '1', representing the preferences of the residents.
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
        
    #State: `S` is a list containing `n+1` sublists, where each sublist `[x, y]` at index `i` (0 ≤ i ≤ n) represents the count of '0's and '1's in the first `i` characters of the string `a`. The last sublist in `S` is `[count of '0's in a, count of '1's in a]`. The values of `n` and `a` remain unchanged.
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
        
    #State: `ans` is the index `i` (0 ≤ i ≤ n) that minimizes the absolute difference `abs(n / 2 - i)` while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum`. The list `S` remains unchanged.
    print(ans)
    #This is printed: - The value of `ans` will be the index `i` that satisfies the conditions and is closest to `n / 2`.
    #
    #Since the exact values of `S`, `lsum`, and `rsum` are not provided, we can't compute the exact numerical value of `ans`. However, based on the given conditions, the print statement will output the index `i` that minimizes the absolute difference `abs(n / 2 - i)` while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads two inputs from the standard input: an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', representing the preferences of the residents. It then calculates and prints an index `i` (0 ≤ i ≤ n) that minimizes the absolute difference `abs(n / 2 - i)` while ensuring that the number of '0's in the first `i` characters of `a` is at least half the length of the first `i` characters, and the number of '1's in the remaining characters of `a` is at least half the length of the remaining characters. If no such index exists, it prints `-1`. The values of `n` and `a` remain unchanged after the function execution.

#State of the program right berfore the function call: None.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: None.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer from the user input, and for each value in the range of this integer, it calls the function `func_1`. The function does not return any value, and the state of the program after the function concludes is the same as before, except for any side effects caused by the calls to `func_1`.

