#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D".
def func():
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('U') % 2 == 1:
            results.append('yes')
        else:
            results.append('no')
        
    #State: Output State: `t` integers are appended to the `results` list. For each iteration, if the count of 'U' in the input string `arr` is odd, 'yes' is appended; otherwise, 'no' is appended.
    for i in results:
        print(i)
        
    #State: Output State: The `results` list contains `t` elements, where each element is either 'yes' or 'no' based on whether the count of 'U' in the input string `arr` is odd or even, respectively.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting of "U" and "D". It checks if the count of "U" in the string `s` is odd. If the count is odd, it appends 'yes' to the results list; otherwise, it appends 'no'. Finally, it prints each element in the results list, which contains 'yes' or 'no' based on the odd/even count of "U" in each input string.

