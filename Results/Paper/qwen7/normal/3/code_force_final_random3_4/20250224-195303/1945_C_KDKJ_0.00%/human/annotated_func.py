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
        
    #State: Output State: The final state of `S` will be a list containing sublists `[x, y]` for each character in the string `a`, where `x` is the count of '0's encountered so far and `y` is the count of '1's encountered so far. The length of `S` will be equal to the length of the input string `a` plus one, as a new sublist is appended to `S` for each iteration of the loop.
    #
    #In natural language: After the loop has executed all its iterations, the list `S` will contain a sublist for each character in the input string `a`. Each sublist will have two elements: the first element will be the total count of '0's encountered up to that point, and the second element will be the total count of '1's encountered up to that point. The length of `S` will be one more than the length of the input string `a`, as a new sublist is added for each character processed.
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
        
    #State: The value of `ans` is the index `i` that minimizes the absolute difference between `i` and `n / 2`, while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum` for all executed iterations of the loop.
    print(ans)
    #This is printed: ans (where ans is the index i that minimizes |i - n / 2| and satisfies left * 2 >= lsum and right * 2 >= rsum for all executed iterations of the loop)
#Overall this is what the function does:The function reads an integer `n` and a binary string `a` of length `n`. It then constructs a list `S` where each element contains the counts of '0's and '1's encountered up to that point in the string `a`. After processing the string, it finds and prints the index `i` that minimizes the absolute difference between `i` and `n/2`, while ensuring that the number of '0's and '1's on both sides of `i` meet specific conditions.

#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: The function `func_1()` has been called three times, and the loop will continue to call `func_1()` as long as the user inputs a positive integer value.
    #
    #Explanation: Based on the given information, each iteration of the loop calls `func_1()`. After the loop has executed 3 times, it means that the user has inputted a positive integer three consecutive times. Therefore, after all iterations of the loop have finished, `func_1()` will have been called as many times as the user provided positive integers. The loop will terminate when the user inputs a non-positive integer (0 or negative).
#Overall this is what the function does:The function does not accept any parameters and does not return anything. It repeatedly calls another function `func_1()` three times based on user input. The loop continues until the user inputs a non-positive integer (0 or negative). After three valid positive integer inputs, the loop terminates.

