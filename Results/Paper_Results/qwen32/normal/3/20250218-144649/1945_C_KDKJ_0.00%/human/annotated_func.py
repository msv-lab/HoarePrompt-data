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
        
    #State: `[[0, 0], [0, 1], [1, 1], ..., [count_0, count_1]]`
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
        
    #State: `[[0, 0], [0, 1], [1, 1], ..., [count_0, count_1]]`, `ans` is the index closest to `n/2`, `satisfy` is 0.
    print(ans)
    #This is printed: ans (where ans is the index closest to n/2 in the list of points)
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It then calculates and prints an index `ans` which is the position in the string that is closest to the middle of the string, under the condition that the number of '0's on the left and the number of '1's on the right can each be at most half of their respective totals up to that point.

#State of the program right berfore the function call: No variables in the function signature. The function `func_2` does not take any parameters and is expected to handle input and output operations internally.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: n is 0.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer from the input, which determines how many times it calls another function `func_1`. After completing the loop, it returns the string "Hello, World!".

