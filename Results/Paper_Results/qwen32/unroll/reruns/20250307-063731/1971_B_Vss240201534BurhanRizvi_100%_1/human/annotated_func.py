#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        if len(s) == 1:
            print('No')
        elif len(set(s)) == 1 and len(s) > 1:
            print('No')
        else:
            s2 = ''.join(random.sample(s, len(s)))
            if s == s2:
                s2 = s[1:] + s[0]
            print('Yes')
            print(s2)
        
    #State: For each test case, either "No" if the string length is 1 or all characters are the same, or "Yes" followed by a modified version of the string `s` which is a random permutation or a rotated version of the string if the random permutation matches the original string.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a string `s`. For each string, it checks if the string length is 1 or if all characters in the string are the same. If either condition is true, it outputs "No". Otherwise, it outputs "Yes" followed by a modified version of the string `s`, which is either a random permutation of the string or a rotated version of the string if the random permutation matches the original string.

