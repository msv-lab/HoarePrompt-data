On the board Ivy wrote down all integers from l to r , inclusive.

In an operation, she does the following:

  * pick two numbers x and y on the board, erase them, and in their place write the numbers 3x and \lfloor \frac{y}{3} \rfloor . (Here \lfloor \bullet \rfloor denotes rounding down to the nearest integer).

What is the minimum number of operations Ivy needs to make all numbers on the
board equal 0 ? We have a proof that this is always possible.

Input

The first line contains an integer t (1 \leq t \leq 10^4 ) — the number of
test cases.

The only line of each test case contains two integers l and r (1 \leq l < r
\leq 2 \cdot 10^5 ).

Output

For each test case, output a single integer — the minimum number of operations
needed to make all numbers on the board equal 0 .

Example

Input

    4
    
    1 3
    
    2 4
    
    199999 200000
    
    19 84

Output

    5
    6
    36
    263
    
Note

In the first test case, we can perform 5 operations as follows:
