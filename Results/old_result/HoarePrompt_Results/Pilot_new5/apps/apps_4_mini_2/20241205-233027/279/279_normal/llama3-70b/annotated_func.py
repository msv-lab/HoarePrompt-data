#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200000), p is a list of integers representing a permutation of numbers from 1 to n, and b is a list of integers consisting of zeros and ones, both lists having a length of n.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 200000), `p` is a list of integers based on the input, `b` is a list of integers consisting of zeros and ones based on the input, `ans` is equal to the count of elements in `p` that are not in their correct position (i + 1) plus the count of zeros in `b`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` and two lists, `p`, which is a permutation of integers from 1 to `n`, and `b`, which consists of zeros and ones. It counts the number of elements in `p` that are not in their correct position (i.e., `p[i] != i + 1`) and adds the count of zeros in `b`. The function then outputs the total count, which can range from 0 to `2n`, covering the cases where all elements are misplaced and all values in `b` are zeros.

