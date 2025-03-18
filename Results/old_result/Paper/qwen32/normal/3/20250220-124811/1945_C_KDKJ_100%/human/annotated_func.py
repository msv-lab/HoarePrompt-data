#State of the program right berfore the function call: n is a positive integer representing the number of houses, and a is a string of length n consisting only of '0' and '1'.
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
        
    #State: `S` is `[[0, 0], [x1, y1], ..., [xn, yn], [count_0, count_not_0]]` where `count_0` is the number of `'0'`s in `a` and `count_not_0` is the number of non-`'0'`s in `a`.
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
        
    #State: S is `[[0, 0], [x1, y1], ..., [xn, yn], [count_0, count_not_0]]`, `ans` is the value of `i` from 0 to `n` that minimizes `abs(n / 2 - i)` while satisfying `left * 2 >= lsum` and `right * 2 >= rsum`.
    print(ans)
    #This is printed: ans (where ans is the index i from 0 to n that minimizes abs(n / 2 - i) while satisfying left * 2 >= lsum and right * 2 >= rsum)
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It then determines and prints the index `i` from 0 to `n` that minimizes the absolute difference between `n / 2` and `i`, while ensuring that the number of '0's in the left segment (up to index `i`) is at least half the length of that segment and the number of '1's in the right segment (from index `i` to the end) is at least half the length of that segment.

#State of the program right berfore the function call: The function `func_2` does not have any parameters. It reads the number of test cases from the input and iterates over each test case, calling `func_1` for each one.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The function `func_1()` has been executed `int(input())` times, `func_2` does not have any parameters.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads the number of test cases from the input and iterates over each test case, calling `func_1` for each one. After all test cases are processed, the function concludes without returning any value.

