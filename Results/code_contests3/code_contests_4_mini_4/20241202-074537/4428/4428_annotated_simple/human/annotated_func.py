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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100; `S` is a string of length `N` consisting only of 'I' and 'D'. `result` is equal to the number of 'I' characters in `S` minus the number of 'D' characters in `S`.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 100; `S` is a string of length `N` consisting only of 'I' and 'D'. If the number of 'I' characters in `S` minus the number of 'D' characters in `S` is less than 0, then `result` is set to 0. Otherwise, `result` remains unchanged.
    print(result)
#Overall this is what the function does:The function accepts a positive integer `N` (where 1 ≤ N ≤ 100) and a string `S` of length `N` consisting only of the characters 'I' and 'D'. It counts the number of 'I' characters (adding 1 for each) and the number of 'D' characters (subtracting 1 for each) in `S`. The final result is the count of 'I' minus the count of 'D', but if this result is negative, it is set to 0 before being printed. Therefore, the function effectively calculates the net count of 'I' over 'D' and ensures that the output is non-negative.

