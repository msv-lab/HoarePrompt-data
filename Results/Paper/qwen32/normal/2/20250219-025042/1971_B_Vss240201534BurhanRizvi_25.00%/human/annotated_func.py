#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: t is 0, s is the last input string, and s2 is a permutation of the last input string.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a string `s` of lowercase English letters. For each string, it generates a random permutation `s2`. If `s2` is different from `s`, it prints 'Yes' followed by `s2`; otherwise, it prints 'No'. After processing all test cases, the function concludes without returning any value.

