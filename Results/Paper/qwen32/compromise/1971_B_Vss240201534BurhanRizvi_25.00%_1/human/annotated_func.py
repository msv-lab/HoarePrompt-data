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
        
    #State: A series of "Yes" or "No" printed `t` times, with "Yes" followed by a shuffled version of the input string `s` if `s` is not equal to its shuffled version.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string `s` of lowercase English letters. It then checks if the string `s` can be rearranged into a different permutation. If it can, the function prints "Yes" followed by one such permutation; otherwise, it prints "No". This process is repeated `t` times.

