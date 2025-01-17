You are given an integer array a of size n . The elements of the array are
numbered from 1 to n .

You can perform the following operation any number of times (possibly, zero):
choose an index i from 1 to n ; decrease a_i by 2 and increase a_{(i \bmod n)
+ 1} by 1 .

After you perform the operations, all elements of the array should be non-
negative equal integers.

Your task is to calculate the minimum number of operations you have to
perform.

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

The first line of each test case contains a single integer n (2 \le n \le 2
\cdot 10^5 ).

The second line of each test case contains n integers a_1, a_2, \dots, a_n (1
\le a_i \le 10^9 ).

Additional constraint on the input: the sum of n over all test cases doesn't
exceed 2 \cdot 10^5 .

Output

For each test case, print a single integer — the minimum number of operations
you have to perform. If it is impossible to make all elements of the array
equal, print -1.

Example

Input

    3
    
    2
    
    1 1
    
    3
    
    1 3 2
    
    4
    
    2 1 2 6

Output

    0
    -1
    3
    