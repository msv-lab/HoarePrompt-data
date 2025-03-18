#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with a length between 1 and 500, inclusive.
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
        
    #State: Output State: After the loop executes all the iterations, `t` remains a positive integer such that \(1 \leq t \leq 500\), `q` equals `t - 1`, `count` is the total number of changes in consecutive characters in the string `s` for each iteration, `s` is the input string for each iteration, `flag` is 1 if there was at least one instance where `int(s[i]) < int(s[i + 1])` during any iteration, and `i` equals `len(s) - 2` for the final iteration. The `print` statement will output `count + 1` if `flag` is 0, otherwise it will output `count`. This means for each input string `s`, the loop will process it, and based on the conditions inside the loop, it will print either `count + 1` or `count`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a binary string `s`. For each test case, it counts the number of changes in consecutive characters in the string `s`. If there is no instance where a character is less than its next character, it prints the count plus one; otherwise, it prints the count. The function does not return any value but prints the result for each test case.

