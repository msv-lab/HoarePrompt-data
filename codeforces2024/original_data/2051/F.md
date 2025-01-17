Consider a deck of n cards. The positions in the deck are numbered from 1 to n
from top to bottom. A joker is located at position m .

q operations are applied sequentially to the deck. During the i -th operation,
you need to take the card at position a_i and move it either to the beginning
or to the end of the deck. For example, if the deck is [2, 1, 3, 5, 4] , and
a_i=2 , then after the operation the deck will be either [1, 2, 3, 5, 4] (the
card from the second position moved to the beginning) or [2, 3, 5, 4, 1] (the
card from the second position moved to the end).

Your task is to calculate the number of distinct positions where the joker can
be after each operation.

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

The first line of each test case contains three integers n , m , and q (2 \le
n \le 10^9 ; 1 \le m \le n ; 1 \le q \le 2 \cdot 10^5 ).

The second line contains q integers a_1, a_2, \dots, a_q (1 \le a_i \le n ).

Additional constraint on the input: the sum of q over all test cases does not
exceed 2 \cdot 10^5 .

Output

For each test case, print q integers — the number of distinct positions where
the joker can be after each operation.

Example

Input

    5
    
    6 5 3
    
    1 2 3
    
    2 1 4
    
    2 1 1 2
    
    5 3 1
    
    3
    
    3 2 4
    
    2 1 1 1
    
    18 15 4
    
    13 15 1 16

Output

    2 3 5 
    2 2 2 2 
    2 
    2 3 3 3 
    2 4 6 8 
    