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
        
    #State: `S` is a list containing `n + 1` sublists, where each sublist `[x, y]` represents the cumulative count of '0's and '1's in the string `a` up to that point. The last sublist in `S` will be `[count of '0's in a, count of '1's in a]`
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
        
    #State: `S` remains unchanged, `ans` is the index `i` that satisfies the conditions `left * 2 < lsum` or `right * 2 < rsum` and `abs(n / 2 - i) <= abs(n / 2 - ans)`, `satisfy` remains 0.
    print(ans)
    #This is printed: ans (where ans is the index i that satisfies the conditions `left * 2 < lsum` or `right * 2 < rsum` and `abs(n / 2 - i) <= abs(n / 2 - ans)`)
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `a` of length `n` consisting only of '0' and '1'. It computes the cumulative counts of '0's and '1's at each position in the string `a` and stores these counts in a list `S`. After processing, the function prints the index `ans` that satisfies the conditions: the cumulative count of '0's on the left side of the index is less than half the total count of characters on that side, and the cumulative count of '1's on the right side of the index is less than half the total count of characters on that side. If multiple indices satisfy these conditions, the one closest to the middle of the string is chosen. The function does not return any value; it only prints the result.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The initial state remains unchanged, as the function `func_2` does not take any parameters and the loop body only calls `func_1`, which does not modify any variables in the initial state.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It reads an integer from the user input, and for each integer value, it calls the function `func_1`. The function `func_2` does not modify any external variables or state. The final state of the program remains unchanged except for the side effects caused by the calls to `func_1`.

