#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: Output State: The output state will consist of multiple lines, where for each input string `s`:
    #
    #1. If `s` has a length of 1, it will print "No".
    #2. If `s` consists of the same character repeated (e.g., "aaa"), it will also print "No".
    #3. Otherwise, it will print "Yes" followed by a permutation of the characters in `s`.
    #
    #Since the exact inputs are not specified, we cannot provide a specific output state, but the general form of the output state can be described as above.
#Overall this is what the function does:The function processes up to 1000 test cases, where each test case includes a string `s` of lowercase English letters with a maximum length of 10. For each string `s`, it checks if the string has a length of 1 or consists of the same character repeated. If either condition is met, it prints "No". Otherwise, it generates a random permutation of the characters in `s` and prints "Yes" followed by this permutation.

