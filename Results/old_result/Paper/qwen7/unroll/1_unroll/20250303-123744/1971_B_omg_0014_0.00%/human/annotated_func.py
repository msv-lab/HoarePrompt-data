#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 2:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 1000, n is an input integer, each iteration of the loop checks if the input string has a set length of 2 characters. If true, it prints 'NO'. Otherwise, it prints 'YES' and then checks if the sorted string (in ascending order) is equal to the original string. If true, it prints the sorted string in descending order; otherwise, it prints the sorted string in ascending order. This process repeats for n iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` and a string `s`. For each test case, it checks if the unique characters in `s` form exactly two distinct characters. If so, it prints 'NO'. Otherwise, it prints 'YES' and then either the lexicographically sorted version of `s` in descending order or the ascending order, depending on which matches the original string `s`. After processing all test cases, the function does not return any value.

