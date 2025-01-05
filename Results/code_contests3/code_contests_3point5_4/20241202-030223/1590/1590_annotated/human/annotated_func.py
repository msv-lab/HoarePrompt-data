#State of the program right berfore the function call: **Precondition**: **n and s are integers such that 1 <= n <= 100 and 1 <= s <= 1000. Each passenger's floor fi is an integer such that 1 <= fi <= s, and the time of arrival ti is an integer such that 1 <= ti <= 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `s` is an integer between 1 and 1000, `p` contains `n` tuples with values `(fi, ti)`, `i` is `n-1`, `fi` and `ti` are assigned values obtained from mapping integers from user input
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, the final output state cannot be accurately determined without the initial state and full loop conditions as the if statement condition depends on the value of `time_passed` and `p[i][1]`.
    print(time_passed)
#Overall this is what the function does:The function `func` reads input for the number of passengers `n` and floors `s`, then simulates an elevator system with `n` passengers and `s` floors. It sorts the passengers based on their destination floors and calculates the total time taken for all passengers to reach their respective floors, considering the elevator moving between floors and stopping according to passenger arrival times. However, the final output state after the simulation loop cannot be determined without additional context, making it unclear if the calculated time is accurate.

