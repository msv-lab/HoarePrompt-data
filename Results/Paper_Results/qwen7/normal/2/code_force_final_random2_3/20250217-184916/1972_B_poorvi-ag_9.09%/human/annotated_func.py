#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D" representing the initial state of the coins.
def func():
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if n % 2 == 0:
            results.append('no')
        elif arr.count('U') > arr.count('D'):
            results.append('yes')
        else:
            results.append('no')
        
    #State: Postcondition: `t` is an integer between 1 and 100, `results` is a list containing 'yes' and 'no' for each iteration of the loop, `i` is `t`, `n` is the integer input by the user for each iteration, and `arr` is the string input by the user for each iteration. If `n` is even, 'no' is appended to the `results` list. Otherwise, if the count of 'U' in `arr` is greater than the count of 'D', 'yes' is appended; otherwise, 'no' is appended.
    for i in results:
        print(i)
        
    #State: All elements in the `results` list are either 'yes' or 'no'. The loop has executed as many times as there are elements in the `results` list.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t` (1 ≤ t ≤ 100), a positive integer `n` (1 ≤ n ≤ 100), and a string `s` of length `n` containing only "U" and "D". For each test case, it checks if the number of "U" characters in the string `s` is greater than the number of "D" characters when `n` is odd. If true, it appends "yes" to the results list; otherwise, it appends "no". If `n` is even, it always appends "no". Finally, it prints each element in the results list.

