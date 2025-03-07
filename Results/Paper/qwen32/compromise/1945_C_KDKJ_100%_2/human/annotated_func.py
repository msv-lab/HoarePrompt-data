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
        
    #State: `n` is the input integer, `a` is the input string of length `n` consisting only of the characters '0' and '1', `S` is `[[0, 0], [count_0, count_1]]`.
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
        
    #State: `n` is the input integer, `a` is the input string of length `n` consisting only of the characters '0' and '1', `S` is `[[0, 0], [count_0, count_1]]`, `ans` is the calculated index that meets the loop conditions.
    print(ans)
    #This is printed: ans (where ans is the calculated index that meets the loop conditions specified in the code)
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It calculates and prints an index `ans` that minimizes the absolute difference between the index and half of `n`, under the condition that the number of '0's on the left side of the index is at least half the length of the left side, and the number of '1's on the right side is at least half the length of the right side.

#State of the program right berfore the function call: No variables in the function signature. The function `func_2` does not have any parameters and thus no preconditions can be derived from its signature alone.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The function `func_1()` was called `int(input())` times.
#Overall this is what the function does:The function `func_2` repeatedly calls `func_1` a number of times specified by user input and performs no other actions. It does not accept any parameters and does not return any value.

