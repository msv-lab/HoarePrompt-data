#State of the program right berfore the function call: start and end are integers where start <= end, and they represent the range of folder names to be processed.
def func():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        
        arr = input()
        
        count_ones = arr.count('1')
        
        if count_ones == 0:
            results.append('yes')
        elif count_ones % 2 != 0:
            results.append('no')
        elif count_ones == 2:
            if '11' in arr:
                results.append('no')
            else:
                results.append('yes')
        else:
            results.append('yes')
        
    #State: `start` and `end` are integers where `start` <= `end`, `t` is 0, `results` is a list containing `t` elements, each element is either 'yes' or 'no' based on the conditions evaluated during each iteration of the loop.
    for r in results:
        print(r)
        
    #State: `start` and `end` are integers where `start` <= `end`, `t` is 0, `results` is a list containing `n` elements (where `n` is the total number of iterations), each element is either 'yes' or 'no' based on the conditions evaluated during each iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads another integer `n` and a string `arr` consisting of '0's and '1's. It then evaluates whether the string meets specific conditions and appends 'yes' or 'no' to a results list accordingly. Finally, it prints each result in the list. The function does not accept any parameters and does not return any value. After execution, the program state includes a list `results` containing `t` elements, each being 'yes' or 'no'.

