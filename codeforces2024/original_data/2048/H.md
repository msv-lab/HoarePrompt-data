Kevin is exploring problems related to binary strings in Chinatown. When he
was at a loss, a stranger approached him and introduced a peculiar operation:

  * Suppose the current binary string is t , with a length of \vert t \vert . Choose an integer 1 \leq p \leq \vert t \vert . For all 1 \leq i < p , simultaneously perform the operation t_i = \max(t_i, t_{i+1}) , and then delete t_p . 

For example, suppose the current binary string is 01001, and you choose p = 4
. Perform t_i = \max(t_i, t_{i+1}) for t_1 , t_2 , and t_3 , transforming the
string into 11001, then delete t_4 , resulting in 1101.

Kevin finds this strange operation quite interesting. Thus, he wants to ask
you: Given a binary string s , how many distinct non-empty binary strings can
you obtain through any number of operations (possibly zero)?

Since the answer may be very large, you only need to output the result modulo
998\,244\,353 .

Input

Each test contains multiple test cases. The first line contains a single
integer t (1\le t \le 10^4 ) — the number of test cases.

For each test case, the only line contains a binary string s ( 1 \le \lvert s
\rvert \le 10^6 ).

It is guaranteed that the sum of \lvert s \rvert over all test cases does not
exceed 10^6 .

Output

For each test case, print a single integer in the only line of the output —
the number of distinct non-empty binary strings you can obtain, modulo
998\,244\,353 .

Example

Input

    2
    
    11001
    
    000110111001100

Output

    9
    73
    
Note

In the first test case, all the binary strings you can obtain are: 11001,
1001, 1101, 001, 101, 111, 01, 11, and 1. There are 9 in total.
