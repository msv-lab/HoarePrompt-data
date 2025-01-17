You are given three non-negative integers b , c , and d .

Please find a non-negative integer a \in [0, 2^{61}] such that (a\, |\, b)-(a\, \&\, c)=d , where | and \& denote the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR) and the [bitwise AND operation](https://en.wikipedia.org/wiki/Bitwise_operation#AND), respectively.

If such an a exists, print its value. If there is no solution, print a single
integer -1 . If there are multiple solutions, print any of them.

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 10^5 ). The description of the test cases follows.

The only line of each test case contains three positive integers b , c , and d
(0 \le b, c, d \le 10^{18} ).

Output

For each test case, output the value of a , or -1 if there is no solution.
Please note that a must be non-negative and cannot exceed 2^{61} .

Example

Input

    3
    
    2 2 2
    
    4 2 6
    
    10 2 14

Output

    0
    -1
    12
    
Note

In the first test case, (0\,|\,2)-(0\,\&\,2)=2-0=2 . So, a = 0 is a correct
answer.

In the second test case, no value of a satisfies the equation.

In the third test case, (12\,|\,10)-(12\,\&\,2)=14-0=14 . So, a = 12 is a
correct answer.
