#State of the program right berfore the function call: start and end are non-negative integers such that start <= end.
def func():
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('1') == 2 and '11' in arr:
            results.append('no')
        
        if arr.count('1') % 2 == 0:
            if arr.count('1') == 2 and '11' in arr:
                results.append('no')
            else:
                results.append('yes')
        else:
            results.append('no')
        
    #State: `start` and `end` are non-negative integers such that `start` <= `end`; `t` is the number of iterations; `results` is a list of length `t` containing `'yes'` or `'no'` based on the conditions evaluated during each iteration.
    for r in results:
        print(r)
        
    #State: `start` and `end` are non-negative integers such that `start` <= `end`, `t` is at least 1, `results` is a list of length `t` containing `'yes'` or `'no'`, and all elements in `results` have been printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads another integer `n` and a string `arr`. It then determines if the string `arr` meets specific conditions related to the count of '1's in the string and prints 'yes' or 'no' accordingly. The function does not accept `start` and `end` as parameters and does not return any value; instead, it prints the results directly.

