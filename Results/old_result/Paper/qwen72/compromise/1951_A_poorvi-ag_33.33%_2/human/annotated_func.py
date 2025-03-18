#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end, and the current directory contains subfolders with names that can be converted to integers within the range [start, end], and each of these subfolders may contain .html files.
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
        
    #State: `results` is a list containing 'yes' or 'no' strings based on the input conditions for each iteration, and the length of `results` is equal to `t`. The values of `start`, `end`, and the current directory contents remain unchanged.
    for r in results:
        print(r)
        
    #State: The loop prints each element of the `results` list, one by one, in the order they appear in the list. The values of `start`, `end`, and the current directory contents remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from the user, then for each of the `t` iterations, it reads another integer `n` and a string `arr`. It checks if the string `arr` contains exactly two '1's and if '11' is a substring, appending 'no' to the `results` list. If the string `arr` contains an even number of '1's but does not contain '11' as a substring, it appends 'yes' to the `results` list. Otherwise, it appends 'no'. After processing all iterations, it prints each element in the `results` list. The function does not modify the values of `start`, `end`, or the current directory contents.

