#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
def func():
    t = int(input().strip(' '))
    for i in range(t):
        s = input().strip(' ')
        
        a = set()
        
        for i in s:
            a.add(i)
        
        if len(a) > 1:
            print('YES')
            newstr = s[len(s) // 2:] + s[:len(s) // 2]
            isreverse = s[::-1]
            if newstr != s:
                print(s[len(s) // 2:] + s[:len(s) // 2])
            elif isreverse != s:
                print(isreverse)
            else:
                print(s[len(s) // 2:] + s[0:len(s) // 2])
        else:
            print('NO')
        
    #State: Output State: The output will consist of 'YES' or 'NO' for each string `s` provided, based on whether the string can be split into two halves such that one half is a rearrangement of the other. If such a rearrangement is possible, the program prints the rearranged string; otherwise, it prints 'NO'. The specific strings printed depend on the input provided during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a string `s`. For each test case, it checks if the string `s` can be split into two halves such that one half is a rearrangement of the other. If such a rearrangement is possible, it prints the rearranged string; otherwise, it prints 'NO'. The function does not return any value but prints the results for each test case.

