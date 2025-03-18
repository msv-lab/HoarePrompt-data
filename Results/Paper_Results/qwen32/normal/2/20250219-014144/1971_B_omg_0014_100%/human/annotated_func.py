#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: The loop has processed all `n` test cases, printing "NO" if all characters in the string are the same, or "YES" followed by the sorted string in either ascending or descending order based on the original order of the string. The variables `t` and `n` remain unchanged, and the loop variable `i` is equal to `n`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a string of lowercase English letters. For each string, it checks if all characters are identical. If they are, it outputs "NO". Otherwise, it outputs "YES" followed by the string sorted in ascending order if the original string is not already sorted, or in descending order if the original string is sorted in ascending order.

