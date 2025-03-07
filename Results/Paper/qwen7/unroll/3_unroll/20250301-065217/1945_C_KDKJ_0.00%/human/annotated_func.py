#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'.
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
        
    #State: Output State: `a` is an input string consisting only of '0' and '1', `n` is the length of the input string `a`, `S` is a list containing `n` sublists. Each sublist contains two elements where the first element represents the count of '0's encountered up to that point in the string `a`, and the second element represents the count of '1's encountered up to that point.
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
        
    #State: Output State: `satisfy` is 0, `a` is an input string consisting only of '0' and '1', `n` is the length of the input string `a`, `S` is a list containing `n` sublists, each sublist contains two elements where the first element represents the count of '0's encountered up to that point in the string `a`, and the second element represents the count of '1's encountered up to that point, `ans` is the index `i` that satisfies the condition in the loop or remains 0 if no such index exists.
    print(ans)
    #This is printed: 0
#Overall this is what the function does:The function accepts an integer `n` such that 3 ≤ n ≤ 3⋅10^5 and a string `a` of length `n` consisting only of '0' and '1'. It constructs a list `S` where each element is a sublist containing the counts of '0's and '1's encountered up to that point in the string `a`. After processing the string, it finds an index `i` that satisfies a specific condition related to the counts of '0's and '1's on both sides of the index. If such an index exists, it returns the value of `i`; otherwise, it returns 0.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: a is a string of length n consisting only of '0' and '1', unchanged.
#Overall this is what the function does:The function does not accept any parameters and does not return any value. It reads an integer from user input, which represents the number of times to call `func_1()`. After calling `func_1()` multiple times, the string `a` remains unchanged.

