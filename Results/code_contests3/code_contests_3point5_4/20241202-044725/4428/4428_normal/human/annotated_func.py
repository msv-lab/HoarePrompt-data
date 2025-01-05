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
        
    #State of the program after the  for loop has been executed: N is a positive integer, S is a string of length N containing only the characters 'I' and 'D'. The value of result will depend on the number of 'I's and 'D's in the string S. If there are more 'I's than 'D's, result will be the difference between the number of 'I's and 'D's. If there are more 'D's than 'I's, result will be the negative difference between the number of 'D's and 'I's. If the number of 'I's is equal to the number of 'D's, result will be 0.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *N is a positive integer, S is a string of length N containing only the characters 'I' and 'D'. If the difference between the number of 'D's and 'I's is greater than 0, then the function returns the negative difference between the number of 'D's and 'I's. If the difference is less than 0, then the function returns the difference between the number of 'I's and 'D's. If the difference is 0, the function returns 0.
    print(result)
#Overall this is what the function does:The function accepts user input for a positive integer N and a string S of length N containing only 'I' and 'D'. It then calculates the difference between the count of 'I's and 'D's in the string S. If the result is negative, it sets the result to 0. Finally, it prints the final result. The function essentially counts the occurrences of 'I' and 'D' in the string S and adjusts the result accordingly.

