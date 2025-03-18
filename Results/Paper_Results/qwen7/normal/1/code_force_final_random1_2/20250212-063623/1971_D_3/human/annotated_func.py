#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with 1 ≤ |s| ≤ 500.
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
        
    #State: Output State: After the loop executes all iterations, `j` is equal to the length of the string `s`, `count` is the total number of transitions from '0' to '1' or from '1' to '0' in the string `s` minus one, `flag` is True if there was at least one transition from '0' to '1' during the loop's execution, otherwise `flag` is False, and `i` is equal to `t - 1`.
    #
    #This means that after the loop has completed all its iterations (from 0 to `t-1`), the variable `i` will be `t - 1`. The variable `j` will be equal to the length of the string `s` because the while loop increments `j` until it reaches the end of the string. The variable `count` will be the total number of transitions between different characters in the string `s`, adjusted by subtracting one if a '0' is followed by a '1' at any point. Finally, `flag` will be True if there was at least one instance where a '0' was immediately followed by a '1' in the string `s`, and False otherwise.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and a binary string `s`. For each test case, it counts the total number of transitions between different characters in the string `s`, adjusting the count by subtracting one if a '0' is immediately followed by a '1'. It also checks if there was at least one instance where a '0' was immediately followed by a '1'. The function prints the adjusted count for each test case and does not return any value.

