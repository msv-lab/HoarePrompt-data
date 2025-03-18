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
        
    #State: `n` is the new input integer, `a` is `"0101"`, `S` is `[[0, 0], [1, 0], [1, 1], [2, 1], [2, 2]]`.
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
        
    #State: n is 5, a is "0101", S is [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2]], ans is 0, satisfy is 0.
    print(ans)
    #This is printed: 0
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It calculates and prints an index `ans` that represents a position in the string `a` where a certain balance condition is met or is closest to being met.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2()`.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: No variables are present in the function signature of `func_2()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and repeatedly calls `func_1` a number of times specified by user input. It does not return any value.

