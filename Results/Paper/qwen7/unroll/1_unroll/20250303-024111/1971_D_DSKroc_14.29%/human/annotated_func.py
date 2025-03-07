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
        
    #State: Output State: t is an integer between 1 and 500 inclusive, and for each input string s, the output is the number of positions where the digit is greater than the next digit plus one.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and a binary string `s`. For each test case, it counts the number of positions where a digit is greater than the next digit in the string `s`, then adds one to this count. Finally, it prints this adjusted count for each test case.

