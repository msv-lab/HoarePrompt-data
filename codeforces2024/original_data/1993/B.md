Given an array a of n positive integers.

In one operation, you can pick any pair of indexes (i, j) such that a_i and
a_j have distinct parity, then replace the smaller one with the sum of them.
More formally:

  * If a_i < a_j , replace a_i with a_i + a_j ; 
  * Otherwise, replace a_j with a_i + a_j . 

Find the minimum number of operations needed to make all elements of the array
have the same parity.

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

The first line of each test case contains a single integer n (1 \le n \le 2
\cdot 10^5 ).

The second line contains n integers a_1, a_2, \ldots, a_n (1 \le a_i \le 10^9
) — the elements of array a .

It is guaranteed that the sum of n over all test cases does not exceed 2 \cdot
10^5 .

Output

For each test case, output a single integer — the minimum number of operations
required.

Example

Input

    7
    
    5
    
    1 3 5 7 9
    
    4
    
    4 4 4 4
    
    3
    
    2 3 4
    
    4
    
    3 2 2 8
    
    6
    
    4 3 6 1 2 1
    
    6
    
    3 6 1 2 1 2
    
    5
    
    999999996 999999997 999999998 999999999 1000000000

Output

    0
    0
    2
    4
    3
    3
    3
    
Note

In the first test case, all integers already have the same parity. Therefore,
no operation is needed.

In the third test case, we can perform two operations (1, 2) and (1, 3) . The
array a transforms as follows: a = [\color{red}2, \color{red}3, 4]
\longrightarrow [\color{red}5, 3, \color{red}4] \longrightarrow [5, 3, 9] .

In the fourth test case, an example of an optimal sequence of operations is
(1, 2) , (1, 3) , (1, 4) , and (1, 4) . The array a transforms as follows: a =
[\color{red}3, \color{red}2, 2, 8] \longrightarrow [\color{red}3, 5,
\color{red}2, 8] \longrightarrow [\color{red}3, 5, 5, \color{red}8]
\longrightarrow [\color{red}{11}, 5, 5, \color{red}8] \longrightarrow [11, 5,
5, 19] .
