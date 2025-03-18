#State of the program right berfore the function call: No variables are passed in the function signature, but within the function, n is an integer representing the number of houses (3 ≤ n ≤ 3·10^5), and a is a string of length n consisting only of '0' and '1'.
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
        
    #State: `n` is an input integer, `a` is a string consisting only of '0' and '1', `S` is a list containing sublists where each sublist represents the cumulative count of '0's and '1's encountered in the string `a` up to that point. The final sublist in `S` will be `[count_of_0s, count_of_1s]` where `count_of_0s` is the total number of '0's in `a` and `count_of_1s` is the total number of '1's in `a`.
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
        
    #State: `n` is the same input integer, `a` is the same string consisting only of '0' and '1', `S` is the same list containing sublists where each sublist represents the cumulative count of '0's and '1's encountered in the string `a` up to that point, and `ans` is the value of `i` that minimizes the absolute difference between `n / 2` and `i` while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum`.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `i` that meets the above criteria.
    #
    #Since the exact values of `n` and `a` are not provided, we can't compute the exact numerical value of `ans`. However, based on the structure of the problem, the print statement will output the value of `i` that minimizes the absolute difference between `n / 2` and `i` while satisfying the given conditions.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads an integer `n` and a string `a` of length `n` consisting only of '0' and '1'. It calculates the cumulative counts of '0's and '1's in the string `a` and stores these counts in a list `S`. The function then determines the value of `i` (0 ≤ i ≤ n) that minimizes the absolute difference between `n / 2` and `i` while ensuring that the number of '0's on the left side of the split (up to index `i`) is at least half the length of the left side, and the number of '1's on the right side of the split (from index `i` to the end) is at least half the length of the right side. Finally, it prints this value of `i`. If no such `i` exists, it prints `-1`.

#State of the program right berfore the function call: None of the variables in the function signature are used.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: None of the variables in the function signature are used. 
    #
    #The loop iterates a number of times specified by the user input, and each iteration calls the function `func_1()`. However, since `func_1()` does not modify any variables in the function signature and no variables are used within the loop, the initial state remains unchanged after all iterations of the loop have finished.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It reads an integer from user input, which determines the number of times it will call the function `func_1`. The function `func_1` is called repeatedly, but since `func_1` does not modify any variables in the function signature of `func_2`, the overall state of the program remains unchanged after `func_2` concludes.

