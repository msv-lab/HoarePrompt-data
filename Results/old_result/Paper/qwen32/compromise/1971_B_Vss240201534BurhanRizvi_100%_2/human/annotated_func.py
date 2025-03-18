#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, s is a string consisting of lowercase English letters with a length of at most 10.
def func():
    for _ in range(int(input())):
        s = input()
        
        if len(s) == 1:
            print('No')
        elif len(set(s)) == 1 and len(s) > 1:
            print('No')
        else:
            s2 = ''.join(random.sample(s, len(s)))
            if s == s2:
                s2 = s[1:] + s[0]
            print('Yes')
            print(s2)
        
    #State: - The initial state of `t` and the strings `s` for each test case remains unchanged as per the problem statement.
    #   - The output consists of "Yes" or "No" followed by the modified string `s2` for each test case where the output is "Yes".
    #   - The final output state will include all these printed lines for each test case.
    #
    #Given the nature of the loop and the operations performed, the output state can be described as:
    #
    #Output State:
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a string `s` of lowercase English letters with a length of at most 10. For each string, it checks if the string is of length 1 or if all characters in the string are the same. If either condition is true, it outputs "No". Otherwise, it outputs "Yes" followed by a modified version of the string `s`. The modification involves shuffling the string; if the shuffled string is the same as the original, it rotates the string by moving the first character to the end.

