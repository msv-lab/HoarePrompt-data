#State of the program right berfore the function call: n is a positive integer representing the number of houses, and a is a string of length n consisting only of the characters '0' and '1'.
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
        
    #State: `S` is `[[0, 0], [count_0, count_1]]` where `count_0` and `count_1` are the total counts of '0's and '1's in the string `a`, respectively.
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
        
    #State: S is [[0, 0], [count_0, count_1]], ans is the index i that best meets the loop's conditions.
    print(ans)
    #This is printed: ans (where ans is the index of the sublist in S that best meets the loop's conditions)
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It calculates and prints an index `i` that represents a position in the string where the counts of '0's on the left and '1's on the right are balanced in a specific way, or the closest to being balanced.

#State of the program right berfore the function call: No variables are present in the function signature, thus no precondition can be derived from it.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The loop has executed `func_1()` a number of times equal to the integer value provided by the user input. No other variables have been changed or introduced.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It repeatedly calls another function `func_1` a number of times specified by the integer input provided by the user. The function itself does not return any specific value or modify any external variables.

