#State of the program right berfore the function call: n is a positive integer (1 <= n <= 100), and a is a list of n integers such that 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all(a[k] - a[i] == k - i for k in range(i, j)):
                max_erase = max(max_erase, j - i - 1)
        
    #State of the program after the  for loop has been executed: `max_erase` is the maximum value of `j - i - 1` for all valid indices `i` and `j` such that the condition `all(a[k] - a[i] == k - i for k in range(i, j))` holds true, where `n` is the length of the list `a` and `a` is a list of integers satisfying `1 <= a[0] < a[1] < ... < a[n-1] <= 1000`. If the loop does not execute, `max_erase` remains 0.
    print(max_erase)
#Overall this is what the function does:The function reads a positive integer `n` and a list `a` of `n` strictly increasing integers from the user input. It calculates the maximum number of integers that can be "erased" (i.e., values that can be removed while satisfying a specific condition related to the sorted nature of the input list). The condition checks for consecutive values based on their indices and updates a variable, `max_erase`, to reflect the maximum count of such removable integers, which is eventually printed. If no values meet the criteria to be considered removable, `max_erase` will remain zero, indicating that no elements can be erased under the specified rule. The function doesn't explicitly handle invalid inputs or edge cases such as when n is not within the provided bounds, nor does it check if inputs are non-integer or improperly formatted.

