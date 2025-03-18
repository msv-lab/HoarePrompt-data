#State of the program right berfore the function call: The function `func` is intended to solve a game problem but lacks parameters in its definition. The correct function definition should include parameters for the board dimensions `h` and `w`, and the initial positions of Alice's and Bob's chips `(x_a, y_a)` and `(x_b, y_b)`. The correct function definition should be: `def func(h, w, x_a, y_a, x_b, y_b):` where `h` and `w` are the height and width of the board, respectively, and `x_a, y_a, x_b, y_b` are the initial coordinates of Alice's and Bob's chips, with the constraints: 1 ≤ `x_a`, `x_b` ≤ `h` ≤ 10^6, 1 ≤ `y_a`, `y_b` ≤ `w` ≤ 10^9, and it is guaranteed that either `x_a` ≠ `x_b` or `y_a` ≠ `y_b`.
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
        
    #State: `answers` is a list containing the results of the game problem for each of the `test_cases` test cases, where each result is either 'Alice', 'Bob', or 'Draw'.
    for j in answers:
        print(j)
        
    #State: The list `answers` remains unchanged, and the loop has printed each element of the list `answers` to the console.
#Overall this is what the function does:The function `func` reads a series of game scenarios from user input, processes each scenario to determine the winner (Alice, Bob, or Draw) based on the initial positions of their chips and the board dimensions, and prints the result for each scenario. The function does not return any value; instead, it prints the results directly to the console. After the function concludes, the list `answers` contains the results of all the game scenarios, and these results have been printed to the console.

