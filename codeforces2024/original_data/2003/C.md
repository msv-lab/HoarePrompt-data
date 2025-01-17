Turtle gives you a string s , consisting of lowercase Latin letters.

Turtle considers a pair of integers (i, j) (1 \le i < j \le n ) to be a
pleasant pair if and only if there exists an integer k such that i \le k < j
and both of the following two conditions hold:

  * s_k \ne s_{k + 1} ; 
  * s_k \ne s_i or s_{k + 1} \ne s_j . 

Besides, Turtle considers a pair of integers (i, j) (1 \le i < j \le n ) to be
a good pair if and only if s_i = s_j or (i, j) is a pleasant pair.

Turtle wants to reorder the string s so that the number of good pairs is
maximized. Please help him!

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 10^4 ). The description of the test cases follows.

The first line of each test case contains a single integer n (2 \le n \le 2
\cdot 10^5 ) — the length of the string.

The second line of each test case contains a string s of length n , consisting
of lowercase Latin letters.

It is guaranteed that the sum of n over all test cases does not exceed 2 \cdot
10^5 .

Output

For each test case, output the string s after reordering so that the number of
good pairs is maximized. If there are multiple answers, print any of them.

Example

Input

    5
    
    3
    
    abc
    
    5
    
    edddf
    
    6
    
    turtle
    
    8
    
    pppppppp
    
    10
    
    codeforces

Output

    acb
    ddedf
    urtlet
    pppppppp
    codeforces
    
Note

In the first test case, (1, 3) is a good pair in the reordered string. It can
be seen that we can't reorder the string so that the number of good pairs is
greater than 1 . bac and cab can also be the answer.

In the second test case, (1, 2) , (1, 4) , (1, 5) , (2, 4) , (2, 5) , (3, 5)
are good pairs in the reordered string. efddd can also be the answer.
