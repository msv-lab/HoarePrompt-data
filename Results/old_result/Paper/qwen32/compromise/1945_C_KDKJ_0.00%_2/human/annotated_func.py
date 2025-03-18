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
        
    #State: S is a list of length n+1 where the last element is [count of '0's in a, count of '1's in a].
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
        
    #State: S is a list of length n+1 where the last element is [count of '0's in a, count of '1's in a]; ans is 0; satisfy is 0.
    print(ans)
    #This is printed: 0
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It then calculates and prints an index `ans` which is determined based on the counts of '0's and '1's in the string `a`. The index `ans` is chosen such that the number of '0's to the left of `ans` and the number of '1's to the right of `ans` are as balanced as possible relative to the total counts of '0's and '1's in the string.

#State of the program right berfore the function call: No variables in the function signature.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: No variables in the function signature.
#Overall this is what the function does:The function `func_2` does not accept any parameters and repeatedly calls another function `func_1` a number of times specified by user input. It does not return any value.

