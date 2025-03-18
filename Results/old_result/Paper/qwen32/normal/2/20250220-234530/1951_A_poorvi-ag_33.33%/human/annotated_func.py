#State of the program right berfore the function call: start and end are integers such that start <= end.
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
        
    #State: `start` and `end` are integers such that `start <= end`; `t` is an integer representing the number of iterations; `i` is equal to `t` after the loop; `results` is a list of `t` elements, each being either `'yes'` or `'no'` based on the conditions evaluated during each iteration.
    for r in results:
        print(r)
        
    #State: `start` and `end` are integers such that `start <= end`; `t` is an integer representing the number of iterations; `i` is equal to `t` after the loop; `results` is a list of `t` elements, each being either `'yes'` or `'no'` based on the conditions evaluated during each iteration. All elements in `results` have been printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, then for each test case, it reads an integer `n` and a string `arr`. It checks if the string `arr` contains exactly two '1's and they are consecutive, or if the count of '1's in `arr` is even. Based on these conditions, it appends either 'yes' or 'no' to a list `results`. Finally, it prints each element in `results`.

