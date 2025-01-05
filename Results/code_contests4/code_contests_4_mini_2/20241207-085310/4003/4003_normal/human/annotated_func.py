#State of the program right berfore the function call: A and B are integers such that 1 ≤ A, B ≤ 9.
def func():
    testSNs = raw_input().split()
    SCORE = int(0)
    for x in range(testSNs[0]):
        if not testSNs[x] % 10 is 0:
            SCORE += testSNs[x]
        else:
            continue
        
    #State of the program after the  for loop has been executed: `A` and `B` are integers between 1 and 9. `SCORE` is the sum of all elements in `testSNs` that are not multiples of 10. `testSNs` is a list of strings as input, split by spaces.
    print(SCORE)
#Overall this is what the function does:The function accepts no parameters, reads a line of input consisting of space-separated integers, and calculates the sum of these integers that are not multiples of 10. It then prints the calculated sum. However, the function does not correctly handle the input as integers because `testSNs` contains strings, and the comparison `testSNs[x] % 10` will result in a TypeError. Consequently, the function may not behave as intended if the input contains any integers that are multiples of 10 or if the input is invalid.

