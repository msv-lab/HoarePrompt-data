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
        
    #State: `n` is the integer value obtained from user input, `a` is the string input from the user, `S` is `[[0, 0], [count of '0's after first character, count of non-'0's after first character], ..., [final count of '0's, final count of non-'0's]]`.
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
        
    #State: `n` is the integer value obtained from user input, `a` is the string input from the user, `S` is `[[0, 0], [count of '0's after first character, count of non-'0's after first character], ..., [final count of '0's, final count of non-'0's]]`, `ans` is the index closest to the middle of the string that satisfies the conditions, `satisfy` is 0.
    print(ans)
    #This is printed: ans (where ans is the index in the string `a` that is closest to the middle and satisfies the condition related to the counts of '0's and non-'0's in the string `a`)
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It then determines and prints an index `ans` in the string `a` that is closest to the middle and satisfies certain conditions related to the counts of '0's and '1's on both sides of the index.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. Therefore, no precondition can be derived from the variables in the function signature.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The function `func_1()` is executed `int(input())` times, but the specific state changes depend on the implementation of `func_1()`. No other variables are affected.
#Overall this is what the function does:The function `func_2` does not accept any parameters and repeatedly calls the function `func_1` a number of times specified by the user input. The final state of the program depends on the actions performed by `func_1` during each call.

