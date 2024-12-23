#State of the program right berfore the function call: The input is a list of integers representing the array $a$, where the length of the list $n$ satisfies $1 \le n \le 100$, and the elements of the list are strictly increasing integers within the range $[1, 1000]$.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a list of integers input by the user, `max_erase` is the maximum value of `a[i] - a[i-1] - 1` for all valid `i` (where `1 <= i < n`).
    print(max_erase)
#Overall this is what the function does:The function accepts a list of integers representing an array \(a\), where the length of the list \(n\) is between 1 and 100 inclusive, and the elements are strictly increasing integers within the range [1, 1000]. It calculates and prints the maximum value of \(a[i] - a[i-1] - 1\) for all valid indices \(i\) (where \(1 \le i < n\)). The function also handles the case where the list contains only one element, in which case the maximum erase value is 0. There is no missing functionality in the provided code.

