You are given an array a of length n and q queries l , r .

For each query, find the maximum possible m , such that all elements a_l ,
a_{l+1} , ..., a_r are equal modulo m . In other words, a_l \bmod m = a_{l+1}
\bmod m = \dots = a_r \bmod m , where a \bmod b — is the remainder of division
a by b . In particular, when m can be infinite, print 0 .

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

The first line of each test case contains two integers n , q (1 \le n, q \le
2\cdot 10^5 ) — the length of the array and the number of queries.

The second line of each test case contains n integers a_i (1 \le a_i \le 10^9
) — the elements of the array.

In the following q lines of each test case, two integers l , r are provided (1
\le l \le r \le n ) — the range of the query.

It is guaranteed that the sum of n across all test cases does not exceed
2\cdot 10^5 , and the sum of q does not exceed 2\cdot 10^5 .

Output

For each query, output the maximum value m described in the statement.

Example

Input

    3
    
    5 5
    
    5 14 2 6 3
    
    4 5
    
    1 4
    
    2 4
    
    3 5
    
    1 1
    
    1 1
    
    7
    
    1 1
    
    3 2
    
    1 7 8
    
    2 3
    
    1 2

Output

    3 1 4 1 0 
    0 
    1 6 
    
Note

In the first query of the first sample, 6 \bmod 3 = 3 \bmod 3 = 0 . It can be
shown that for greater m , the required condition will not be fulfilled.

In the third query of the first sample, 14 \bmod 4 = 2 \bmod 4 = 6 \bmod 4 = 2
. It can be shown that for greater m , the required condition will not be
fulfilled.
