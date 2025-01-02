#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 10^5, and two lists A and B of integers are provided where A[i] and B[i] represent the i-th terms of the sequences A and B respectively, with 0 ≤ A[i] ≤ 10^9 and 1 ≤ B[i] ≤ 10^9 for all 1 ≤ i ≤ N.
def func():
    n = int(raw_input())
    ab = [map(int, raw_input().split()) for _ in xrange(n)]
    cnt = 0
    for i in xrange(n - 1, -1, -1):
        a, b = ab[i][0], ab[i][1]
        
        if (a + cnt) % b == 0:
            continue
        
        cnt += b - (a + cnt) % b
        
    #State of the program after the  for loop has been executed: 
    print(cnt)
#Overall this is what the function does:The function `func()` accepts three parameters: an integer `N`, a list `A` of integers, and a list `B` of integers. It calculates a cumulative value `cnt` based on the elements of `A` and `B`. Specifically, for each element in `B` starting from the last element and moving towards the first, it checks if adding the current value of `cnt` to the corresponding element in `A` results in a multiple of the corresponding element in `B`. If not, it adjusts `cnt` by adding the difference required to make the sum a multiple of the corresponding element in `B`. After processing all elements, it prints the final value of `cnt`.

Potential edge cases include:
- When `N` is at its minimum value (1), the function will process only one element.
- When `N` is at its maximum value (10^5), the function will process up to 10^5 elements, which may require efficient handling to avoid performance issues.

The function does not handle missing or invalid input (e.g., non-integer values for `N` or elements in `A` and `B`). These should be considered as potential improvements.

