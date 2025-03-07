#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b such that 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9, and it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. Additionally, the sum of h over all test cases does not exceed 10^6.
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
        
    #State: Output State: The `test_cases` variable remains as an integer within the range \(1 \leq \text{test_cases} \leq 10^4\). The `i` variable is now equal to `test_cases - 1` since the loop has completed all its iterations. The `answers` list contains the results of applying the given logic to each set of input clues for all `test_cases`.
    #
    #In more detail, for each of the `test_cases` provided:
    #- If `clues[2]` is greater than `clues[4]` or `clues[0]` is 1, 'Draw' is appended to `answers`.
    #- Otherwise, based on the parity (even or odd) of `clues[2]` and `clues[4]`, and the comparison between `clues[3]` and `clues[5]`, 'Alice', 'Bob', or 'Draw' is appended to `answers`.
    #
    #The final state of `answers` is a list containing the outcomes for each of the `test_cases` according to the rules defined in the loop.
    for j in answers:
        print(j)
        
    #State: `i` is `test_cases - 1`, `answers` is a list containing the results for each of the `test_cases` according to the rules defined in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of six integers: h, w, x_a, y_a, x_b, y_b. For each test case, it determines whether Alice, Bob, or a Draw occurs based on specific conditions involving the parity of h and w, and the relative positions of x_a, y_a, x_b, and y_b. The function outputs the result for each test case in the form of 'Alice', 'Bob', or 'Draw'.

