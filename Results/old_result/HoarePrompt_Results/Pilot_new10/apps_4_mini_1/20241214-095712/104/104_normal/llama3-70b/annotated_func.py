#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and a is a list of n integers such that 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all(a[k] - a[i] == k - i for k in range(i, j)):
                max_erase = max(max_erase, j - i - 1)
        
    #State of the program after the  for loop has been executed: `max_erase` is the maximum length of segments satisfying the condition found in `a`, `i` is `n - 1`, and `j` is `n + 1`, `n` is an integer such that 1 <= `n` <= 100.
    print(max_erase)
#Overall this is what the function does:The function accepts an integer `n` (1 <= n <= 100) and a list `a` of `n` integers (1 <= a[0] < a[1] < ... < a[n-1] <= 1000), and calculates the length of the longest segment of contiguous elements in `a` such that each element in the segment has the same difference with its index as the first element. It prints the maximum length of segments found that satisfy this condition minus one. If no segments satisfying the condition exist, it will print 0.

