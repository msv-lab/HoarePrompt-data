#State of the program right berfore the function call: n and s are integers such that 1 <= n <= 100 and 1 <= s <= 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `s` is an integer between 1 and 1000, `p` contains `n` tuples with unknown values, `fi` and `ti` are assigned values from the input after mapping them to integers
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `s` is an integer between 1 and 1000, `p` is sorted in descending order based on the first element of the tuples, `fi` and `ti` are assigned values from the input after mapping them to integers, a tuple (0, 0) is appended to the list `p`, `time_passed` is the total accumulated time after all iterations of the loop.
    print(time_passed)
#Overall this is what the function does:The function `func` reads input for `n` and `s`, where `n` is an integer between 1 and 100, and `s` is an integer between 1 and 1000. It then reads `n` pairs of integers and sorts them in descending order based on the first element of the tuples. After that, it calculates the time passed based on the values stored in the pairs. The function does not have a return value and prints the total accumulated time at the end.

