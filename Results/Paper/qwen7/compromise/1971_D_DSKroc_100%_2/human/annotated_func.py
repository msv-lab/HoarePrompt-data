#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        flag = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) != int(s[i + 1]):
                count += 1
            if int(s[i]) < int(s[i + 1]):
                flag = 1
        
        if flag == 0:
            print(count + 1)
        else:
            print(count)
        
    #State: The output state after the loop executes all iterations is as follows: `q` equals `t`, `i` equals `-1`, `count` is the total number of adjacent character pairs in `s` where the first character is not equal to the second character when both are converted to integers, and `flag` is 1 if there was at least one instance where `int(s[i]) < int(s[i + 1])` during the loop's execution; otherwise, `flag` is 0.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes a positive integer `t` and a binary string `s`. It counts the number of adjacent character pairs in `s` where the characters are not equal when converted to integers. If there is at least one instance where the current character is less than the next character in `s`, it subtracts one from the count before printing the result. Otherwise, it prints the count as is. The function implicitly takes input values for `t` and `s` for each test case and outputs the result for each case.

