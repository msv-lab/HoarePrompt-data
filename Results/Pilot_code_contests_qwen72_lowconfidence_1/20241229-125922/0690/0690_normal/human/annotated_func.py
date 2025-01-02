#State of the program right berfore the function call: N is an integer where 1 ≤ N ≤ 100, and A is a 2D list of integers where 1 ≤ A_{i, j} ≤ 100 for 1 ≤ i ≤ 2 and 1 ≤ j ≤ N.
def func():
    N = int(raw_input())
    A = raw_input().split(' ')
    B = raw_input().split(' ')
    A = map(int, A)
    B = map(int, B)
    maxim = 0
    for i in xrange(1, N + 1):
        temp = sum(A[0:i]) + sum(B[i - 1:N])
        
        print(sum(A[0:i]), sum(B[i - 1:N]))
        
        if maxim < temp:
            maxim = temp
        
    #State of the program after the  for loop has been executed: `N` is an integer where 1 ≤ N ≤ 100, `i` is `N + 1`, `A` is a map object containing integers derived from the original list of strings, `B` is a map object of integers derived from the original list of strings, `maxim` is the maximum value of `sum(A[0:i]) + sum(B[i-1:N])` for all `i` from 1 to `N`.
    print(maxim)
#Overall this is what the function does:The function reads an integer `N` and two lists of integers `A` and `B` from the standard input. It then calculates the maximum possible sum of the first `i` elements of `A` and the last `N-i+1` elements of `B` for all `i` from 1 to `N`. The function prints the maximum sum found and the intermediate sums for each `i`. The function does not return any value. The final state of the program includes `N` being an integer between 1 and 100, `A` and `B` being lists of integers, and `maxim` holding the maximum sum calculated. Edge cases include handling invalid inputs (e.g., non-integer values or incorrect list lengths), which are not addressed in the current implementation.

