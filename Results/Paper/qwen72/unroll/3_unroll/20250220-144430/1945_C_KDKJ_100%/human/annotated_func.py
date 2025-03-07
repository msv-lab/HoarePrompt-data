#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of '0' and '1'.
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
        
    #State: `S` is a list containing `n+1` sublists, where each sublist `[x, y]` at index `i` (0-indexed) represents the count of '0's and '1's from the start of the string `a` up to the `i-1`-th character. The last sublist in `S` will be `[count of '0's in a, count of '1's in a]` and the first sublist remains `[0, 0]`.
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
        
    #State: `S` remains unchanged, `ans` is the index `i` that minimizes the absolute difference between `n / 2` and `i`, while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum`.
    print(ans)
    #This is printed: 2 (where 2 is the index that minimizes the absolute difference between n / 2 and i while satisfying the conditions left * 2 >= lsum and right * 2 >= rsum)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a string `a` of length `n` from the user, where `a` consists only of '0' and '1'. It then computes and prints the index `i` (0-indexed) that minimizes the absolute difference between `n / 2` and `i`, while ensuring that the number of '0's in the left part of the string (up to index `i-1`) is at least half the length of the left part, and the number of '1's in the right part of the string (from index `i` to the end) is at least half the length of the right part. If no such index exists, it prints `-1`.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The variables in the function `func_2` remain unchanged, as the loop only calls `func_1` and does not modify any variables within the loop head or body.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any specific value. It reads an integer from the user input, and for each value in the range of this integer, it calls the function `func_1`. The function itself does not modify any variables or state within `func_2`. The final state of the program after `func_2` concludes is unchanged except for any side effects that `func_1` may have.

