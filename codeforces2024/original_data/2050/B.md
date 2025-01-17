You are given an array a of length n . In one operation, you can pick an index
i from 2 to n-1 inclusive, and do one of the following actions:

  * Decrease a_{i-1} by 1 , then increase a_{i+1} by 1 .

  * Decrease a_{i+1} by 1 , then increase a_{i-1} by 1 . 

After each operation, all the values must be non-negative. Can you make all
the elements equal after any number of operations?

Input

First line of input consists of one integer t (1 \le t \le 10^4 ) — the number
of test cases.

First line of each test case consists of one integer n (3 \le n \le 2\cdot
10^5 ).

Second line of each test case consists of n integers a_i (1 \le a_i \le 10^9
).

It is guaranteed that the sum of n of all test cases doesn't exceed 2\cdot
10^5 .

Output

For each test case, print "YES" without quotation marks if it is possible to
make all the elements equal after any number of operations; otherwise, print
"NO" without quotation marks.

You can print answers in any register: "yes", "YeS", "nO" — will also be
considered correct.

Example

Input

    8
    
    3
    
    3 2 1
    
    3
    
    1 1 3
    
    4
    
    1 2 5 4
    
    4
    
    1 6 6 1
    
    5
    
    6 2 1 4 2
    
    4
    
    1 4 2 1
    
    5
    
    3 1 2 1 3
    
    3
    
    2 4 2

Output

    YES
    NO
    YES
    NO
    YES
    NO
    NO
    NO
    