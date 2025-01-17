Sakurako has a box with n balls. Each ball has it's value. She wants to bet
with her friend that if the friend randomly picks two balls from the box (it
could be two distinct balls, but they may have the same value), the product of
their values will be the same as the number that Sakurako guessed.

Since Sakurako has a PhD in probability, she knows that the best number to
pick is [the expected value](http://tiny.cc/matozh_en), but she forgot how to
calculate it. Help Sakurako and find the expected value of the product of two
elements from the array.

It can be shown that the expected value has the form \frac{P}{Q} , where P and
Q are non-negative integers, and Q \ne 0 . Report the value of P \cdot
Q^{-1}(\bmod 10^9+7) .

Input

The first line contains a single integer t (1\le t\le 10^4 ) — the number of
test cases.

The first line of each test case contains a single integer n (2\le n\le 2\cdot
10^5 ) — the number of elements in the array.

The second line of each test case contains n integers a_1, a_2, \dots, a_n
(0\le a_i\le 10^9 ) — the elements of the array.

It is guaranteed that the sum of n across all test cases does not exceed
2\cdot 10^5 .

Output

For each test case, output the value of P \cdot Q^{-1}(\bmod 10^9+7) .

Example

Input

    3
    
    3
    
    3 2 3
    
    4
    
    2 2 2 4
    
    5
    
    1 2 3 4 5

Output

    7
    6
    500000012
    
Note

For the first test, Sakurako's friend can pick these pairs of balls: (a_1,a_2)
, (a_1,a_3) , (a_2,a_3) . Their products equal to 3\cdot 2=6 , 3\cdot 3=9 ,
3\cdot 2=6 respectively, so the expected value is \frac{6+9+6}{3}=7 .

For the second test, Sakurako's friend can pick these pairs of balls:
(a_1,a_2) , (a_1,a_3) , (a_1,a_4) , (a_2,a_3) , (a_2,a_4) , (a_3,a_4) . Their
products equal to 2\cdot 2=4 , 2\cdot 2=4 , 2\cdot 4=8 , 2\cdot 2=4 , 2\cdot
4=8 , 2\cdot 4=8 respectively, so the expected value is
\frac{4+4+8+4+8+8}{6}=\frac{36}{6}=6 .
