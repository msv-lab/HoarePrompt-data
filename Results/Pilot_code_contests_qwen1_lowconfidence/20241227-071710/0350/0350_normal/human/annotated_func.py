#State of the program right berfore the function call: The function takes no input parameters. The sequence of integers is provided within the function body through a variable or list, where the length of the sequence is at least 1 and at most 2 * 10^5, and each element in the sequence is a non-zero integer between -10^9 and 10^9 (exclusive of 0).
def func():
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    n = int(raw_input())
    A = map(int, input().split())
    idx, size = 0, len(A)
    total = size * (1 + size) / 2
    p = [0] * size
    q = [0] * size
    if (A[0] > 0) :
        p[0], q[0] = 1, 0
    else :
        q[0], p[0] = 1, 0
    #State of the program after the if-else block has been executed: `idx` is 0, `size` is undefined, `total` is size * (1 + size) / 2, `p` is a list of `size` elements, where the first element is either 1 or 0, and the rest are 0, `q` is a list of `size` elements, where the first element is either 0 or 1, and the rest are 0, depending on whether `A[0]` is greater than 0 or less than or equal to 0.
    for i in xrange(1, size):
        if A[i] > 0:
            p[i] = p[i - 1] + 1
            q[i] = q[i - 1]
        else:
            p[i] = q[i - 1]
            q[i] = p[i - 1] + 1
        
    #State of the program after the  for loop has been executed: `size` is a positive integer, `p` is a list of `size` elements where the first element is either 2 or `q[0]` and the rest are 0, `q` is a list of `size` elements where the first element is either 0 or 1 and the rest are 0, `idx` is 0, `i` is `size`.
    print('%s %s' % (sum(q), sum(p)))
#Overall this is what the function does:The function processes a sequence of integers and calculates two sequences, `p` and `q`, based on the sign of each integer in the input sequence. Specifically, `p[i]` represents the count of positive integers encountered up to index `i`, while `q[i]` represents the count of negative integers encountered up to index `i`. After processing, the function prints the sum of elements in `q` and the sum of elements in `p`.

Potential edge cases:
- If the input sequence contains only one element, both `p` and `q` will have one element, with `p[0]` being 1 or 0 based on the sign of the first element, and `q[0]` being 0 or 1 based on the sign of the first element.
- If all elements in the sequence are positive, `p` will contain consecutive numbers starting from 1, and `q` will be all zeros.
- If all elements in the sequence are negative, `q` will contain consecutive numbers starting from 1, and `p` will be all zeros.

Missing functionality in the annotations:
- The annotation stating that `size` is undefined after the if-else block is incorrect. The variable `size` is actually defined as the length of the input sequence `A`.
- The annotation stating that `idx` is 0 and `i` is `size` after the for loop is correct, but it doesn't mention that `i` starts from 1, not 0.

