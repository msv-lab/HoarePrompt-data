#State of the program right berfore the function call: n is an integer representing the number of houses, and a is a string of length n consisting only of '0' and '1', where '0' indicates a resident prefers to live on the left side of the street, and '1' indicates a resident prefers to live on the right side of the street.
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
        
    #State: Output State: The final state of `S` will be a list containing sublists where the last element of each sublist is equal to the total number of '1's in the string `a`, and the second last element is equal to the total number of '0's in the string `a`.
    #
    #In more detail, after all iterations of the loop, `S` will contain a single sublist where the first element (`x`) is the count of '1's in the string `a`, and the second element (`y`) is the count of '0's in the string `a`.
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
        
    #State: ans is the index i that minimizes the absolute difference between i and n/2 among all indices i where the conditions `left * 2 >= lsum` and `right * 2 >= rsum` hold, or ans is -1 if no such index exists.
    print(ans)
    #This is printed: ans (where ans is the index i that minimizes the absolute difference between i and n/2 among all indices i where the conditions left * 2 >= lsum and right * 2 >= rsum hold, or -1 if no such index exists)
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing the number of houses, and `a`, a string of length `n` consisting only of '0' and '1'. It calculates the optimal index `i` that minimizes the absolute difference between `i` and `n/2` while ensuring that the number of '0's to the left of `i` is at least half the number of positions to the left of `i`, and the number of '1's to the right of `i` is at least half the number of positions to the right of `i`. If no such index exists, it returns `-1`. The function returns the optimal index `i` or `-1`.

#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: The function `func_1()` has been called a total of int(input()) times.
    #
    #Explanation: Given that the loop runs for a number of times specified by the user input, and `func_1()` is called within this loop for each iteration, the final output state will be that `func_1()` has been called exactly equal to the number provided by the user as input. Since the problem does not specify any changes to the function or its parameters within the loop, and no other variables are mentioned as being affected by the loop, the only state change is the number of times `func_1()` has been executed.
#Overall this is what the function does:The function does not accept any parameters and does not return anything. It reads an integer from user input, then calls another function `func_1()` that many times. After completing these calls, the function ends, leaving no variables modified and no value returned.

