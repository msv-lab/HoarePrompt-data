#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: t is the number of test cases, and for each test case, the output is the number of positions where the digit is greater than the next digit in the string representation of the input, plus one.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a binary string and counts the number of positions where a digit is greater than the next digit. It then prints the count plus one for each test case.

