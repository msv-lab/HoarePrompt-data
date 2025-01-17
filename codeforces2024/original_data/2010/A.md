You are given a sequence of integers. Output the alternating sum of this
sequence. In other words, output a_1 - a_2 + a_3 - a_4 + a_5 - \dots . That
is, the signs of plus and minus alternate, starting with a plus.

Input

The first line of the test contains one integer t (1 \le t \le 1000 ) — the
number of test cases. Then follow t test cases.

The first line of each test case contains one integer n (1 \le n \le 50 ) —
the length of the sequence. The second line of the test case contains n
integers a_1, a_2, \dots, a_n (1 \le a_i \le 100 ).

Output

Output t lines. For each test case, output the required alternating sum of the
numbers.

Example

Input

    4
    
    4
    
    1 2 3 17
    
    1
    
    100
    
    2
    
    100 100
    
    5
    
    3 1 4 1 5

Output

    -15
    100
    0
    10
    