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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer within the range of 1 to 100, `result` is equal to `2 * count_I - N`, where `count_I` is the number of 'I's in string `S`.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer within the range of 1 to 100, `count_I` is the number of 'I's in string `S`, and if `result` is less than 0, then `result` is set to 0.
    print(result)
#Overall this is what the function does:The function accepts a positive integer `N` (where 1 ≤ N ≤ 100) and a string `S` of length `N` consisting only of the characters 'I' and 'D'. It calculates the result based on the counts of 'I' and 'D' in the string, where each 'I' increments the result by 1 and each 'D' decrements it by 1. Finally, if the result is negative, it sets the result to 0 before printing it. The function does not return any value, but prints the final result.

