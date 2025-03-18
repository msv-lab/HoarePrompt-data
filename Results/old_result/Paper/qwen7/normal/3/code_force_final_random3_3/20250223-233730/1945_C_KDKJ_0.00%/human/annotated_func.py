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
        
    #State: Output State: The final state of `a` is an empty string since the loop processes each character of the initial string until it is completely consumed. `S` is a list containing all intermediate states of `[x, y]` for each iteration of the loop, where `x` is incremented by 1 if the current character is '0', and `y` is incremented by 1 if the current character is '1'. Specifically, `S` will contain a list of sublists, with each sublist corresponding to the values of `x` and `y` after processing each character of the original string `a`.
    #
    #In other words, `S` will be a list of pairs, where each pair represents the counts of '0's and '1's encountered up to that point in the string `a`, starting from the beginning and ending with the counts of the entire string.
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
        
    #State: After the loop executes all iterations, `i` is `n-1`, `left` is `S[n-1][0]`, `lsum` is the sum of all `x` values in `S`, `rsum` is 0, and `ans` is the index `i` that minimizes the absolute difference between `i` and `n/2` while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum`.
    print(ans)
    #This is printed: n-1
#Overall this is what the function does:The function processes a binary string `a` of length `n` (where 3 ≤ n ≤ 3⋅10^5) and calculates an index `ans` that satisfies certain conditions related to the counts of '0's and '1's in the string. Specifically, it finds an index `i` such that the number of '0's and '1's counted up to `i` meet specific criteria and the index is closest to `n/2`. The function then prints the value of `ans`, which is `n-1` after processing the entire string.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 300000, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: `n` is an integer such that 3 ≤ n ≤ 300000, `a` is a string of length `n` consisting only of '0' and '1', and `func_1()` has been called three times.
    #
    #Explanation: The loop runs for a number of times specified by the user input, which is decremented by 1 each time the loop iterates. After the loop executes all its iterations, `func_1()` will have been called as many times as the initial input value minus the number of iterations it took to fully execute the loop. Given that the loop executes until the input value reaches zero, if it executed 3 times, it means the initial input was 3 or more, and now it is 0. Therefore, `func_1()` would have been called exactly the number of times equal to the initial input value.
#Overall this is what the function does:The function does not accept any parameters and does not return any value. It reads an integer input specifying the number of times to call `func_1()`, then calls `func_1()` that many times. After the loop completes, the state of the program includes an integer `n` (initially between 3 and 300000) and a binary string `a` of length `n`, with `func_1()` having been called the number of times specified by the input.

