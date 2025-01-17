[Shirobon - FOX](https://soundcloud.com/shirobon/fox?in=mart_207/sets/fav)

⠀

You are given n points on the x axis, at increasing positive integer
coordinates x_1 < x_2 < \ldots < x_n .

For each pair (i, j) with 1 \leq i < j \leq n , you draw the segment [x_i,
x_j] . The segments are closed, i.e., a segment [a, b] contains the points a,
a+1, \ldots, b .

You are given q queries. In the i -th query, you are given a positive integer
k_i , and you have to determine how many points with integer coordinates are
contained in exactly k_i segments.

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 10^4 ). The description of the test cases follows.

The first line of each test case contains two integers n , q (2 \le n \le 10^5
, 1 \le q \le 10^5 ) — the number of points and the number of queries.

The second line of each test case contains n integers x_1, x_2, \ldots, x_n (1
\leq x_1 < x_2 < \ldots < x_n \leq 10^9 ) — the coordinates of the n points.

The third line of each test case contains q integers k_1, k_2, \ldots, k_q (1
\leq k_i \leq 10^{18} ) — the parameters of the q queries.

It is guaranteed that the sum of n over all test cases does not exceed 10^5 ,
and the sum of q over all test cases does not exceed 10^5 .

Output

For each test case, output a single line with q integers: the i -th integer is
the answer to the i -th query.

Example

Input

    3
    
    2 2
    
    101 200
    
    2 1
    
    6 15
    
    1 2 3 5 6 7
    
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    
    5 8
    
    254618033 265675151 461318786 557391198 848083778
    
    6 9 15 10 6 9 4 4294967300

Output

    0 100 
    0 0 0 0 2 0 0 0 3 0 2 0 0 0 0 
    291716045 0 0 0 291716045 0 301749698 0 
    
Note

In the first example, you only draw the segment [101, 200] . No point is
contained in exactly 2 segments, and the 100 points 101, 102, \ldots, 200 are
contained in exactly 1 segment.

In the second example, you draw 15 segments: [1, 2], [1, 3], [1, 5], [1, 6],
[1, 7], [2, 3], [2, 5], [2, 6], [2, 7], [3, 5], [3, 6], [3, 7], [5, 6], [5,
7], [6, 7] . Points 1, 7 are contained in exactly 5 segments; points 2, 4, 6
are contained in exactly 9 segments; points 3, 5 are contained in exactly 11
segments.
