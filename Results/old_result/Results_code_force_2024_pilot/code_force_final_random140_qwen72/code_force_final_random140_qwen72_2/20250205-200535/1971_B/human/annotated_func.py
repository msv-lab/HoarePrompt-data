#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `s` is a string of length at most 10 consisting of lowercase English letters, `cnt_test_cases` has been fully decremented to 0, `i` is the final index of the last iteration (which is `cnt_test_cases - 1`), `string` is the last input string with leading and trailing whitespace removed, `m` is the first character of the last `string`, and `k` is the number of times the first character `m` appears in the last `string`. If `k` equals the length of the last `string`, all characters in the last `string` are the same as the first character `m`. Otherwise, `k` is not equal to the length of the last `string`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 <= t <= 1000. For each test case, it reads a string `s` of up to 10 lowercase English letters. It then checks if all characters in the string are the same. If they are, it prints 'No'. If not, it prints 'Yes' followed by the sorted version of the string. After processing all test cases, the function completes, and the state includes `t` being an integer within the specified range, `s` being the last processed string, and all test cases having been fully processed.

