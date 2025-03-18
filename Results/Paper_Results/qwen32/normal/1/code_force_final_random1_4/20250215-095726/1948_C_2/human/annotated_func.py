#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an even integer such that 2 ≤ n ≤ 2 \cdot 10^5, and the sum of n over all test cases does not exceed 2 \cdot 10^5. Each of the two strings representing the rows of the grid consists of exactly n characters, where each character is either '<' or '>'.
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
        
    #State: All test cases result in "Yes" being printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two strings of equal even length containing only '<' and '>'. It checks if it's possible to pair each '<' in the first string with a '>' in the second string such that each pair is aligned vertically and no two pairs overlap. For each test case, it outputs "YES" if such pairing is possible, otherwise "NO".

