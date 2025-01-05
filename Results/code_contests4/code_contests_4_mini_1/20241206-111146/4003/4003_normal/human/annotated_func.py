#State of the program right berfore the function call: A and B are integers such that 1 ≤ A ≤ 9 and 1 ≤ B ≤ 9.
def func():
    testSNs = raw_input().split()
    SCORE = int(0)
    for x in range(testSNs[0]):
        if not testSNs[x] % 10 is 0:
            SCORE += testSNs[x]
        else:
            continue
        
    #State of the program after the  for loop has been executed: `A` and `B` are integers such that 1 ≤ `A` ≤ 9, `B` is an integer such that 1 ≤ `B` ≤ 9, `testSNs` is a list of strings representing integers, `SCORE` is the sum of all integers from `testSNs[1]` to `testSNs[testSNs[0] - 1]` that are not multiples of 10.
    print(SCORE)
#Overall this is what the function does:The function reads a space-separated list of integers from user input, sums all integers except those that are multiples of 10, and prints the total score. It does not accept parameters directly and lacks input validation.

