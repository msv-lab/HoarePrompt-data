#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end are greater than or equal to 0.
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
        
    #State: Output State: The `results` list will contain 'no' repeated `t` times, where `t` is the total number of iterations the loop executed. The values of `start`, `end`, `i`, `n`, and `arr` will be as they were last updated during the final iteration of the loop.
    #
    #In Natural Language: After the loop has executed all its iterations, the `results` list will consist of 'no' repeated `t` times. This means that regardless of the inputs provided in each iteration, the loop always appends 'no' to the `results` list. The values of `start`, `end`, `i`, `n`, and `arr` will reflect their state after the last iteration of the loop.
    for r in results:
        print(r)
        
    #State: The `results` list will contain 'no' repeated `t` times.
#Overall this is what the function does:The function reads an integer `t` and then processes `t` inputs. For each input, it checks a string `arr` containing only '0's and '1's. If `arr` contains exactly two '1's and these '1's are adjacent, it appends 'no' to the `results` list; otherwise, it appends 'yes'. After processing all inputs, it prints 'no' repeated `t` times. The final state of the program includes the `results` list containing 'no' repeated `t` times, and the variables `start`, `end`, `i`, `n`, and `arr` reflecting their state after the last iteration of the loop.

