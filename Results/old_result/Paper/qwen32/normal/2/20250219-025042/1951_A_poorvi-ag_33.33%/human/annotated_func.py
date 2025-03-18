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
        
    #State: `start` and `end` are non-negative integers such that `start` <= `end`; `t` is an input integer; `results` is a list containing `'yes'` and/or `'no'` based on the conditions evaluated during each of the `t` iterations.
    for r in results:
        print(r)
        
    #State: `start` and `end` are non-negative integers such that `start` <= `end`; `t` is an input integer; `results` is a list containing all its elements, and each element has been printed.
    #
    #Output State:
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, then for each test case, it reads another integer `n` and a string `arr`. It checks the conditions on the string `arr` to determine if it should append 'yes' or 'no' to the `results` list. Finally, it prints each element in the `results` list.

