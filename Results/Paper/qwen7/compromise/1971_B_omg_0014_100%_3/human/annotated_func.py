#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: The output state will consist of 'YES' or 'NO' printed for each iteration based on whether the string `s` contains more than one unique character. If 'YES' is printed, the sorted version of `s` (in ascending order) or its reverse (in descending order) will also be printed, depending on which is equal to the original string `s`.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer `t` and a string `s`. For each test case, it checks if the string `s` contains more than one unique character. If `s` has only one unique character, it prints 'NO'. Otherwise, it prints 'YES' followed by either the sorted version of `s` in ascending order or its reverse in descending order, depending on which matches the original string `s`.

