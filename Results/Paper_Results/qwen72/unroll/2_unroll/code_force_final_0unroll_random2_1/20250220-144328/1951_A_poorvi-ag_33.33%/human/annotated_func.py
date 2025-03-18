#State of the program right berfore the function call: start and end are integers such that start <= end, and the current working directory contains subfolders with names that can be interpreted as integers within the range [start, end].
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
        
    #State: `start` and `end` remain unchanged, `t` remains unchanged, `results` is a list containing 'yes' or 'no' for each iteration based on the conditions evaluated in the loop.
    for r in results:
        print(r)
        
    #State: `start` and `end` remain unchanged, `t` remains unchanged, `results` is a list containing 'yes' or 'no' for each iteration based on the conditions evaluated in the loop. The loop prints each element of the `results` list, one by one.
#Overall this is what the function does:The function reads an integer `t` from the user, then for each of the `t` iterations, it reads an integer `n` and a string `arr` from the user. It evaluates the string `arr` and appends 'yes' to a list `results` if the number of '1's in `arr` is even and does not contain '11'. Otherwise, it appends 'no'. After processing all `t` inputs, it prints each element of the `results` list. The function does not modify the `start` and `end` variables, and it does not return any value.

