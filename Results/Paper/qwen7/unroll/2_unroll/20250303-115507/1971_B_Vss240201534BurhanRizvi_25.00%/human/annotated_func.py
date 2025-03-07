#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: For each test case, either 'Yes' followed by a randomly shuffled version of the input string or 'No' is printed. The exact output depends on the input string for each test case.
#Overall this is what the function does:For each test case defined by the input integer `t`, the function reads a string `s` of lowercase English letters and checks if `s` can be shuffled to form a different string. If a different shuffled version exists, it prints 'Yes' followed by the shuffled string; otherwise, it prints 'No'. The function processes up to 1000 test cases.

