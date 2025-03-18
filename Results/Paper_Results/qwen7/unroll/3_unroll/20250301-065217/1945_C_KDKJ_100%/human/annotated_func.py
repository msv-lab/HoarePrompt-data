#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3*10^5, and a is a string of length n consisting only of '0' and '1'.
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
        
    #State: Output State: `a` is an input string consisting only of '0' and '1', and `n` is the length of this string; `S` is a list containing one sublist where the first element is the count of '0's in `a` and the second element is the count of '1's in `a`.
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
        
    #State: Output State: `a` is an input string consisting only of '0' and '1', and `n` is the length of this string; `S` is a list containing one sublist where the first element is the count of '0's in `a` and the second element is the count of '1's in `a`; `ans` is the index `i` that minimizes the absolute difference between `i` and `n/2` while satisfying the condition `left * 2 < lsum` or `right * 2 < rsum`.
    print(ans)
    #This is printed: ans (where ans is the index that minimizes the absolute difference between i and n/2 while satisfying the condition left * 2 < lsum or right * 2 < rsum)
#Overall this is what the function does:The function reads an integer `n` and a binary string `a` of length `n`. It then calculates the counts of '0's and '1's at each position in the string and stores these counts in a list `S`. Afterward, it finds the index `i` that minimizes the absolute difference between `i` and `n/2` while ensuring that the number of '0's to the left of `i` is less than half the number of positions to the left of `i`, and the number of '1's to the right of `i` is less than half the number of positions to the right of `i`. Finally, it prints the found index `i`.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 300000, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: a is a string of length n consisting only of '0' and '1', n is an integer such that 3 ≤ n ≤ 300000. The value of n and the content of the string a do not change after the loop executes all the iterations.
#Overall this is what the function does:The function does not accept any parameters and does not return anything. It reads an integer `n` from user input, which must be between 3 and 300,000 inclusive, and then iterates this number of times, calling another function `func_1()` each time. After completing these iterations, the function outputs a string `a` of length `n` consisting only of '0' and '1', ensuring that the values of `n` and `a` remain unchanged from their initial state before the loop begins.

