#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string such that 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        count = 1
        
        flag = False
        
        j = 0
        
        while j < len(s) - 1:
            if s[j] != s[j + 1]:
                count += 1
                if s[j] == '0' and s[j + 1] == '1':
                    flag = True
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: Output State: `t` is greater than 0, `i` is equal to `t`, `s` is the last input string processed, `count` is the total number of times the condition `s[j] != s[j + 1]` was met across all strings, `flag` is True if any string had a segment where `s[j] == '0'` and `s[j + 1] == '1'`, and `j` is equal to `len(s) - 1`.
    #
    #This means that after all iterations of the loop have finished, `t` will still be greater than 0 (since it was initialized as such and not modified within the loop), `i` will be equal to `t` (as the loop runs from 0 to `t-1`), `s` will be the last string input, `count` will hold the cumulative count of transitions from '0' to '1' across all strings, `flag` will be True if any string contained such a transition, and `j` will be equal to the length of the last string minus one.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and a binary string `s`. For each test case, it counts the number of times the binary string transitions from '0' to '1'. If any string contains a transition from '0' to '1', it subtracts one from the count. Finally, it prints the adjusted count for each test case.

