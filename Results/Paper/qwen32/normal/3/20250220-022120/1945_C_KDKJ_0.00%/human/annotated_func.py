#State of the program right berfore the function call: n is an integer representing the number of houses in the village such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of the characters '0' and '1'.
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
        
    #State: `n` is an integer provided by the user input, `a` is a string provided by the user input, `S` is a list of `[x, y]` pairs where the first element is `[0, 0]` and each subsequent element `[x, y]` represents the cumulative counts of `'0'`s and non-`'0'`s up to that character in the string `a`.
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
        
    #State: Output State: `n` is an integer provided by the user input and must be greater than 0, `a` is a string provided by the user input, `S` is a list of `[x, y]` pairs where the first element is `[0, 0]` and each subsequent element `[x, y]` represents the cumulative counts of `'0'`s and non-`'0'`s up to that character in the string `a`, `ans` is the index `i` that is closest to `n / 2` and satisfies the condition `left * 2 >= lsum` and `right * 2 >= rsum`, and `satisfy` is 0.
    print(ans)
    #This is printed: ans (where ans is the index i that is closest to n / 2 and satisfies the condition left * 2 >= lsum and right * 2 >= rsum)
#Overall this is what the function does:The function reads an integer `n` and a string `a` of length `n` consisting of '0's and '1's. It calculates and prints an index `i` that is closest to `n / 2` and satisfies the condition where the number of '0's on the left of `i` is at least half of the total characters to the left of `i`, and the number of '1's on the right of `i` is at least half of the total characters to the right of `i`.

#State of the program right berfore the function call: The function `func_2` does not take any parameters. It implicitly relies on the input being available via the `input()` function, which should provide the number of test cases followed by the details of each test case as described in the problem statement.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The input to `int(input())` must be a positive integer greater than or equal to the number of test cases; `func_1()` has been called for each of the test cases specified by the input integer.
#Overall this is what the function does:The function `func_2` reads the number of test cases from the input and processes each test case by calling `func_1`. It does not return any value explicitly but performs actions based on the details of each test case provided through the input.

