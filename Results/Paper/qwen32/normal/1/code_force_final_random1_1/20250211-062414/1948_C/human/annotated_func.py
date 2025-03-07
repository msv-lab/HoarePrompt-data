#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an even integer such that 2 ≤ n ≤ 2 · 10^5, and the sum of n over all test cases does not exceed 2 · 10^5. Each of the two strings representing the rows of the grid consists of exactly n characters, where each character is either '<' or '>'.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: The loop will print "Yes" for each of the t test cases.
#Overall this is what the function does:The function processes `t` test cases, each consisting of an even integer `n` and two strings of length `n` containing only '<' and '>'. It checks if it is possible to pair each '<' in the first string with a '>' in the second string such that each pair is vertically aligned and no two pairs overlap. For each test case, it prints "YES" if such pairing is possible, otherwise it prints "NO".

