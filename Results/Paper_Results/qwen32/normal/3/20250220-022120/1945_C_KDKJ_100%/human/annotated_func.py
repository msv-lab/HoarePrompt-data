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
        
    #State: S is a list of coordinates starting from [0, 0] and ending with [x, y] after processing all characters in a.
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
        
    #State: `S` is a list of coordinates starting from [0, 0] and ending with [x, y]; `n` is greater than or equal to 0; `ans` is the value of `i` that is closest to `n / 2` and meets the conditions `left * 2 >= lsum` and `right * 2 >= rsum`, or `-1` if no such `i` exists.
    print(ans)
    #This is printed: ans (where ans is the index i in the list S that is closest to n / 2 and meets the conditions left * 2 >= lsum and right * 2 >= rsum, or -1 if no such i exists)
#Overall this is what the function does:The function reads a positive integer `n` and a string `a` of length `n` consisting of '0's and '1's. It calculates and prints the index `i` in the string `a` that is closest to `n / 2` and meets the conditions where the number of '0's up to index `i` is at least half of `i` and the number of '1's from index `i` to the end is at least half of the remaining length. If no such index exists, it prints `-1`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. The function `func_2` does not take any parameters and does not have any direct relationship with the variables described in the problem description.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: `n` is a positive integer doubled minus 1 after the last iteration.
#Overall this is what the function does:The function `func_2` prompts the user for an integer input, then calls `func_1` that many times. The function does not accept any parameters and does not return a value. The state of the program after execution depends on the actions performed by `func_1` during each call.

