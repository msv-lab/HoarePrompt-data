#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and S is a string of length N containing only the characters 'I' and 'D'.
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer within the range 1 to 100, `result` is equal to the difference between the count of 'I's and 'D's in `S`.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer within the range 1 to 100. If `result` is less than 0, then `result` is set to 0. Otherwise, `result` retains its value.
    print(result)
#Overall this is what the function does:The function accepts a positive integer N (1 ≤ N ≤ 100) and a string S of length N consisting of the characters 'I' and 'D'. It counts the occurrences of 'I' and 'D', calculating the difference between them. If the difference (result) is negative, it is set to 0 before being printed. Therefore, the function outputs the count of 'I's minus the count of 'D's, ensuring the output is never less than 0.

