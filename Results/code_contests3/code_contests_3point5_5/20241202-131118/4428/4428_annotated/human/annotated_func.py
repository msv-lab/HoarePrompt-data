#State of the program right berfore the function call: N is a positive integer between 1 and 100, S is a string of length N containing only 'I' and 'D'.
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: N is a positive integer between 1 and 100, S is a string of length N containing only 'I' and 'D'. If there are more 'I's than 'D's in the string S, result is the difference between the count of 'I's and 'D's. If there are more 'D's than 'I's in the string S, result is the negative difference between the count of 'I's and 'D's. If there are an equal number of 'I's and 'D's, result is 0.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *N is a positive integer between 1 and 100, S is a string of length N containing only 'I' and 'D'. If there are more 'I's than 'D's, the result is the difference between the count of 'I's and 'D's. If there are more 'D's than 'I's, the result is the negative difference between the count of 'I's and 'D's. If there are an equal number of 'I's and 'D's, the result is 0. If the result is less than 0, the function does not have an else part.
    print(result)
#Overall this is what the function does:The function `func` reads an integer `N` and a string `S` of length `N` containing only 'I' and 'D'. It then calculates the difference between the count of 'I's and 'D's in the string. If there are more 'I's than 'D's, it returns the positive difference. If there are more 'D's than 'I's, it returns the negative difference. If the counts are equal, it returns 0. If the calculated result is negative, it sets the result to 0. The function does not accept any parameters and prints the final result.

