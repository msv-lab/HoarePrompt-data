#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n consisting only of "U" and "D" representing the initial state of the coins.
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
        
    #State: After all iterations of the loop, `t` is equal to the total number of inputs provided, `i` is equal to `t-1`, `n` is the last input integer received, `arr` is the last string input by the user, and the `results` list contains 'yes' or 'no' for each input based on whether the count of 'U' in `arr` is odd or even, respectively.
    for i in results:
        print(i)
        
    #State: Output State: `results` is a non-empty list, `i` is the third element in the `results` list, `t` is the length of `results`, `n` is the last integer in `results`, and `arr` is the last string input by the user.
    #
    #This means that after all iterations of the loop have finished, `i` will be set to the last element in the `results` list, `t` will be equal to the total number of elements in `results` (which is the length of the list), `n` will be the last integer in the `results` list, and `arr` will be the last string input by the user.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t`, another positive integer `n`, and a string `s` of length `n` made up of "U" and "D". For each test case, it checks if the count of "U" in the string `s` is odd. If the count is odd, it appends 'yes' to the results list; otherwise, it appends 'no'. After processing all test cases, it prints each result in the list. The final state of the program is that it has printed the results for all test cases, and the `results` list contains 'yes' or 'no' for each test case based on the count of "U" in the corresponding string `s`.

