#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with a length between 1 and 500, inclusive.
def func():
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut += 1
        
        print(cut + 1)
        
    #State: Output State: The loop will have executed `t` times. After all iterations, `cut` will hold the total number of occurrences where the character '1' is immediately followed by '0' in the string `a`. The variable `i` will be incremented until it is no longer less than `len(a) - 1`, which means `i` will be `len(a)` after the loop completes. The value of `t` will be `0` since it decreases by 1 for each iteration of the loop and starts at a value between 1 and 500. The string `a` remains unchanged throughout the loop.
    #
    #In simpler terms, after the loop has finished executing all its iterations, `cut` will contain the total count of times '1' is immediately followed by '0' in the string `a`, `i` will be equal to the length of `a`, and `t` will be `0`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t` and a binary string `s`. It counts the number of times the character '1' is immediately followed by '0' in the string `s` for each test case. After processing all test cases, it prints the count for each case and sets the value of `t` to 0. The function does not return any value but prints the results for each test case.

