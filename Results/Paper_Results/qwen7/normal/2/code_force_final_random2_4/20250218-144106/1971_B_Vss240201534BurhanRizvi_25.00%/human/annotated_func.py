#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: Output State: After the loop executes all the iterations, `s2` is a random permutation of the input string `s`. The condition `s != s2` is checked for each iteration, and if `s` is different from `s2`, 'Yes' is printed along with `s2`. If `s` is equal to `s2`, 'No' is printed. This process is repeated for all the inputs provided by the user, and for each input, `s2` will always be a random permutation of the corresponding `s`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and a string `s`. For each test case, it generates a random permutation of the string `s` and checks if the original string `s` is different from the permuted string `s2`. If they are different, it prints 'Yes' followed by the permuted string `s2`; otherwise, it prints 'No'. This process is repeated for all provided test cases.

