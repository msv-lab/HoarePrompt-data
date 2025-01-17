Shohag has an integer n . Please help him find an increasing integer sequence
1 \le a_1 \lt a_2 \lt \ldots \lt a_n \le 100 such that a_i \bmod i \neq a_j
\bmod j ^{\text{∗}} is satisfied over all pairs 1 \le i \lt j \le n .

It can be shown that such a sequence always exists under the given
constraints.

^{\text{∗}} a \bmod b denotes the remainder of a after division by b . For
example, 7 \bmod 3 = 1, 8 \bmod 4 = 0 and 69 \bmod 10 = 9 .

Input

The first line contains a single integer t (1 \le t \le 50 ) — the number of
test cases.

The first and only line of each test case contains an integer n (2 \le n \le
50 ).

Output

For each test case, print n integers — the integer sequence that satisfies the
conditions mentioned in the statement. If there are multiple such sequences,
output any.

Example

Input

    2
    
    3
    
    6

Output

    2 7 8
    2 3 32 35 69 95
    
Note

In the first test case, the sequence is increasing, values are from 1 to 100
and each pair of indices satisfies the condition mentioned in the statement:

  * For pair (1, 2) , a_1 \bmod 1 = 2 \bmod 1 = 0 , and a_2 \bmod 2 = 7 \bmod 2 = 1 . So they are different. 
  * For pair (1, 3) , a_1 \bmod 1 = 2 \bmod 1 = 0 , and a_3 \bmod 3 = 8 \bmod 3 = 2 . So they are different. 
  * For pair (2, 3) , a_2 \bmod 2 = 7 \bmod 2 = 1 , and a_3 \bmod 3 = 8 \bmod 3 = 2 . So they are different. 

Note that you do not necessarily have to print the exact same sequence, you
can print any other sequence as long as it satisfies the necessary conditions.
