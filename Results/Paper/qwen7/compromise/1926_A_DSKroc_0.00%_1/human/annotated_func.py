#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of letters 'A' and 'B'.
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
        
    #State: Output State: `t` is an integer between 1 and 32, `q` is `t-1`, `ac` is the total count of 'A' characters in the original string `s`, `bc` is the total count of non-'A' characters in the original string `s`, `s` is an empty string, and `i` is no longer applicable since `s` is now empty.
    #
    #In natural language: After the loop has executed all its iterations, the variable `t` remains within the range of 1 to 32, `q` is set to `t-1`, `ac` contains the total number of 'A' characters found in the original string `s`, `bc` contains the total number of non-'A' characters found in the original string `s`, the string `s` has been fully processed and is now an empty string, and the variable `i` is no longer defined as it refers to the last character of `s`, which is now non-existent.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: `t` is an integer between 1 and 32, `q` is set to `t-1`, `ac` contains the total number of 'A' characters found in the original string `s`, `bc` contains the total number of non-'A' characters found in the original string `s`, the string `s` is now an empty string, and `ac` is either greater than `bc` or less than or equal to `bc` depending on the condition of the if statement.
#Overall this is what the function does:The function processes up to 32 test cases, where each test case involves an input string of length 5 consisting of 'A' and 'B'. For each test case, it counts the number of 'A' characters (`ac`) and the number of non-'A' characters (`bc`). After processing all test cases, it prints 'A' if the count of 'A' characters is greater than the count of non-'A' characters, otherwise it prints 'B'. The function does not return any value but outputs 'A' or 'B' based on the comparison of counts.

