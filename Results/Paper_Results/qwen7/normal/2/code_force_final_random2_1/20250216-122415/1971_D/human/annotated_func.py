#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with 1 ≤ |s| ≤ 500.
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
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: Output State: `t` must be greater than 2, `i` is equal to `t`, `s` is the last input string provided, `count` is a non-negative integer reflecting the total number of transitions from '0' to '1' found in the string `s`, `flag` is True, `j` is equal to `len(s) - 1`.
    #
    #This means that after all iterations of the loop have finished, the variable `t` will be set to the final value it had during the last iteration (which would be the total number of inputs processed), `i` will match `t` as it has completed all its iterations, `s` will hold the last string input, `count` will reflect the total count of transitions from '0' to '1' across all strings processed, `flag` will be True indicating that at least one transition from '0' to '1' was found in the strings, and `j` will be equal to the length of the last string minus one, as the loop condition `j < len(s) - 1` ensures `j` reaches the last index of the string before exiting the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a binary string `s`. For each test case, it counts the number of transitions from '0' to '1' in the string `s`. If at least one such transition is found, it subtracts one from the count. The function prints the final count for each test case and does not return any value.

