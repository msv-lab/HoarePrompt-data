#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a1, a2, ..., an is a list of n integers where each integer is either 0 or 1.
def func():
    n = int(input())
    a = map(int, raw_input().split())
    maximum_count = 0
    for start in range(0, n):
        for end in range(0, n):
            if start <= end:
                b = list(a)
                for i in range(start, end + 1):
                    b[i] = 1 - b[i]
                count = sum(b)
                maximum_count = max(maximum_count, count)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `maximum_count` is the maximum count of 1s that can be obtained by toggling segments of the list `a`, `start` is equal to `n`, `end` is less than `n`, and `count` is the sum of the elements in the last toggled list `b`.
    print(maximum_count)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and a list of `n` integers (each either 0 or 1), and computes the maximum number of 1's in the list that can be achieved by toggling any contiguous subarray. It returns this maximum count as output. The function does not handle cases where the input is invalid or outside the specified range for `n`.

