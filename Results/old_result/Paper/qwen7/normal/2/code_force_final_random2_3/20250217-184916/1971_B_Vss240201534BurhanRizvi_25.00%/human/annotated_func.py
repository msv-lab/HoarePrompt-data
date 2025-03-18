#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: Output State: The loop has executed all its iterations, meaning the input integer `n` (which was initially provided by `int(input())`) has been decremented to 0. For each iteration, `s` is the input string, and `s2` is a random permutation of `s`. If `s` is different from `s2`, 'Yes' is printed along with `s2`; otherwise, 'No' is printed. The final state includes the initial input integer `n` being 0, and for each of the input strings `s`, there is a corresponding random permutation `s2` printed as per the loop's execution.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` and a string `s`. For each test case, it generates a random permutation of the string `s` and checks if the original string `s` is different from the permutation. If they are different, it prints 'Yes' followed by the permutation; otherwise, it prints 'No'. After processing all test cases, the function concludes with no return value.

