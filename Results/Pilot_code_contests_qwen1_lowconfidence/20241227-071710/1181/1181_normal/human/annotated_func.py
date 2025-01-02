#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 3·10^5, and the second line contains n integers x1, x2, ..., xn such that 1 ≤ xi ≤ 10^9 and all xi are distinct.
def func():
    n = int(raw_input())
    s = sorted(map(int, raw_input().split()))
    r = 0
    for i in xrange(n):
        r += s[i] * (2 ** (n - 1 - i) - 1 - (2 ** i - 1)) % (1000000000 + 7)
        
    #State of the program after the  for loop has been executed: Let's analyze the given loop step by step to determine the final output state after all iterations of the loop have finished.
    #
    #### Initial State
    #- \( n \) is an integer such that \( 1 \leq n \leq 3 \times 10^5 \).
    #- \( s \) is a sorted list of integers.
    #- \( r \) is 0.
    #
    #### Loop Code
    #```python
    #for i in range(n):
    #    r += s[i] * (2 ** (n - 1 - i) - 1 - (2 ** i - 1)) % (1000000000 + 7)
    #```
    #
    #### Analysis of the Loop
    #- The loop runs from \( i = 0 \) to \( i = n - 1 \).
    #- For each iteration, the value of \( r \) is updated based on the formula:
    #  \[
    #  r \leftarrow r + s[i] \times (2^{n-1-i} - 1 - (2^i - 1)) \mod (1000000000 + 7)
    #  \]
    #
    #### Simplification of the Formula
    #Let's simplify the expression inside the loop:
    #\[
    #2^{n-1-i} - 1 - (2^i - 1) = 2^{n-1-i} - 2^i
    #\]
    #This can be further simplified as:
    #\[
    #2^{n-1-i} - 2^i = 2^i (2^{n-2i-1} - 1)
    #\]
    #So, the update to \( r \) becomes:
    #\[
    #r \leftarrow r + s[i] \times 2^i (2^{n-2i-1} - 1) \mod (1000000000 + 7)
    #\]
    #
    #### Final Value of \( r \)
    #After all \( n \) iterations, \( r \) will be the sum of the terms:
    #\[
    #r = \sum_{i=0}^{n-1} s[i] \times 2^i (2^{n-2i-1} - 1) \mod (1000000000 + 7)
    #\]
    #
    #### Final Output State
    #- \( n \) remains the same as the initial value.
    #- \( s \) remains the same as the initial value.
    #- \( r \) is the sum of the terms described above.
    #
    #### Conclusion
    #The final output state after all iterations of the loop have finished is:
    #\[
    #\text{Output State: } n \text{ is an integer such that } 1 \leq n \leq 3 \times 10^5, \text{ } s \text{ is a sorted list of integers, } r \text{ is } \sum_{i=0}^{n-1} s[i] \times 2^i (2^{n-2i-1} - 1) \mod (1000000000 + 7).
    #\]
    print - r
#Overall this is what the function does:The function processes a list of distinct integers of length \( n \) (where \( 1 \leq n \leq 3 \times 10^5 \)), each integer being between 1 and \( 10^9 \). It calculates the sum of the elements in the list multiplied by a specific weighted factor, which is derived from powers of 2 and their differences. The calculation involves a loop that iterates over each element in the list, updating a running total `r` according to the formula:

\[
r \leftarrow r + s[i] \times 2^i (2^{n-2i-1} - 1) \mod (1000000000 + 7)
\]

After processing all elements, the function outputs the negation of the final value of `r`.

