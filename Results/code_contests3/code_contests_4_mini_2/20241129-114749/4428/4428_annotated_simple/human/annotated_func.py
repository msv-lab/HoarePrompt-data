#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and S is a string of length N consisting only of the characters 'I' and 'D'.
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `result` is equal to the count of 'I' in `S` minus the count of 'D' in `S`, `N` is the input integer, `S` is the input string of length `N`.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`result` is equal to the count of 'I' in `S` minus the count of 'D' in `S`, `N` is the input integer, and `S` is the input string of length `N`. If `result` was less than 0, it is now set to 0.
    print(result)
#Overall this is what the function does:The function accepts a positive integer `N` (1 ≤ N ≤ 100) and a string `S` of length `N` containing only the characters 'I' and 'D'. It calculates the difference between the count of 'I' and the count of 'D' in `S`. If this difference is negative, it sets the result to 0 before printing it. Thus, the function effectively counts how many more 'I's than 'D's are in the string, ensuring the result is not negative.

