#State of the program right berfore the function call: n is a positive integer representing the number of houses, a is a string of length n consisting only of '0' and '1', S is a list of lists where each sublist contains two integers representing cumulative counts of '0's and '1's encountered up to that point in the string a.
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
        
    #State: `S` is `[[0, 0], [x1, y1], [x2, y2], ..., [xf, yf]]` where `xf` is the number of `'0'` characters in `a` and `yf` is the number of non-`'0'` characters in `a`.
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
        
    #State: S is `[[0, 0], [x1, y1], [x2, y2], ..., [xf, yf]]; ans is the index i that minimizes abs(n / 2 - i) while satisfying left * 2 >= lsum and right * 2 >= rsum`.
    print(ans)
    #This is printed: ans (where ans is the index i that minimizes abs(n / 2 - i) while satisfying left * 2 >= lsum and right * 2 >= rsum)
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It calculates and prints an index `i` that minimizes the absolute difference between `n/2` and `i`, under the condition that the number of '0's in the left part of the string (up to index `i`) is at least half the length of that part, and the number of '1's in the right part of the string (from index `i` to the end) is at least half the length of that part.

#State of the program right berfore the function call: No variables in the function signature. The function `func_2` does not take any parameters and its functionality is to iterate over multiple test cases by calling `func_1` for each test case.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The input to `int(input())` must be an integer greater than or equal to 0, and `func_1()` has been executed as many times as the value of that integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer from the input, which represents the number of test cases, and then calls `func_1` that many times.

