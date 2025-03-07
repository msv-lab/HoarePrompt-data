#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: Output State: After the loop executes all iterations, `s` will be a string that has been processed according to the rules defined within the loop. Specifically, `s` will be transformed in such a way that it no longer contains all the same characters and does not consist of a single repeated character sequence. If the length of `s` was originally greater than 1 and did not have all characters the same, `s` will undergo a series of transformations where its characters are rearranged or shifted to ensure it meets the "Yes" condition criteria. If `s` initially had all the same characters or was a single character, it will remain unchanged or become an empty string due to the conditions in the loop.
    #
    #If the loop runs until `t` (the initial positive integer input) reaches zero, and given the transformations applied in each iteration, `s` will eventually meet the "Yes" condition or remain unchanged based on the initial input constraints. The final state of `s` will depend on the specific sequence of inputs provided during each iteration, but it will always be a valid string that satisfies the loop's criteria.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` and a string `s`. For each test case, it checks if the string `s` can be transformed into a new string `s2` that meets certain criteria. If `s` can be transformed, it prints 'Yes' followed by the transformed string `s2`; otherwise, it prints 'No'. The function ensures that after processing all test cases, each string `s` either meets the "Yes" condition or remains unchanged based on the initial input constraints.

