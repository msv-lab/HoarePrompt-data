#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: Output State: All test cases specified by `cnt_test_cases` have been processed, and for each input string, the program has determined whether it should print 'Yes' followed by the sorted version of the string or 'No'. The variable `total` remains unchanged from its initial value, `cnt_test_cases` remains unchanged, and `t` remains unchanged. For each input string, `i` is equal to the length of the string, `m` is the first character of the string, and `k` is the total count of occurrences of `m` in the string. If `k` is equal to the length of the string, the program prints 'No'; otherwise, it prints 'Yes' followed by the sorted version of the string.
    #
    #In simpler terms, after all iterations of the loop, the program has processed all test cases, printed 'Yes' followed by the sorted version of the string for those strings that do not consist entirely of the same character, and printed 'No' for those that do. The initial conditions and other variables outside the loop remain as they were initially.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` and a string `s`. It checks each string to determine if it consists entirely of the same character. If so, it prints 'No'. Otherwise, it prints 'Yes' followed by the sorted version of the string. After processing all test cases, it outputs the results without modifying any external variables.

