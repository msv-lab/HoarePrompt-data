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
        
    #State: `n` is the new input integer, `a` is the new input string, `S` is `[[0, 0], [1, 0], [1, 1], [2, 1], [2, 2]]` for the example `a = "0101"`.
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
        
    #State: n is the new input integer, a is the new input string, S is [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2]], ans is 3, satisfy is 0.
    print(ans)
    #This is printed: 3
#Overall this is what the function does:The function reads an integer `n` and a string `a` of length `n` consisting of '0's and '1's. It calculates and prints an index `ans` that represents a balance point in the string where the number of '0's and '1's can be considered balanced according to specific conditions.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. It does not take any parameters and does not return any value. It is designed to handle multiple test cases by calling `func_1()` for each test case.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: No variables are present in the function signature of `func_2`. It does not take any parameters and does not return any value. It is designed to handle multiple test cases by calling `func_1()` for each test case. The loop has executed for the number of iterations specified by the integer input, calling `func_1()` in each iteration. The state of other variables not affected by the loop remains unchanged.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It reads an integer input that specifies the number of test cases, and for each test case, it calls the function `func_1()`. The state of the program after execution is that `func_1()` has been called the number of times specified by the input integer, and no other variables or state in the program are modified by `func_2` itself.

