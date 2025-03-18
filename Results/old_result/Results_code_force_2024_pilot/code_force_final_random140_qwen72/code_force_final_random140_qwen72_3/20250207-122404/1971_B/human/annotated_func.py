#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    cnt_test_cases = int(input())
    for i in range(cnt_test_cases):
        string = input().strip()
        
        if len(string) == 1:
            print('No')
        
        m = string[0]
        
        k = 0
        
        for i in range(len(string)):
            if string[i] == m:
                k += 1
        
        if k == len(string):
            print('No')
        else:
            print('Yes')
            print(''.join(sorted(string)))
        
    #State: `t` is an integer such that 1 <= t <= 1000, `s` is a string of length at most 10 consisting of lowercase English letters, `cnt_test_cases` is the total number of test cases processed, `i` is the final value of the loop counter which is equal to `cnt_test_cases`, `string` is the last input string stripped of leading and trailing whitespace, `m` is the first character of the last `string`, and `k` is the number of times the first character `m` appears in the last `string`. If `k` equals the length of the last `string`, all characters in the last `string` are the same as the first character `m`. Otherwise, `k` is not equal to the length of the last `string`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where `1 <= t <= 1000`. For each test case, it reads a string `s` of length at most 10 consisting of lowercase English letters. It then checks if the string contains only one unique character. If so, it prints 'No'. If the string contains more than one unique character, it prints 'Yes' followed by the sorted version of the string. After processing all test cases, the function has no return value, but it has printed the results for each test case. The final state of the program includes the processed number of test cases and the printed results for each test case.

