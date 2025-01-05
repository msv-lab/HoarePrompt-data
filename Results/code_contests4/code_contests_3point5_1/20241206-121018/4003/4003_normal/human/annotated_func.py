#State of the program right berfore the function call: A and B are integers such that 1 ≤ A, B ≤ 9.**
def func():
    testSNs = raw_input().split()
    SCORE = int(0)
    for x in range(testSNs[0]):
        if not testSNs[x] % 10 is 0:
            SCORE += testSNs[x]
        else:
            continue
        
    #State of the program after the  for loop has been executed: A and B are integers such that 1 ≤ A, B ≤ 9; testSNs is a list of strings. The SCORE will be the sum of all elements in testSNs where the last digit is not 0.
    print(SCORE)
#Overall this is what the function does:The function `func` reads input from the user, calculates a score based on the input values, and prints the total score. The function does not accept any parameters and does not return any value. However, there are some issues in the code:
1. The loop should iterate over the range of integers, not strings in the `testSNs` list.
2. The comparison in the if statement should check for equality (`==`) rather than identity (`is`) for proper evaluation.
3. The current implementation only sums up elements where the last digit is not 0, which may not be the intended behavior.

