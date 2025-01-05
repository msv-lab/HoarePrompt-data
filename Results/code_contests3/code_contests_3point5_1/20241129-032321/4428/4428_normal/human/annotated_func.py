#State of the program right berfore the function call: N is a positive integer and S is a string of length N consisting of only 'I' and 'D' characters.**
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `result` is the difference between the count of 'I's and the count of non-'I's in the list `S`. `i` is `N-1`, `N` is greater than 0, and `S` is a list of characters.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`result` is the difference between the count of 'I's and the count of non-'I's in the list `S`. `i` is `N-1`, `N` is greater than 0, and `S` is a list of characters. If `result` is less than 0, then there is no change in the values of `i`, `N`, and `S`.
    print(result)
#Overall this is what the function does:The function `func` reads a positive integer `N` and a string `S` of length `N` consisting of only 'I' and 'D' characters. It then calculates the difference between the count of 'I's and the count of non-'I's in the string `S`. If the result is negative, it sets the result to 0. Finally, it prints the resulting value. The function does not have any explicit return value, and it operates based on the input parameters `N` and `S`.

