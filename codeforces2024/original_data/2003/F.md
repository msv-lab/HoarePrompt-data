Piggy gives Turtle three sequences a_1, a_2, \ldots, a_n , b_1, b_2, \ldots,
b_n , and c_1, c_2, \ldots, c_n .

Turtle will choose a subsequence of 1, 2, \ldots, n of length m , let it be
p_1, p_2, \ldots, p_m . The subsequence should satisfy the following
conditions:

  * a_{p_1} \le a_{p_2} \le \cdots \le a_{p_m} ; 
  * All b_{p_i} for all indices i are pairwise distinct, i.e., there don't exist two different indices i , j such that b_{p_i} = b_{p_j} . 

Help him find the maximum value of \sum\limits_{i = 1}^m c_{p_i} , or tell him
that it is impossible to choose a subsequence of length m that satisfies the
conditions above.

Recall that a sequence a is a subsequence of a sequence b if a can be obtained
from b by the deletion of several (possibly, zero or all) elements.

Input

The first line contains two integers n and m (1 \le n \le 3000 , 1 \le m \le 5
) — the lengths of the three sequences and the required length of the
subsequence.

The second line contains n integers a_1, a_2, \ldots, a_n (1 \le a_i \le n ) —
the elements of the sequence a .

The third line contains n integers b_1, b_2, \ldots, b_n (1 \le b_i \le n ) —
the elements of the sequence b .

The fourth line contains n integers c_1, c_2, \ldots, c_n (1 \le c_i \le 10^4
) — the elements of the sequence c .

Output

Output a single integer — the maximum value of \sum\limits_{i = 1}^m c_{p_i} .
If it is impossible to choose a subsequence of length m that satisfies the
conditions above, output -1 .

Examples

Input

    4 2
    
    2 3 4 2
    
    1 3 3 2
    
    1 4 2 3

Output

    5
    
Input

    7 3
    
    1 4 5 2 3 6 7
    
    1 2 2 1 1 3 2
    
    1 5 6 7 3 2 4

Output

    13
    
Input

    5 3
    
    1 2 3 4 5
    
    1 1 2 1 2
    
    5 4 3 2 1

Output

    -1
    
Note

In the first example, we can choose p = [1, 2] , then c_{p_1} + c_{p_2} = 1 +
4 = 5 . We can't choose p = [2, 4] since a_2 > a_4 , violating the first
condition. We can't choose p = [2, 3] either since b_2 = b_3 , violating the
second condition. We can choose p = [1, 4] , but c_1 + c_4 = 4 , which isn't
maximum.

In the second example, we can choose p = [4, 6, 7] .

In the third example, it is impossible to choose a subsequence of length 3
that satisfies both of the conditions.
