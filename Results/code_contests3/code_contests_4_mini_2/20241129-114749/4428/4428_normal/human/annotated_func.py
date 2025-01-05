#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, S is a string of length N consisting only of the characters 'I' and 'D'.
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100; `result` is the difference between the count of 'I's and the count of 'D's in the string `S`.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 100; if `result` is less than 0, then `result` is 0.
    print(result)
#Overall this is what the function does:The function accepts a positive integer `N` (between 1 and 100) and a string `S` of length `N` consisting only of the characters 'I' and 'D'. It calculates the difference between the count of 'I's and 'D's in the string, ensuring that the result is not negative. Finally, it prints the result, which represents the net count of 'I's after decrementing for each 'D'. If the calculated result is less than 0, it prints 0 instead.

