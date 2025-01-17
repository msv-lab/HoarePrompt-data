Given three integers l , r , and G , find two integers A and B (l \le A \le B
\le r ) such that their greatest common divisor (GCD) equals G and the
distance |A - B| is maximized.

If there are multiple such pairs, choose the one where A is minimized. If no
such pairs exist, output "-1 -1".

Input

The first line contains a single integer t (1 \le t \le 10^3 ) — the number of
test cases. Then, t test cases follow.

Each test case consists of a single line containing three integers l, r, G (1
\le l \le r \le 10^{18} ; 1 \le G \le 10^{18} ) — the range boundaries and the
required GCD.

Output

For each test case, output two integers A and B — the solution to the problem,
or "-1 -1" if no such pair exists.

Example

Input

    4
    
    4 8 2
    
    4 8 3
    
    4 8 4
    
    5 7 6

Output

    4 6
    -1 -1
    4 8
    6 6
    