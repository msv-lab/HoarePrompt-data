#State of the program right berfore the function call: The input consists of a positive integer n, followed by a list of n positive integers.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a sorted list of integers, `mex` is the minimum excluded positive integer in `a`.
    print(mex)
#Overall this is what the function does:The function takes a positive integer n and a list of n positive integers as input from the user, sorts the list in ascending order, and calculates the minimum excluded positive integer (mex) in the list. After processing the input, the function prints the calculated mex value, effectively providing the smallest positive integer that does not exist in the input list. The function does not return any value, as it directly prints the result, and it handles all potential edge cases where the input list may or may not contain the smallest positive integers. The final state of the program after it concludes is that the user's input list has been processed, and the mex value has been printed to the console, providing the user with the minimum positive integer that is not included in the input list.

