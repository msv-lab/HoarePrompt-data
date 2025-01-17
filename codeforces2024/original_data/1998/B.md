It is known that [Farmer John likes
Permutations](https://usaco.org/index.php?page=viewproblem2&cpid=1421), but I
like them too!

— Sun Tzu, The Art of Constructing Permutations

You are given a permutation^{\text{∗}} p of length n .

Find a permutation q of length n that minimizes the number of pairs (i, j ) (1
\leq i \leq j \leq n ) such that p_i + p_{i+1} + \ldots + p_j = q_i + q_{i+1}
+ \ldots + q_j .

^{\text{∗}} A permutation of length n is an array consisting of n distinct
integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a
permutation, but [1,2,2] is not a permutation (2 appears twice in the array),
and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input

The first line contains t (1 \leq t \leq 10^4 ) — the number of test cases.

The first line of each test case contains n (1 \leq n \leq 2 \cdot 10^5 ).

The following line contains n space-separated integers p_1, p_2, \ldots, p_n
(1 \leq p_i \leq n ) — denoting the permutation p of length n .

It is guaranteed that the sum of n over all test cases does not exceed 2 \cdot
10^5 .

Output

For each test case, output one line containing any permutation of length n
(the permutation q ) such that q minimizes the number of pairs.

Example

Input

    3
    
    2
    
    1 2
    
    5
    
    1 2 3 4 5
    
    7
    
    4 7 5 1 2 6 3

Output

    2 1
    3 5 4 2 1
    6 2 1 4 7 3 5

Note

For the first test, there exists only one pair (i, j ) (1 \leq i \leq j \leq n
) such that p_i + p_{i+1} + \ldots + p_j = q_i + q_{i+1} + \ldots + q_j ,
which is (1, 2 ). It can be proven that no such q exists for which there are
no pairs.
