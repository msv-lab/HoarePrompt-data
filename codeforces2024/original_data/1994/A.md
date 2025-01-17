Petr, watching Sergey's stream, came up with a matrix a , consisting of n rows
and m columns (the number in the i -th row and j -th column is denoted as
a_{i, j} ), which contains all integers from 1 to n \cdot m . But he didn't
like the arrangement of the numbers, and now he wants to come up with a new
matrix b , consisting of n rows and m columns, which will also contain all
integers from 1 to n \cdot m , such that for any 1 \leq i \leq n, 1 \leq j
\leq m it holds that a_{i, j} \ne b_{i, j} .

You are given the matrix a , construct any matrix b that meets Petr's
requirements, or determine that it is impossible.

Hurry up! Otherwise, he will donate all his money to the stream in search of
an answer to his question.

Input

Each test consists of multiple test cases. The first line contains an integer
t (1 \leq t \leq 10^3 ) — the number of test cases. Then follows the
description of the test cases.

The first line of each test case contains two integers n and m (1 \leq n, m
\leq 10 ) — the number of rows and columns of matrix a .

The next n lines contain m integers each, describing matrix a . The i -th of
these lines contains the elements of matrix a_{i, 1}, a_{i, 2}, \ldots, a_{i,
m} .

It is guaranteed that all numbers in matrix a are distinct and 1 \leq a_{i, j}
\leq n \cdot m .

It is guaranteed that the sum of n \cdot m over all test cases does not exceed
5 \cdot 10^4 .

Output

For each test case, output n \cdot m integers — any suitable matrix b , or -1
if such a matrix does not exist.

Example

Input

    5
    
    1 1
    
    1
    
    2 1
    
    2
    
    1
    
    1 5
    
    2 4 5 3 1
    
    2 4
    
    1 2 3 4
    
    5 6 7 8
    
    3 3
    
    4 2 1
    
    9 8 3
    
    6 7 5

Output

    -1
    1 
    2 
    4 5 3 1 2 
    6 7 8 5 
    2 3 4 1 
    8 3 9 
    7 5 6 
    2 1 4 
    
Note

In the first test case, there is only one element in the matrix, so matrix b
is the only matrix and it does not fit.

In the second test case a_{1, 1} = 2 \neq 1 = b_{1, 1} , a_{2, 1} = 1 \neq 2 =
b_{2, 1} .
