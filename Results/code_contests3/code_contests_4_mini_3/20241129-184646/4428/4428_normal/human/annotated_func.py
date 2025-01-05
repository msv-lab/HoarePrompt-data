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
        
    #State of the program after the  for loop has been executed: `result` is equal to the difference between the number of 'I' characters and the number of 'D' characters in string `S`; `N` is a positive integer between 1 and 100; `S` is a string of length `N` consisting only of the characters 'I' and 'D'.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`result` is equal to the difference between the number of 'I' characters and the number of 'D' characters in string `S`; if `result` is less than 0, then `result` is 0, `N` is a positive integer between 1 and 100, and `S` is a string of length `N` consisting only of the characters 'I' and 'D'.
    print(result)
#Overall this is what the function does:The function accepts a positive integer `N` (where 1 ≤ N ≤ 100) and a string `S` of length `N` consisting only of the characters 'I' and 'D'. It calculates the difference between the count of 'I' characters and 'D' characters in `S`. If the result is negative, it sets the result to 0 before printing it. The function does not return a value, but it outputs the final result.

