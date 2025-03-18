#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each of the t test cases, n is an integer such that 1 ≤ n ≤ 50.
def func():
    os.system('cls')
    s = string.ascii_uppercase
    t = int(input())
    for i in range(t):
        n = int(input())
        
        if n == 1:
            print('NO')
        else:
            ans = ''
            x = 0
            if n % 2 == 0:
                for j in range(n // 2):
                    ans += s[x] * 2
                    x += 1
            else:
                ans, x = 'AAA', 1
                for j in range(n // 2 - 1):
                    ans += s[x] * 2
                    x += 1
            print('YES')
            print(ans)
        
    #State: i is equal to t, s is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', ans is the string constructed based on the last input n, and x is the index of the last character used in constructing ans.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`. For each test case, it determines if it's possible to construct a string of length `n` using pairs of distinct uppercase letters. If `n` is 1, it outputs 'NO'. Otherwise, it constructs and outputs a string of length `n` using pairs of distinct uppercase letters, starting from 'AA', 'BB', etc., and outputs 'YES' followed by the constructed string.

