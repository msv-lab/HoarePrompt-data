#State of the program right berfore the function call: N is a positive integer and S is a string of length N containing only the characters 'I' and 'D'.**
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `result` is the difference between the number of 'I's and the number of non-'I's in the list `S`. `i` is `N-1`, `N` is a non-negative integer, and `S` is a list of characters.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`result` is the difference between the number of 'I's and the number of non-'I's in the list `S`. `i` is `N-1`, `N` is a non-negative integer, and `S` is a list of characters. If `result` is less than 0 after the if condition, all variables retain their initial state.
    print(result)
#Overall this is what the function does:The function `func` reads a positive integer `N` and a string `S` of length `N` containing only the characters 'I' and 'D'. It then calculates the difference between the count of 'I's and the count of non-'I's in the string `S`, and if this difference is negative, it sets the result to 0. Finally, it prints the resultant value. The function does not have an explicit return value or specified output, but it processes the input parameters according to the constraints.

