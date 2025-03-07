#State of the program right berfore the function call: n is an integer representing the number of houses (3 ≤ n ≤ 3⋅10^5), and a is a string of length n consisting only of '0' and '1', where '0' indicates a resident wants to live on the left side of the street, and '1' indicates a resident wants to live on the right side of the street.
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
        
    #State: Output State: `n` is an input integer, `a` is an input string of length `n` consisting only of '0' and '1', and `S` is a list containing `n+1` sublists. The first sublist is `[0, 0]`, and each subsequent sublist contains two integers where the first integer is the count of '0's encountered up to that point in the string `a`, and the second integer is the count of '1's encountered up to that point.
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
        
    #State: Output State: `satisfy` is 0, `ans` is the index `i` that minimizes the difference between `i` and `n/2` while satisfying the condition `left * 2 < lsum` or `right * 2 < rsum`, where `left` is the count of '0's up to index `i`, `lsum` is the total count of '0's and '1's up to index `i`, `right` is the count of '1's from index `i+1` to the end, and `rsum` is the total count of '0's and '1's from index `i+1` to the end.
    print(ans)
    #This is printed: ans (where ans is the index i that minimizes the difference between i and n/2 while satisfying the condition left * 2 < lsum or right * 2 < rsum)
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing the number of houses (3 ≤ n ≤ 3⋅10^5), and `a`, a string of length `n` consisting only of '0' and '1'. The function calculates and returns the index `i` that minimizes the difference between `i` and `n/2` while ensuring that the number of '0's up to index `i` is less than half the total count of '0's and '1's up to that point, or the number of '1's from index `i+1` to the end is less than half the total count of '0's and '1's from that point onwards.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: a is a string of length n consisting only of '0' and '1', unchanged.
#Overall this is what the function does:The function does not accept any parameters and does not return anything. It reads an integer from input, which represents the number of times to call `func_1()`. After calling `func_1()` multiple times, the state of the variable `a` remains unchanged as it is not modified within the function.

