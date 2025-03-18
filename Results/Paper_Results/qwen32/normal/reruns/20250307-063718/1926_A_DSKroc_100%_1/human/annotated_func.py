#State of the program right berfore the function call: t is an integer such that 1 <= t <= 32, and for each of the t test cases, there is a string of length 5 consisting only of the characters 'A' and 'B'. All t strings are distinct.
def func():
    t = int(input())
    for q in range(t):
        ac = 0
        
        bc = 0
        
        s = input()
        
        for i in s:
            if i == 'A':
                ac += 1
            else:
                bc += 1
        
        if ac > bc:
            print('A')
        else:
            print('B')
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each of the `t` test cases, the string `s` of length 5 is processed to count the occurrences of 'A' (`ac`) and 'B' (`bc`). The program prints 'A' if `ac` is greater than `bc`, otherwise it prints 'B'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string of length 5 consisting of 'A' and 'B'. It then prints 'A' if there are more 'A's than 'B's in the string, otherwise it prints 'B'.

