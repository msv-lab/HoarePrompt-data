#State of the program right berfore the function call: The function `func` should take three parameters: `submission_times`, `wrong_submissions`, and `hacks`. `submission_times` is a list of five integers representing the times (in minutes) of Kevin's last correct submissions for each problem, where 0 ≤ mi ≤ 119. `wrong_submissions` is a list of five integers representing the number of wrong submissions Kevin made on each problem, where 0 ≤ wi ≤ 10. `hacks` is a tuple of two integers (hs, hu) representing the number of successful and unsuccessful hacks, respectively, where 0 ≤ hs, hu ≤ 20.
def func():
    m = raw_input().split(' ')
    w = raw_input().split(' ')
    h = raw_input().split(' ')
    ans = 0
    for i in range(5):
        x = 500 * (i + 1)
        
        m1 = int(m[i])
        
        w1 = int(w[i])
        
        pts = max(0.3 * x, (1 - m1 / 250) * x - 50 * w1)
        
        ans = ans + pts
        
    #State of the program after the  for loop has been executed: `i` is 4, `submission_times` is a list of five integers, `wrong_submissions` is a list of five integers, `hacks` is a tuple of two integers, `m` is a list of strings obtained by splitting the user input by spaces, `w` is a list of strings obtained by splitting the user input by spaces, `h` is a list of strings obtained by splitting the user input by spaces, `ans` is `max(150, 500 - 2 * m1 - 50 * w1) + max(300, 1000 - 4 * m1 - 50 * w1) + max(450, 1500 - 6 * m1 - 50 * w1) + max(600, 2000 - 8 * m1 - 50 * w1) + max(750, 2500 - 10 * m1 - 50 * w1)`, where `m1` and `w1` are the integer values of the corresponding elements in `m` and `w`.
    ans = ans + 100 * int(h[0])
    ans = ans - 50 * int(h[1])
    print(ans)
#Overall this is what the function does:The function `func` reads three lines of space-separated inputs from the user, interpreting them as lists of integers. The first input is treated as the `submission_times` for five problems, the second as the `wrong_submissions` for those problems, and the third as a tuple `hacks` containing the number of successful and unsuccessful hacks. It calculates a score based on these inputs, applying specific scoring rules to each problem and adjusting the total score based on the number of successful and unsuccessful hacks. The final score is printed to the console. The function does not return any value. Potential edge cases include invalid input formats (e.g., non-integer values, incorrect number of elements), which would cause the function to raise a `ValueError`. The function assumes the input is always valid and does not handle such errors.

