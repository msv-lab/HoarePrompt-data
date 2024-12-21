#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer is in the range of -100 to 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b, c = 0, 0
    for i in range(n):
        if i % 2 == 0:
            b += a[i]
        else:
            c += a[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers sorted in reverse order; `b` is the sum of all elements at even indices of `a`, and `c` is the sum of all elements at odd indices of `a`.
    print(b - c)
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers from the user input. It then sorts the list in descending order and calculates the sum of the integers at even indices (stored in variable `b`) and the sum of the integers at odd indices (stored in variable `c`). Finally, it prints the result of the subtraction `b - c`. The function operates under the constraints that `n` is between 1 and 100, and each integer in the list can range from -100 to 100. The function does not return any value but outputs the computed difference. Edge cases that could arise include handling lists where all numbers are negative or positive, as well as scenarios where the counts of odd and even indexed elements differ (for instance, when `n` is odd).

