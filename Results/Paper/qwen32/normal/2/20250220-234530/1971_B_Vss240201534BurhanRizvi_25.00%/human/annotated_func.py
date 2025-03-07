#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: The loop has processed all `t` test cases, printing "Yes" followed by a random permutation of the input string `s` if `s` is not equal to the permutation; otherwise, it prints "No". The value of `t` and any other variables not modified by the loop remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` of lowercase English letters and checks if there exists a permutation of `s` that is different from `s`. If such a permutation exists, it prints "Yes" followed by one such permutation; otherwise, it prints "No".

