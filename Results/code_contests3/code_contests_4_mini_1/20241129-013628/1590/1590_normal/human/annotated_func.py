#State of the program right berfore the function call: n is an integer representing the number of passengers (1 ≤ n ≤ 100), s is an integer representing the top floor number (1 ≤ s ≤ 1000), and each passenger's data consists of two integers fi and ti (1 ≤ fi ≤ s, 1 ≤ ti ≤ 1000) for their respective floor and arrival time.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of passengers, `s` is an integer representing the top floor number based on user input, `p` is a list containing `n` tuples, each tuple (fi, ti) represents the floor information for each passenger.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of passengers (0 or greater), `s` is equal to `p[n][0]`, `p` is sorted in descending order with (0, 0) appended, `time_passed` is the total time calculated based on all iterations.
    print(time_passed)
#Overall this is what the function does:The function accepts an integer `n` representing the number of passengers and an integer `s` representing the top floor number. It then collects the floor numbers and arrival times of each passenger, calculates the total time taken to transport all passengers to their respective floors, and prints this total time. The function handles the cases where the time taken to reach a passenger's floor may need to be adjusted if the current time is less than their arrival time. It assumes valid input within specified constraints.

