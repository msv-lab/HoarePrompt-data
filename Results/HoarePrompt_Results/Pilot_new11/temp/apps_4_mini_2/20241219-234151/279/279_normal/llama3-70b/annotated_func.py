#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2·10^5, p is a list of integers representing a permutation of integers from 1 to n, and b is a list of integers consisting of zeros and ones with a length of n.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 2·10^5; `p` is a list representing a permutation of integers from 1 to `n`; `b` is a list of zeros and ones with length `n`; `ans` is the count of elements in `p` that do not match their index (i.e., `p[i] != i + 1`) plus the count of indices `i` where `b[i]` is 0; `i` is `n - 1` after the final iteration.
    print(ans)
#Overall this is what the function does:The function takes three inputs: an integer n, a list p that is a permutation of integers from 1 to n, and a list b consisting only of zeros and ones, all with a length of n. It computes a value `ans` which is the sum of two counts: the number of elements in list p that are not in their correct positions (where the correct position for an integer x is index x-1) and the count of indices in list b that contain the value 0. After processing, the function prints the value of `ans`. The function does not return any value directly; it only prints the result to the standard output. The function does not handle any errors related to input size or input format.

