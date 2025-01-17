You are given a string s , consisting of digits from 0 to 9 . In one
operation, you can pick any digit in this string, except for 0 or the leftmost
digit, decrease it by 1 , and then swap it with the digit left to the picked.

For example, in one operation from the string 1023 , you can get 1103 or 1022
.

Find the lexicographically maximum string you can obtain after any number of
operations.

Input

The first line of the input consists of an integer t (1 \le t \le 10^4 ) — the
number of test cases.

Each test case consists of a single line consisting of a digital string s (1
\le |s| \le 2\cdot 10^5 ), where |s| denotes the length of s . The string does
not contain leading zeroes.

It is guaranteed that the sum of |s| of all test cases doesn't exceed 2\cdot
10^5 .

Output

For each test case, print the answer on a separate line.

Example

Input

    6
    
    19
    
    1709
    
    11555
    
    51476
    
    9876543210
    
    5891917899

Output

    81
    6710
    33311
    55431
    9876543210
    7875567711
    
Note

In the first example, the following sequence of operations is suitable: 19
\rightarrow 81 .

In the second example, the following sequence of operations is suitable: 1709
\rightarrow 1780 \rightarrow 6180 \rightarrow 6710 .

In the fourth example, the following sequence of operations is suitable: 51476
\rightarrow 53176 \rightarrow 53616 \rightarrow 53651 \rightarrow 55351
\rightarrow 55431 .
