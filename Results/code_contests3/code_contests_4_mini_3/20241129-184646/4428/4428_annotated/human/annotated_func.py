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
        
    #State of the program after the  for loop has been executed: `result` is equal to the count of 'I' characters in `S` minus the count of 'D' characters in `S`, `N` is a positive integer between 1 and 100, `S` is a string of length `N` consisting only of the characters 'I' and 'D'.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`result` is equal to the count of 'I' characters in `S` minus the count of 'D' characters in `S`, `N` is a positive integer between 1 and 100, and `S` is a string of length `N` consisting only of the characters 'I' and 'D'. If `result` was less than 0, then `result` is 0.
    print(result)
#Overall this is what the function does:The function accepts an integer `N` and a string `S` of length `N` consisting of 'I' and 'D', calculates the difference between the count of 'I's and 'D's, and prints the result, ensuring it is non-negative.

