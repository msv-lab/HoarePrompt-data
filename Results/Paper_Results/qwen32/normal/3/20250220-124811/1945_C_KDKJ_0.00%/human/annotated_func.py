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
        
    #State: `S` is `[[0, 0], ..., [count_0, count_not_0]]`, where `count_0` is the number of '0's and `count_not_0` is the number of non-'0's in the string `a`.
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
        
    #State: `S` is `[[0, 0], ..., [count_0, count_not_0]]`; `ans` is the index `i` closest to `n / 2` that satisfies `left * 2 >= lsum` and `right * 2 >= rsum`; `satisfy` is 0; `n` is greater than 0.
    print(ans)
    #This is printed: ans (where ans is the index in S closest to n / 2 that satisfies left * 2 >= lsum and right * 2 >= rsum)
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It calculates and prints the index `i` closest to `n / 2` where the number of '0's to the left of `i` is at least half of the total elements to the left, and the number of '1's to the right of `i` is at least half of the total elements to the right.

#State of the program right berfore the function call: No variables in the function signature.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: `count` is `n-1`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It performs a loop that runs a number of times specified by the user input, calling `func_1` during each iteration. The final state of the program after it concludes depends on the actions performed by `func_1` during each iteration, but `func_2` itself does not return any specific value.

