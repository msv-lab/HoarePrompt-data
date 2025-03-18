#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: Output State: The loop has executed all its iterations. Postcondition: `i` is equal to `n`, `n` remains greater than or equal to 1 (since it starts as a positive integer and is decremented by 1 in each iteration), `t` remains an integer such that 1 ≤ t ≤ 1000 and is unchanged throughout the loop executions, `s` is the last input string received, `a` is a set containing the unique characters from the last input string `s`. If the set `a` contains exactly 2 unique characters, no additional changes are made. Otherwise, `b` is a sorted string of the unique characters in `a`, and `c` is a string containing these sorted unique characters in reverse order.
    #
    #This means that after the loop completes, the variable `i` will be equal to `n`, indicating that all iterations of the loop have been executed. The value of `t` will still be within the range 1 to 1000, as it was not modified by the loop. The variable `n` will be 0 or negative (depending on how many inputs were provided) since it is decremented by 1 in each iteration until it reaches 0. The variable `s` will hold the last input string processed, and `a` will contain the unique characters from this string. Depending on the condition of the set `a`, either `b` or `c` will be printed, representing the sorted and reverse-sorted versions of the unique characters, respectively.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of an integer `t` and a string `s`. For each test case, it checks if the string `s` contains exactly two unique characters. If so, it prints 'NO'. Otherwise, it prints 'YES' and then prints either the lexicographically sorted version or the reverse-sorted version of the unique characters in `s`. The function does not return any value but outputs the results directly.

