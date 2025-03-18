#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with a length between 1 and 500.
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
        
    #State: Output State: The loop has executed all its iterations, meaning `i` equals `t`. At this point, `t` must be greater than 4, `s` is the last input string provided with a length of at least 4, `flag` is True, `j` is equal to the length of `s`, and `count` is 2.
    #
    #This final state indicates that the loop has processed all `t` inputs, with each input string `s` having a length of at least 4 characters, and the condition for `flag` being True was met in all cases. The `count` value has been adjusted based on the logic within the loop, resulting in a final count of 2.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `t` and a binary string `s`. For each test case, it counts the number of transitions from '0' to '1' in the string `s`. If any transition from '0' to '1' is found, it subtracts one from the count. Finally, it prints the adjusted count for each test case.

