#State of the program right berfore the function call: None, as the function does not take any parameters and directly reads input from the user.
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
        
    #State: `n` remains unchanged, `a` remains unchanged, `S` is a list containing `len(a) + 1` sublists, where each sublist `[x, y]` represents the cumulative count of '0's and non-'0's encountered in the string `a` up to that point, starting from the initial sublist `[0, 0]`. The final sublist in `S` will contain the total count of '0's and non-'0's in the string `a`.
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
        
    #State: `n` remains unchanged, `a` remains unchanged, `S` remains unchanged, `ans` is 2.
    print(ans)
    #This is printed: 2
#Overall this is what the function does:The function reads two inputs from the user: an integer `n` and a string `a`. It then processes the string `a` to create a list `S` where each element `[x, y]` represents the cumulative count of '0's and non-'0's encountered in `a` up to that point, starting from `[0, 0]`. The function calculates an integer `ans` based on the conditions that the cumulative counts of '0's and non-'0's in the left and right segments of the string `a` must satisfy certain criteria. Finally, it prints the value of `ans`. The function does not return any value.

#State of the program right berfore the function call: None of the variables are passed to the function `func_2()`. The function reads the number of test cases from the standard input and calls `func_1()` for each test case.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: The loop has executed `func_1()` for each test case specified by the input. The number of iterations is equal to the integer value provided by the input. The initial state of the variables outside the loop remains unchanged.
#Overall this is what the function does:The function `func_2` reads an integer from the standard input representing the number of test cases. It then calls the function `func_1` for each test case. After the function completes, the number of times `func_1` has been called is equal to the integer value read from the input, and the initial state of any variables outside the function remains unchanged.

