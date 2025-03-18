#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each of the t test cases, there is a string of length 5 consisting only of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: The loop has executed `t` times, where `t` is the initial integer input between 1 and 32. For each of the `t` test cases, the program has read a distinct string `s` of length 5 consisting only of the characters 'A' and 'B'. It has counted the occurrences of 'A' (stored in `ac`) and the occurrences of 'B' (stored in `bc`). After counting, it printed 'A' if `ac` is greater than `bc`, otherwise it printed 'B'. The variable `q` has been incremented from 0 to `t-1` during the loop execution. The values of `t` and the distinct strings `s` remain unchanged throughout the process.
#Overall this is what the function does:The function reads an integer `t` (where 1 ≤ `t` ≤ 32), representing the number of test cases. For each test case, it reads a distinct string of length 5 consisting only of the characters 'A' and 'B'. It then prints 'A' if the count of 'A' in the string is greater than the count of 'B', otherwise it prints 'B'.

