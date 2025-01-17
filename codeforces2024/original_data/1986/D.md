You are given a string s of length n > 1 , consisting of digits from 0 to 9 .
You must insert exactly n - 2 symbols + (addition) or \times (multiplication)
into this string to form a valid arithmetic expression.

In this problem, the symbols cannot be placed before the first or after the
last character of the string s , and two symbols cannot be written
consecutively. Also, note that the order of the digits in the string cannot be
changed. Let's consider s = 987009 :

  * From this string, the following arithmetic expressions can be obtained: 9 \times 8 + 70 \times 0 + 9 = 81 , 98 \times 7 \times 0 + 0 \times 9 = 0 , 9 + 8 + 7 + 0 + 09 = 9 + 8 + 7 + 0 + 9 = 33 . Note that the number 09 is considered valid and is simply transformed into 9 .
  * From this string, the following arithmetic expressions cannot be obtained: +9 \times 8 \times 70 + 09 (symbols should only be placed between digits), 98 \times 70 + 0 + 9 (since there are 6 digits, there must be exactly 4 symbols).

The result of the arithmetic expression is calculated according to the rules
of mathematics — first all multiplication operations are performed, then
addition. You need to find the minimum result that can be obtained by
inserting exactly n - 2 addition or multiplication symbols into the given
string s .

Input

Each test consists of multiple test cases. The first line contains a single
integer t (1 \leq t \leq 10^4 ) — the number of test cases. Then follows their
description.

The first line of each test case contains a single integer n (2 \leq n \leq 20
) — the length of the string s .

The second line of each test case contains a string s of length n , consisting
of digits from 0 to 9 .

Output

For each test case, output the minimum result of the arithmetic expression
that can be obtained by inserting exactly n - 2 addition or multiplication
symbols into the given string.

Example

Input

    18
    
    2
    
    10
    
    2
    
    74
    
    2
    
    00
    
    2
    
    01
    
    3
    
    901
    
    3
    
    101
    
    5
    
    23311
    
    6
    
    987009
    
    7
    
    1111111
    
    20
    
    99999999999999999999
    
    20
    
    00000000000000000000
    
    4
    
    0212
    
    18
    
    057235283621345395
    
    4
    
    1112
    
    20
    
    19811678487321784121
    
    4
    
    1121
    
    4
    
    2221
    
    3
    
    011

Output

    10
    74
    0
    1
    9
    1
    19
    0
    11
    261
    0
    0
    0
    12
    93
    12
    24
    0
    
Note

In the first four test cases, we cannot add symbols, so the answer will be the
original number.

In the fifth test case, the optimal answer looks as follows: 9 \times 01 = 9
\times 1 = 9 .

In the sixth test case, the optimal answer looks as follows: 1 \times 01 = 1
\times 1 = 1 .

In the seventh test case, the optimal answer looks as follows: 2 + 3 + 3 + 11
= 19 .

In the eighth test case, one of the optimal answers looks as follows: 98
\times 7 \times 0 + 0 \times 9 = 0 .
