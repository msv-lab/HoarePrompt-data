#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string such that 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 500, and for each input string `s`, the output is the number of times a digit is greater than the next digit in `s` plus one.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` and `t` binary strings `s`. It then counts the number of positions in each string where a digit is greater than the next digit and prints the count plus one for each string. The function does not return any value but prints the results for each test case.

