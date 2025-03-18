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
        
    #State: Output State: The value of `t` remains unchanged, and for each iteration of the loop with input string `s`, if the length of the set `a` is 1 (meaning all characters in `s` are the same), it prints 'NO'. Otherwise, it prints 'YES', sorts the string `s` in both ascending and descending order, and prints the sorted string based on the original string's order.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and then `n` strings `s`. If all characters in any string `s` are the same, it prints 'NO'. Otherwise, it prints 'YES' and then prints the lexicographically smallest and largest permutations of `s` based on the original string's order. The function does not return any value but prints the results for each test case.

