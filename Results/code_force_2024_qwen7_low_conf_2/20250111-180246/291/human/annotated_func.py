#State of the program right berfore the function call: n is an integer representing the number of test cases. Each test case consists of two integers n and k (1 \le n, k \le 2 \cdot 10^5), where n is the length of the array and k is the number of operations. The second line of each test case contains n integers a_1, a_2, \ldots, a_n (-10^9 \le a_i \le 10^9) representing the array itself. It is guaranteed that the sum of the values of n and k for all test cases does not exceed 2 \cdot 10^5. The output should be the maximum sum of the array after k operations modulo 10^9 + 7.
def func_1(n):
    s = str(n)
    res = -1
    for i in range(len(s)):
        if int(s[i]) < 5:
            res = i
            break
        
    #State of the program after the  for loop has been executed: `total` is -1, `s` is a non-empty string, and `res` is the smallest index `i` such that the integer value of `s[i]` is less than 5, or `res` remains -1 if no such index exists.
    return res
    #The program returns res, which is the smallest index i such that the integer value of s[i] is less than 5, or -1 if no such index exists
#Overall this is what the function does:The function `func_1` accepts a single integer `n`, which represents the number of test cases. For each test case, it processes a string `s` representing a number composed of digits. The function iterates over each digit in `s` and checks if the integer value of the digit at the current position is less than 5. If such a digit is found, the function records the index of this digit and breaks out of the loop. If no digit less than 5 is found, the function sets the result to -1. Finally, the function returns the recorded index or -1 if no such index exists. This process is repeated for each test case, but the function itself only processes one test case as specified by the input `n`. The function does not perform any operations on arrays or modify their sums; it only examines the digits of a single string representation of a number.

