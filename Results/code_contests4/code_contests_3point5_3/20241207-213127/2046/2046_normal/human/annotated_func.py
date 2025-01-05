#State of the program right berfore the function call: **
def func():
    le = sys.__stdin__.read().split('\n')[::-1]
    af = []
    for zorg in range(int(le.pop())):
        n = int(le.pop())
        
        l = le.pop()
        
        l = [k for k in range(n) if l[k] == '*']
        
        l = [(b - a) for a, b in enumerate(l)]
        
        if l:
            med = l[len(l) // 2]
            af.append(sum(abs(k - med) for k in l))
        else:
            af.append(0)
        
    #State of the program after the  for loop has been executed: `le` is an empty list, `af` is a list containing the sum of absolute differences between each element of `l` and `med` for each iteration of the loop, `zorg` is the number of iterations of the loop, `n` is 0, `l` is an empty list, `med` is the middle element of `l` which is also empty
    print('\n'.join(map(str, af)))
#Overall this is what the function does:The function reads input from the standard input, processes the data according to certain rules, and prints the results to the standard output. It involves iterating over a specified number of test cases, extracting data, calculating the sum of absolute differences based on specific criteria, and outputting the results. However, the function does not accept any parameters and does not return any value.

