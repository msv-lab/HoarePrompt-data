#State of the program right berfore the function call: A and B are integers such that 1 ≤ A, B ≤ 9.**
def func():
    testSNs = raw_input().split()
    SCORE = int(0)
    for x in range(testSNs[0]):
        if not testSNs[x] % 10 is 0:
            SCORE += testSNs[x]
        else:
            continue
        
    #State of the program after the  for loop has been executed: A and B are integers such that 1 ≤ A, B ≤ 9; testSNs is a list containing the input values. SCORE will be the sum of all elements in testSNs where the last digit of each element is not 0.
    print(SCORE)
#Overall this is what the function does:The function `func` reads an input from the user, splits the input into a list of strings, and initializes a variable `SCORE` to 0. It then iterates through the elements of the list, summing up those elements where the last digit is not 0 to the `SCORE` variable. The function prints out the final value of `SCORE`. However, the code contains errors and missing functionality as follows:
1. The code does not properly convert the input values to integers which could lead to TypeError.
2. The range function should take an integer, but it is currently passed a string which will cause a TypeError.
3. The condition `if not testSNs[x] % 10 is 0` does not correctly check if the last digit is 0, as intended, due to incorrect data type conversion.

