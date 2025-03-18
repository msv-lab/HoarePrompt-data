#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200000; p is a list of integers representing a permutation of numbers from 1 to n; b is a list of integers consisting of zeros and ones, with the same length as p.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200000; `p` is a list of integers with length `n`; `b` is a list of integers (0s and 1s) with length `n`; `ans` is equal to the count of indices `i` where `p[i]` is not equal to `i + 1` plus the count of indices `i` where `b[i]` is 0.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` and two lists `p` and `b`, where `p` is a permutation of numbers from 1 to `n`, and `b` consists of zeros and ones. It counts the number of indices `i` where `p[i]` does not equal `i + 1` and adds to this count the number of indices where `b[i]` is 0, returning their sum as the output.

