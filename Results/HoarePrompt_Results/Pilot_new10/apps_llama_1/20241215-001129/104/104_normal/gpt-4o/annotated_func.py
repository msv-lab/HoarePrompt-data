#State of the program right berfore the function call: The input to the function is a sequence of integers where the first integer n is the number of elements in the array (1 ≤ n ≤ 100), and the next n integers are the elements of the array a (1 ≤ a1 < a2 <... < an ≤ 10^3).
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer where 1 ≤ n ≤ 100, `a` is a list of `n` integers where 1 ≤ a1 < a2 <... < an ≤ 10^3, `max_erase` is the maximum of 0 and the maximum difference between any two consecutive elements in `a` minus 1, and `i` is `n - 1` if `n` > 1, otherwise `i` will be 0 because the loop doesn't execute.
    print(max_erase)
#Overall this is what the function does:The function accepts a sequence of integers representing an array size n and its elements a, calculates the maximum difference between any two consecutive elements in a minus 1, and prints this value as the result, handling potential edge cases such as arrays with one or zero elements, and arrays with duplicate or negative elements.

