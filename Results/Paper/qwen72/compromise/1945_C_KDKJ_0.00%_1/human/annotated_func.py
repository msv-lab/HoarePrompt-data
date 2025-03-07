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
        
    #State: `S` is a list containing `n + 1` sublists, where each sublist `[x, y]` at index `i` (0 ≤ i ≤ n) represents the number of '0's and '1's, respectively, in the string `a` from the start up to the `i-1`-th character. The last sublist in `S` will be `[count of '0's in a, count of '1's in a]` and the first sublist will remain `[0, 0]`.
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
        
    #State: `ans` is the index `i` (0 ≤ i ≤ n) that satisfies the condition `left * 2 >= lsum` and `right * 2 >= rsum` and is closest to `n / 2`. If no such index exists, `ans` remains 0. `satisfy` remains 0.
    print(ans)
    #This is printed: ans (where ans is the index i (0 ≤ i ≤ n) that satisfies the conditions left * 2 >= lsum and right * 2 >= rsum and is closest to n / 2, or 0 if no such index exists)
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `a` of length `n` consisting only of '0' and '1'. It calculates the index `i` (0 ≤ i ≤ n) in the string `a` such that the number of '0's in the left part of the string (from the start up to the `i-1`-th character) is at least half the total characters in that part, and the number of '1's in the right part of the string (from the `i`-th character to the end) is at least half the total characters in that part. The function prints the index `i` that is closest to `n / 2` and satisfies these conditions, or prints 0 if no such index exists.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads input from the user and calls another function `func_1()` for each test case.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: The loop has executed `func_1()` a number of times equal to the integer input provided by the user. The variables in the function signature remain unchanged as they are not used within the loop.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer from the user, representing the number of test cases. For each test case, it calls the function `func_1()`. The function does not return any value. After the function concludes, the loop has executed `func_1()` a number of times equal to the integer input provided by the user. The variables in the function signature remain unchanged as they are not used within the function.

