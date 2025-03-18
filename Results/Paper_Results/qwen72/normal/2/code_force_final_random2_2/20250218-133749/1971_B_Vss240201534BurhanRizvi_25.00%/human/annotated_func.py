#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and s is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: After the loop executes all the iterations, `t` is an integer such that 1 <= t <= 1000, and for each iteration, `s` was a new input string (a string of length at most 10 consisting of lowercase English letters). The variable `_` ranges from 0 to `t-1`, and for each iteration, `s2` is a shuffled version of the corresponding `s`. For each iteration, if `s` is not equal to `s2`, the condition `s != s2` held true, and "Yes" along with the shuffled string `s2` was printed. If `s` is equal to `s2`, the condition `s == s2` held true, and "No" was printed.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 <= t <= 1000. For each test case, it reads a string `s` of up to 10 lowercase English letters. It then generates a random shuffle `s2` of the string `s`. If `s2` is different from `s`, it prints "Yes" followed by the shuffled string `s2`. If `s2` is the same as `s`, it prints "No". The function does not return any value; it only performs these operations and prints the results.

