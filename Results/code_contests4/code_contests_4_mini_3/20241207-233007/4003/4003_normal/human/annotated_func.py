#State of the program right berfore the function call: A and B are integers such that 1 ≤ A, B ≤ 9.
def func():
    testSNs = raw_input().split()
    SCORE = int(0)
    for x in range(testSNs[0]):
        if not testSNs[x] % 10 is 0:
            SCORE += testSNs[x]
        else:
            continue
        
    #State of the program after the  for loop has been executed: `A` and `B` are integers, `testSNs` is a list of strings with at least 1 element, `SCORE` is the sum of all non-multiple-of-10 integer values from `testSNs[1:]`, or 0 if all are multiples of 10.
    print(SCORE)
#Overall this is what the function does:The function reads a list of integers from input, sums all integers that are not multiples of 10, and prints this sum. It does not accept any parameters and has no return value. If all integers are multiples of 10, the printed score will be 0. Additionally, the function has a bug where it incorrectly attempts to use `testSNs[0]` as the upper limit for the loop, which may lead to incorrect behavior.

