#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100000, and a is a list of integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 10^9.
def func():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    mex = 1
    for num in arr:
        if num == mex:
            mex += 1
        elif num > mex:
            break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100000, `a` is a list of integers, `arr` is a sorted list containing integers, and `mex` is the smallest positive integer not present in `arr`. If the loop does not execute, `mex` remains 1. If the loop executes multiple times, `mex` will be incremented up to the largest consecutive integer present in `arr`, which depends on the values in `arr`.
    print(mex)
#Overall this is what the function does:The function takes an integer input `n`, representing the number of integers to follow, and a list of integers provided via standard input. It processes this list to determine the smallest positive integer (Minimum Excludant or MEX) that is not present in the list. After sorting the list, the function iterates through the sorted integers, incrementing a `mex` variable starting from 1 for each consecutive integer found in the list. If an integer greater than the current `mex` is encountered, the loop terminates, and the final value of `mex` is printed. The edge cases handled include the scenario where the list does not contain consecutive integers starting from 1, causing `mex` to remain 1. If `arr` includes all integers from 1 to `n`, `mex` will be `n + 1`. The function effectively determines the MEX for any valid input according to the defined constraints.

