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
        
    #State: results is a list of 'yes' or 'no' based on the input strings in each iteration.
    for r in results:
        print(r)
        
    #State: the list 'results' remains unchanged, and each element ('yes' or 'no') in the list is printed to the console.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `n` and a string `arr`. It then determines if the string `arr` contains an even number of '1's and does not consist solely of two consecutive '1's. If these conditions are met, it appends 'yes' to the results list; otherwise, it appends 'no'. After processing all test cases, it prints 'yes' or 'no' for each test case based on the results list.

