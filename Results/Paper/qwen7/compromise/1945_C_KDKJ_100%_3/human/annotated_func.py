#State of the program right berfore the function call: n is an integer representing the number of houses, and a is a string of length n consisting only of '0' and '1', where '0' indicates a resident wants to live on the left side and '1' indicates a resident wants to live on the right side.
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
        
    #State: Output State: `n` is an input integer, `a` is a string of length `n` consisting only of '0' and '1', and `S` is a list containing `n+1` sublists, where the first element of each sublist is the count of '0's encountered up to that point in the string `a`, and the second element is the count of '1's encountered up to that point.
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
        
    #State: Output State: `ans` is the index `i` that minimizes the absolute difference between `i` and `n/2` while satisfying the condition `left * 2 >= lsum` and `right * 2 >= rsum`, where `left` is the count of '0's up to index `i`, `lsum` is `i`, `right` is the count of '1's from index `i` to the end, and `rsum` is `n - i`.
    print(ans)
    #This is printed: 3
#Overall this is what the function does:The function accepts an integer `n` representing the number of houses and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident wants to live on the left side and '1' indicates a resident wants to live on the right side. It calculates and returns the index `i` that minimizes the absolute difference between `i` and `n/2` while ensuring that the number of residents wanting to live on the left side up to index `i` is at least half of the number of positions considered so far, and the number of residents wanting to live on the right side from index `i` to the end is also at least half of the remaining positions.

#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: a is a string of length n consisting only of '0' and '1'. The value of n remains unchanged and is within the range 3 <= n <= 3 * 10^5. The number of iterations of the loop is determined by user input, but the content of the string a does not change within the loop.
#Overall this is what the function does:The function accepts no parameters and returns a string of length n consisting only of '0' and '1', where n is an integer such that 3 <= n <= 3 * 10^5. The function reads user input to determine the number of iterations of a loop, which calls another function `func_1` but does not modify the string `a`. After the loop completes, the function returns the original string `a` unchanged.

