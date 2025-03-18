#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: Output State: The loop will have executed `cnt_test_cases` times. For each input string, the variable `m` will be set to the first character of the string, `k` will be the count of how many times `m` appears in the string, and `i` will be the length of the string. If `k` equals the length of the string, the program will print 'No' and move on to the next test case. Otherwise, it will print 'Yes' followed by the sorted version of the string. After all iterations, the final output will consist of 'Yes' or 'No' for each test case, followed by the sorted string if applicable.
    #
    #In natural language: After all iterations of the loop, the output will consist of 'Yes' or 'No' for each test case based on whether the entire string is composed of the same character. If 'Yes', the string will be printed in sorted order. The loop will have processed all `cnt_test_cases` inputs, and the final output will reflect the results of each case according to the conditions specified in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` (the number of test cases) and a string `s` (of length at most 10 consisting of lowercase English letters). For each test case, it checks if the string `s` contains more than one distinct character. If `s` consists of only one character repeated throughout, it prints 'No'. Otherwise, it prints 'Yes' followed by the sorted version of the string `s`. After processing all test cases, it outputs 'Yes' or 'No' for each case, and the sorted string if applicable.

