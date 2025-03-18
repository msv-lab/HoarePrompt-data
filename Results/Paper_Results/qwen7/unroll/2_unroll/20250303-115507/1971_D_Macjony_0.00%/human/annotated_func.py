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
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: Output State: t is an integer between 1 and 500 (inclusive), s is a string consisting of '0's and '1's, and count is the number of consecutive identical characters in s with the exception that if there is a '01' sequence, it is not counted towards the final count, and flag is a boolean that was used to track the presence of a '01' sequence but is no longer relevant after the loop.
#Overall this is what the function does:The function processes an integer `t` and a binary string `s`. It counts the number of consecutive identical characters in `s`, excluding any '01' sequences. For each of the `t` test cases, it prints the count of such sequences.

