You are given an array of N integers: [A_1, A_2, \dots, A_N] .

A subsequence can be derived from an array by removing zero or more elements
without changing the order of the remaining elements. For example, [2, 1, 2] ,
[3, 3] , [1] , and [3, 2, 1, 3, 2] are subsequences of array [3, 2, 1, 3, 2] ,
while [1, 2, 3] is not a subsequence of array [3, 2, 1, 3, 2] .

A subsequence is microwavable if the subsequence consists of at most two
distinct values and each element differs from its adjacent elements. For
example, [2, 1, 2] , [3, 2, 3, 2] , and [1] are microwavable, while [3, 3] and
[3, 2, 1, 3, 2] are not microwavable.

Denote a function f(x, y) as the length of the longest microwavable
subsequence of array A such that each element within the subsequence is either
x or y . Find the sum of f(x, y) for all 1 \leq x < y \leq M .

Input

The first line consists of two integers N M (1 \leq N, M \leq 300\,000 ).

The second line consists of N integers A_i (1 \leq A_i \leq M ).

Output

Output a single integer representing the sum of f(x, y) for all 1 \leq x < y
\leq M .

Examples

Input

    5 4
    3 2 1 3 2
    
Output

    13
    
Input

    3 3
    1 1 1
    
Output

    2
    
Note

Explanation for the sample input/output #1

The value of f(1, 2) is 3 , taken from the subsequence [2, 1, 2] that can be
obtained by removing A_1 and A_4 . The value of f(1, 3) is 3 , taken from the
subsequence [3, 1, 3] that can be obtained by removing A_2 and A_5 . The value
of f(2, 3) is 4 , taken from the subsequence [3, 2, 3, 2] that can be obtained
by removing A_3 . The value of f(1, 4) , f(2, 4) , and f(3, 4) are all 1 .

Explanation for the sample input/output #2

The value of f(1, 2) and f(1, 3) are both 1 , while the value of f(2, 3) is 0
.
