#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an even integer such that 2 ≤ n ≤ 2 \cdot 10^5, and the sum of n over all test cases does not exceed 2 \cdot 10^5. Each of the two strings representing the rows of the grid consists of exactly n characters, each of which is either '<' or '>'. There are no arrows pointing outside the grid.
def func():
    for i in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        if b[-2] != '>':
            print('NO')
        elif n == 1:
            print('YES')
        else:
            no_path = True
            for k in range(0, n, 2):
                if b[k] != '>':
                    no_path = False
            if not no_path:
                no_path = True
                for k in range(1, n - 1, 2):
                    print(k)
                    if a[k] != '>':
                        no_path = False
            if no_path:
                print('YES')
            else:
                print('NO')
        
    #State: a sequence of 'YES' or 'NO' for each test case based on the criteria described in the code.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks if it's possible to pair each '<' with a '>' in two strings of equal length, where the pairs are either non-overlapping within the same string or one character is in the first string and the paired character is in the second string. It outputs "YES" if such pairing is possible and "NO" otherwise.

