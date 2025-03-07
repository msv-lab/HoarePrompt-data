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
        
    #State: n is an input integer, a is a new input string, S is a list of lists where each inner list represents the cumulative count of '0's and '1's encountered in the string `a` up to that point, starting with the initial count [0, 0].
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
        
    #State: ans is the index closest to the middle of the string `a` that satisfies the conditions specified in the loop.
    print(ans)
    #This is printed: ans (where ans is the index closest to the middle of the string `a` that satisfies the conditions specified in the loop)
#Overall this is what the function does:The function `func_1` reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It calculates and prints an index `ans` that is closest to the middle of the string `a` while satisfying specific conditions related to the cumulative counts of '0's and '1's on the left and right sides of the index.

#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of the characters '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of the characters '0' and '1'.
#Overall this is what the function does:The function reads an integer input, which indicates the number of times to call `func_1()`. It does not directly use or modify the parameters `n` and `a` as described in the annotations. The final state of the program is that `func_1()` is called the specified number of times, but the function itself does not return any value or modify the input parameters `n` and `a`.

