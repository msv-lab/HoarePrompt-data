For an arbitrary grid, Robot defines its beauty to be the sum of elements in
the grid.

Robot gives you an array a of length n and an array b of length m . You
construct a n by m grid M such that M_{i,j}=a_i\cdot b_j for all 1 \leq i \leq
n and 1 \leq j \leq m .

Then, Robot gives you q queries, each consisting of a single integer x . For
each query, determine whether or not it is possible to perform the following
operation exactly once so that M has a beauty of x :

  1. Choose integers r and c such that 1 \leq r \leq n and 1 \leq c \leq m 
  2. Set M_{i,j} to be 0 for all ordered pairs (i,j) such that i=r , j=c , or both. 

Note that queries are not persistent, meaning that you do not actually set any
elements to 0 in the process — you are only required to output if it is
possible to find r and c such that if the above operation is performed, the
beauty of the grid will be x . Also, note that you must perform the operation
for each query, even if the beauty of the original grid is already x .

Input

The first line contains three integers n , m , and q (1 \leq n,m \leq 2\cdot
10^5, 1 \leq q \leq 5\cdot 10^4 ) — the length of a , the length of b , and
the number of queries respectively.

The second line contains n integers a_1, a_2, \ldots, a_n (0 \leq |a_i| \leq n
).

The third line contains m integers b_1, b_2, \ldots, b_m (0 \leq |b_i| \leq m
).

The following q lines each contain a single integer x (1 \leq |x| \leq 2\cdot
10^5 ), the beauty of the grid you wish to achieve by setting all elements in
a row and a column to 0 .

Output

For each testcase, output "YES" (without quotes) if there is a way to perform
the aforementioned operation such that the beauty is x , and "NO" (without
quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yES", "yes"
and "Yes" will be recognized as a positive response).

Examples

Input

    3 3 6
    
    -2 3 -3
    
    -2 2 -1
    
    -1
    
    1
    
    -2
    
    2
    
    -3
    
    3

Output

    NO
    YES
    NO
    NO
    YES
    NO
    
Input

    5 5 6
    
    1 -2 3 0 0
    
    0 -2 5 0 -3
    
    4
    
    -3
    
    5
    
    2
    
    -1
    
    2

Output

    YES
    YES
    YES
    YES
    NO
    YES
    
Note

In the second example, the grid is

0 -2 5 0 -3

0 4 -10 0 6

0 -6 15 0 -9

0 0 0 0 0

0 0 0 0 0

By performing the operation with r=4 and c=2 , we create the following grid:

0 0 5 0 -3

0 0 -10 0 6

0 0 15 0 -9

0 0 0 0 0

0 0 0 0 0

which has beauty 4 . Thus, we output YES.

In the second query, selecting r=3 and c=5 creates a grid with beauty -3 .

In the third query, selecting r=3 and c=3 creates a grid with beauty 5 .
