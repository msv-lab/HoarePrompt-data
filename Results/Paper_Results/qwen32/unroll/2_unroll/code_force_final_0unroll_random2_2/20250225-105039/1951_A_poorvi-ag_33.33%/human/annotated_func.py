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
        
    #State: `start` and `end` are integers such that `start <= end`; `t` is an input integer; `results` is a list of strings (`'yes'` or `'no'`) determined by the input strings in each iteration.
    for r in results:
        print(r)
        
    #State: start and end are integers such that start <= end; t is an input integer; results is a list of strings ('yes' or 'no') determined by the input strings in each iteration.
#Overall this is what the function does:The function reads an integer `t` from the input, then for each of the next `t` lines, it reads a string `arr` and determines if the string meets specific conditions related to the count of the character '1'. It prints 'yes' if the count of '1' is even and not equal to 2 with '11' as a substring, otherwise it prints 'no'. The function does not accept `start` and `end` as parameters and does not return any value; it only prints the results.

