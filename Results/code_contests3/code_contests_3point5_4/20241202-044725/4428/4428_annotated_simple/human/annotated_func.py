#State of the program right berfore the function call: N is a positive integer and S is a string of length N consisting of only characters 'I' and 'D'.**
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: N is a positive integer, S is a string of length N consisting of only characters 'I' and 'D'. If there are more 'I's than 'D's in the string S, the result will be the difference between the count of 'I's and 'D's. If there are more 'D's than 'I's, the result will be the negative difference between the count of 'D's and 'I's. If the count of 'I's and 'D's is equal, the result will be 0.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *N is a positive integer, S is a string of length N consisting of only characters 'I' and 'D'. If there are more 'I's than 'D's in the string S, the result will be the difference between the count of 'I's and 'D's. If there are more 'D's than 'I's, the result will be the negative difference between the count of 'D's and 'I's. If the count of 'I's and 'D's is equal, the result will be 0. After the execution of the if-else block, if the result is less than 0, the result is set to 0.
    print(result)
#Overall this is what the function does:The function `func` reads a positive integer `N` and a string `S` of length `N` consisting only of characters 'I' and 'D'. It then iterates through the string, incrementing the result by 1 for each 'I' and decrementing it by 1 for each 'D'. If the final result is negative, it is set to 0. The function prints the final result. However, the functionality lacks a clear description of the purpose of calculating the result, so it's challenging to provide a detailed summary without additional context or task information.

