#State of the program right berfore the function call: **Precondition**: **n and s are positive integers such that 1 <= n <= 100 and 1 <= s <= 1000. fi and ti are positive integers representing the floor and time of arrival for each passenger, respectively, such that 1 <= fi <= s and 1 <= ti <= 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `s` is a positive integer, `p` contains a list of tuples `(fi, ti)` values obtained from the input split by spaces for each iteration of the loop.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `s` is 0, `p` contains a list of tuples sorted based on the first element of each tuple in descending order with the addition of the tuple (0, 0), `time_passed` is the total sum of differences between each consecutive tuple's first element and the corresponding second element in list `p`.
    print(time_passed)
#Overall this is what the function does:The function `func` reads input values for `n`, `s`, `fi`, and `ti` based on specified constraints. It then processes the input data to calculate the total time passed for each passenger's arrival. The function does not accept any parameters and outputs the total time passed.

