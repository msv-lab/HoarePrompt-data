#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 100, and s is a string of length n consisting only of the characters "U" and "D".
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
        
    #State: `results` is a list containing `t` elements, where each element is either 'yes' or 'no' depending on whether the count of 'U' in the respective string `s` is odd. All other variables remain unchanged.
    for i in results:
        print(i)
        
    #State: results is a list containing t elements, where each element is either 'yes' or 'no' depending on whether the count of 'U' in the respective string s is odd. The loop has printed each element of the results list to the console. All other variables remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting of "U" and "D". It then determines if the count of "U" in `s` is odd and appends 'yes' to the results if true, otherwise 'no'. Finally, it prints 'yes' or 'no' for each test case based on the count of "U".

