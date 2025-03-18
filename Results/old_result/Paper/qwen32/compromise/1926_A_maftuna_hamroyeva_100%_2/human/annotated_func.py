#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each of the t test cases, there is a string of length 5 consisting only of the characters 'A' and 'B'. All t strings are distinct.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        l = 0
        
        h = 0
        
        for j in a:
            if j == 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        else:
            print('B')
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each test case, the program reads a string of length 5 consisting of 'A' and 'B', counts the occurrences of 'A' (`l`) and other characters (`h`), and prints 'A' if `l` is greater than `h`, otherwise it prints 'B'. The variables `l` and `h` are reset for each iteration, and `i` ranges from 0 to `t-1`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, then for each test case, it reads a string of length 5 consisting of 'A' and 'B'. It counts the occurrences of 'A' and 'B' in each string and prints 'A' if 'A' appears more times, otherwise it prints 'B'.

