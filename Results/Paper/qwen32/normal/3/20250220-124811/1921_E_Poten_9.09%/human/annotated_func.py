#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each of the following t test cases consists of six integers h, w, x_a, y_a, x_b, y_b where 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9. It is guaranteed that either x_a != x_b or y_a != y_b. The sum of h over all test cases does not exceed 10^6.
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
        
    #State: `t` is a positive integer such that 1 <= t <= 10^4, `test_cases` is equal to `t`, `clues` is a list of integers obtained from the input, `i` is equal to `t` (indicating all iterations are completed), and `answers` is a list containing `t` elements, each either 'Draw', 'Bob', or 'Alice', determined by the conditions specified in the loop.
    for j in answers:
        print(j)
        
    #State: `t` is a positive integer such that 1 <= t <= 10^4, `test_cases` is equal to `t`, `clues` is a list of integers, `i` is 0, `answers` is a list containing `t` elements, each either 'Draw', 'Bob', or 'Alice'
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads six integers: `h` (height), `w` (width), `x_a`, `y_a` (coordinates of point A), and `x_b`, `y_b` (coordinates of point B). It then determines the outcome for each test case based on the provided coordinates and dimensions, and prints 'Alice', 'Bob', or 'Draw' for each case.

