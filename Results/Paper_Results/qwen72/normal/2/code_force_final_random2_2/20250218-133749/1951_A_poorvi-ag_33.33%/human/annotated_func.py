#State of the program right berfore the function call: start and end are integers where start <= end, and they represent the range of folder names to be processed. The current working directory contains subfolders named with digits within the specified range, and each of these subfolders may contain .html files.
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
        
    #State: `start` and `end` are integers where `start <= end`, the current working directory contains subfolders named with digits within the specified range, each of these subfolders may contain .html files, `t` remains the same, `i` is `t-1`, `n` is an input integer, `arr` is an input string. The list `results` will contain `t` elements, where each element is either 'yes' or 'no' based on the conditions evaluated during each iteration of the loop. Specifically, if `arr` contains exactly two '1's and the substring '11', the corresponding element in `results` is 'no'. If `arr` contains an even number of '1's but does not meet the exact two '1's and '11' condition, the corresponding element in `results` is 'yes'. If `arr` contains an odd number of '1's, the corresponding element in `results` is 'no'.
    for r in results:
        print(r)
        
    #State: `start` and `end` are integers where `start <= end`, the current working directory contains subfolders named with digits within the specified range, each of these subfolders may contain .html files, `t` remains the same, `i` is `t-1`, `n` is an input integer, `arr` is an input string, `results` is a non-empty list containing `t` elements, where each element is either 'yes' or 'no' based on the conditions evaluated during each iteration of the loop, and all elements in `results` have been printed.
#Overall this is what the function does:The function reads a series of inputs and evaluates strings to determine if they meet certain criteria, appending 'yes' or 'no' to a results list accordingly. It then prints each element of the results list. The function does not modify the current working directory or any subfolders; it only processes input data and outputs the results.

