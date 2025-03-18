#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200000), p is a list of integers representing a permutation of numbers from 1 to n, and b is a list of integers consisting of zeros and ones, both of length n.
def func():
    n = int(input())
    p = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] != i + 1:
            ans += 1
        
        if b[i] == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 200000), `p` is a valid permutation of integers from 1 to `n`, `b` is a list of integers; `ans` is equal to the count of indices `i` where `p[i]` is not equal to `i + 1` plus the count of indices `i` where `b[i]` is equal to 0, across all indices from 0 to n-1.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` which is a permutation of integers from 1 to `n`, and a list `b` containing zeros and ones. It counts how many elements in `p` are not in their expected position and how many elements in `b` are zeros, and prints the total count.

