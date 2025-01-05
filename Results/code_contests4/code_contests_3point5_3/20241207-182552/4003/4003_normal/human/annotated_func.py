#State of the program right berfore the function call: A and B are integers such that 1 ≤ A, B ≤ 9.**
def func():
    testSNs = raw_input().split()
    SCORE = int(0)
    for x in range(testSNs[0]):
        if not testSNs[x] % 10 is 0:
            SCORE += testSNs[x]
        else:
            continue
        
    #State of the program after the  for loop has been executed: A and B are integers such that 1 ≤ A, B ≤ 9; `testSNs` is a list of strings, `SCORE` is an integer. If any element in `testSNs` is not divisible by 10, then `SCORE` is updated by adding that element from `testSNs`. If all elements in `testSNs` are divisible by 10, `SCORE` remains 0.
    print(SCORE)
#Overall this is what the function does:The function reads input values as strings, converts them to integers, and calculates a score based on the provided conditions. It iterates through the list of strings and if an element is not divisible by 10, it adds that element to the score. However, the code has issues: 
1. The loop should iterate over the range of the length of `testSNs`.
2. The condition `not testSNs[x] % 10 is 0` should be `int(testSNs[x]) % 10 != 0` to correctly check divisibility by 10.
3. The function does not return any value, it only prints the calculated score.

