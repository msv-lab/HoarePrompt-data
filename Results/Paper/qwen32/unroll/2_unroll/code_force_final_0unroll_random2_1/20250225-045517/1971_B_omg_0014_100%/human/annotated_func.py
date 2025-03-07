#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 1:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `s` is the last input string, `a` is a set of unique characters from the last input string, `b` is the last input string sorted in ascending order, `c` is the last input string sorted in descending order.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string `s` of lowercase English letters. For each string, it checks if all characters are the same. If they are, it outputs 'NO'. Otherwise, it outputs 'YES' and then prints the string in sorted order, either ascending or descending, depending on whether the original string is already in ascending order.

