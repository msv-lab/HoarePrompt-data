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
        
    #State: t is 0, indicating all test cases have been processed. Each input string s has been processed by generating a random permutation s2, and the appropriate output ("Yes" or "No") has been printed based on whether s is equal to s2.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string `s` of lowercase English letters. It then generates a random permutation of `s` and checks if the permuted string `s2` is different from the original string `s`. If they are different, it prints "Yes" followed by the permuted string; otherwise, it prints "No". This process is repeated for all `t` test cases.

