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
        
    #State: results is a list of 'yes' or 'no' based on the input conditions after t iterations.
    for r in results:
        print(r)
        
    #State: results is a list of 'yes' or 'no' based on the input conditions after t iterations. The values in results have been printed to the console.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `arr`. It then determines if the string `arr` meets specific conditions related to the number of '1's it contains and prints 'yes' or 'no' based on these conditions. The function does not accept parameters `start` and `end` as described in the annotations. Instead, it processes each test case independently and prints the result for each.

