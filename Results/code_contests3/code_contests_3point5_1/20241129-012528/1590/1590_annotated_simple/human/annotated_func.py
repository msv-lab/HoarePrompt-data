#State of the program right berfore the function call: 
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `s` is an integer value, `p` contains `n` tuples with values `(fi, ti)` where `fi` and `ti` are integer values, `i` is `n`, `fi` and `ti` are assigned integer values from the input for each tuple
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `s` is the first element of the tuple at index `n` in list `p`, `p` contains `n+1` tuples with values in descending order based on the first element of each tuple ending with (0, 0), `time_passed` is the sum of the differences between consecutive elements in the second element of each tuple in `p`, `i` is `n`
    print(time_passed)
#Overall this is what the function does:The function `func` reads input values to populate a list of tuples, sorts the list based on the first element of each tuple in descending order, calculates the time passed based on the differences between consecutive tuple elements, and prints the total time passed. However, it does not accept any parameters and does not return any value.

