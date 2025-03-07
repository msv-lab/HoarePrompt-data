#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: After executing all iterations, for each input string `s`, the program outputs "No" if `s` has a length of 1 or consists of identical characters (length > 1). Otherwise, it outputs "Yes" followed by a modified version of `s` (`s2`), which is either a shuffled version of `s` or `s` rotated by one position if the shuffle didn't change the order.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of a string `s`. For each string, it checks if the string has a length of 1 or consists of identical characters. If so, it outputs "No". Otherwise, it outputs "Yes" followed by a modified version of the string, which is either a shuffled version of the string or the string rotated by one position if the shuffle did not change the order.

