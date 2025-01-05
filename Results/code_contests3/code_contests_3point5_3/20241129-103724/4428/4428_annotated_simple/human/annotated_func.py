#State of the program right berfore the function call: **N is a positive integer such that 1 <= N <= 100. S is a string of length N containing only the characters 'I' and 'D'.
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: N is a positive integer such that 1 <= N <= 100, S is a string of length N containing only the characters 'I' and 'D'. The value of result will depend on the count of 'I' and 'D' in the string S. If there are more 'I's than 'D's, result will be the difference between the count of 'I's and 'D's. If there are more 'D's than 'I's, result will be the negative difference between the count of 'D's and 'I's. If there are an equal number of 'I's and 'D's, result will be 0.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *N is a positive integer such that 1 <= N <= 100, S is a string of length N containing only the characters 'I' and 'D'. The value of result will depend on the count of 'I' and 'D' in the string S. If there are more 'I's than 'D's, result will be the difference between the count of 'I's and 'D's. If there are more 'D's than 'I's, result will be the negative difference between the count of 'D's and 'I's. If there are an equal number of 'I's and 'D's, result will be 0. Additionally, if result is negative, the function returns 0.
    print(result)
#Overall this is what the function does:Functionality: The function `func` reads a positive integer `N` and a string `S` of length `N` containing only 'I' and 'D' characters. It then iterates through the string, incrementing the result by 1 for each 'I' and decrementing by 1 for each 'D'. If the final result is negative, it is set to 0. The function prints the final result. The actual code does not generate an array of integers as stated in the annotations.

