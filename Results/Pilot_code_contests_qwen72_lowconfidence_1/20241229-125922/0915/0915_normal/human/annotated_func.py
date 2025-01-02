#State of the program right berfore the function call: a1, a2, a3, a4 are integers where 0 ≤ a1, a2, a3, a4 ≤ 104, and s is a string of length 1 ≤ |s| ≤ 105, consisting of characters '1', '2', '3', and '4'.
def func_1():
    c = [0] * 5
    for i in range(1, 5):
        c[i] = int(input())
        
    #State of the program after the  for loop has been executed: `a1`, `a2`, `a3`, `a4` are integers where \(0 \leq a1, a2, a3, a4 \leq 10^4\), `s` is a string of length \(1 \leq |s| \leq 10^5\) consisting of characters '1', '2', '3', and '4', `c` is `[0, input_integer_1, input_integer_2, input_integer_3, input_integer_4]`, `i` is 4
    s = input()
    res = 0
    for ch in s:
        res += c[int(ch)]
        
    #State of the program after the  for loop has been executed: `a1`, `a2`, `a3`, `a4` are integers where \(0 \leq a1, a2, a3, a4 \leq 10^4\), `s` is a string consisting of characters '1', '2', '3', and '4', `c` is `[0, input_integer_1, input_integer_2, input_integer_3, input_integer_4]`, `i` is 4, `res` is the sum of the values in `c` indexed by the integer representation of each character in `s`. If `s` is empty, `res` remains 0.
    print(res)
    return
    #The program returns `res`, which is the sum of the values in `c` indexed by the integer representation of each character in `s`. If `s` is empty, `res` remains 0.
#Overall this is what the function does:The function `func_1` reads four integers from user input and stores them in a list `c` (with indices 1 to 4). It then reads a string `s` from user input, where `s` consists of characters '1', '2', '3', and '4'. The function calculates the sum of the values in `c` indexed by the integer representation of each character in `s` and prints this sum. The function does not return any value. If `s` is empty, the function prints 0. Note that the function does not accept any parameters; it only interacts with the user through standard input.

