#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string such that 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut0 = 0
        
        cut1 = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut1 += 1
            if a[i] == '0' and a[i + 1] == '1':
                cut0 += 1
        
        if cut0 == 0:
            print(cut1 + 1)
        else:
            print(cut0 + cut1)
        
    #State: Output State: The value printed by the program based on the input string `a` for each iteration, where `cut0` is the count of "01" substrings and `cut1` is the count of "10" substrings. If there are no "01" substrings, the output is `cut1 + 1`. Otherwise, the output is `cut0 + cut1`.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads an integer `t` and a binary string `s`. It counts the occurrences of "01" and "10" substrings within `s`. If there are no "01" substrings, it prints the count of "10" substrings plus one. Otherwise, it prints the sum of the counts of "01" and "10" substrings. The function does not return any value but prints the result for each test case.

