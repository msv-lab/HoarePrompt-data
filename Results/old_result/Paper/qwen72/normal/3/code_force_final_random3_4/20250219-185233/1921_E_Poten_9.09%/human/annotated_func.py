#State of the program right berfore the function call: The function should take six integers as input: h, w, x_a, y_a, x_b, y_b, where 1 ≤ h ≤ 10^6, 1 ≤ w ≤ 10^9, 1 ≤ x_a, x_b ≤ h, 1 ≤ y_a, y_b ≤ w, and either x_a ≠ x_b or y_a ≠ y_b.
def func():
    test_cases = int(input())
    answers = []
    for i in range(test_cases):
        clues = list(map(int, input().split(' ')))
        
        if clues[2] > clues[4] or clues[0] == 1:
            answers.append('Draw')
        elif clues[2] % 2 == 0 and clues[4] % 2 == 0 or clues[2] % 2 != 0 and clues[4
            ] % 2 != 0:
            if clues[3] == clues[5]:
                answers.append('Bob')
            elif clues[3] < clues[5]:
                if abs(clues[3] - clues[5]) > 1:
                    if clues[3] - 1 >= abs((clues[2] - clues[4]) // 2) or clues[5
                        ] - clues[3] >= abs((clues[2] - clues[4]) // 2):
                        answers.append('Draw')
                    else:
                        answers.append('Bob')
                elif clues[3] - 1 > abs((clues[2] - clues[4]) // 2) or clues[5
                    ] - clues[3] > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Bob')
            elif clues[3] > clues[5]:
                if abs(clues[3] - clues[5]) > 1:
                    if clues[1] - clues[3] >= abs((clues[2] - clues[4]) // 2) or clues[
                        3] - clues[5] >= abs((clues[2] - clues[4]) // 2):
                        answers.append('Draw')
                    else:
                        answers.append('Bob')
                elif clues[1] - clues[3] > abs((clues[2] - clues[4]) // 2) or clues[3
                    ] - clues[5] > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Bob')
        elif clues[3] == clues[5]:
            answers.append('Alice')
        elif clues[3] < clues[5]:
            if abs(clues[3] - clues[5]) > 1:
                if clues[1] - clues[5] > abs((clues[2] - clues[4]) // 2) or clues[5
                    ] - clues[3] > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Alice')
            elif clues[1] - clues[5] - 1 > abs((clues[2] - clues[4]) // 2) or clues[5
                ] - clues[3] - 1 > abs((clues[2] - clues[4]) // 2):
                answers.append('Draw')
            else:
                answers.append('Alice')
        elif clues[3] > clues[5]:
            if abs(clues[3] - clues[5]) > 1:
                if clues[5] - 1 > abs((clues[2] - clues[4]) // 2) or clues[3] - clues[5
                    ] > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Alice')
            elif clues[5] - 1 - 1 > abs((clues[2] - clues[4]) // 2) or clues[3
                ] - clues[5] - 1 > abs((clues[2] - clues[4]) // 2):
                answers.append('Draw')
            else:
                answers.append('Alice')
        
    #State: `test_cases` is greater than or equal to the number of iterations, `i` is equal to `test_cases - 1`, `clues` is a list of integers provided by the user. The `answers` list contains a string ('Draw', 'Bob', or 'Alice') for each test case, based on the conditions evaluated in the loop.
    for j in answers:
        print(j)
        
    #State: `answers` is a list that must have at least `test_cases` strings ('Draw', 'Bob', or 'Alice'), `j` is the last string in the `answers` list.
#Overall this is what the function does:The function reads an integer `test_cases` from the user, indicating the number of test scenarios to process. For each test scenario, it reads six integers from the user, representing the dimensions of a grid (`h`, `w`) and two distinct points within this grid (`x_a`, `y_a` and `x_b`, `y_b`). Based on the relative positions of these points and the grid dimensions, the function determines the outcome of a game between Alice and Bob, appending 'Draw', 'Bob', or 'Alice' to a list `answers`. After processing all test scenarios, it prints each outcome in the `answers` list. The final state of the program is that `answers` contains `test_cases` strings, each representing the result of a test scenario.

