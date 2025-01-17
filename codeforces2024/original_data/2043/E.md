You are given two matrices A and B of size n \times m , filled with integers
between 0 and 10^9 . You can perform the following operations on matrix A  in
any order and any number of times:

  * &=: choose two integers i and x (1 \le i \le n , x \ge 0 ) and replace each element in row i with the result of the bitwise AND operation between x and that element. Formally, for every j \in [1, m] , the element A_{i,j} is replaced with A_{i,j} \text{ & } x ; 
  * |=: choose two integers j and x (1 \le j \le m , x \ge 0 ) and replace each element in column j with the result of the bitwise OR operation between x and that element. Formally, for every i \in [1, n] , the element A_{i,j} is replaced with A_{i,j} \text{ | } x . 

The value of x may be chosen differently for different operations.

Determine whether it is possible to transform matrix A into matrix B using the
given operations any number of times (including zero).

Input

The first line contains a single integer t (1 \le t \le 100 ) — the number of
test cases. Then, t test cases follow.

Each test case is given as follows:

  * the first line contains two integers n and m (1 \le n, m \le 10^3 ; n \cdot m \le 10^3 ) — the dimensions of the matrices A and B ; 
  * the following n lines describe the matrix A , where the i -th line contains m integers A_{i,1}, A_{i,2}, \dots, A_{i,m} (0 \le A_{i,j} \le 10^9 ); 
  * the following n lines describe the matrix B , where the i -th line contains m integers B_{i,1}, B_{i,2}, \dots, B_{i,m} (0 \le B_{i,j} \le 10^9 ). 

Output

For each test case, output Yes if it is possible to transform the matrix A
into the matrix B ; otherwise, output No. Each letter can be output in any
case, upper or lower.

Example

Input

    4
    
    1 1
    
    12
    
    13
    
    2 2
    
    10 10
    
    42 42
    
    21 21
    
    21 21
    
    2 2
    
    74 10
    
    42 106
    
    21 85
    
    85 21
    
    2 4
    
    1 2 3 4
    
    5 6 7 8
    
    3 2 3 4
    
    1 0 1 0

Output

    Yes
    Yes
    No
    Yes
    
Note

Let's consider the second set of input data and show a sequence of operations
that transforms matrix A into matrix B :

Initially, the matrix looks like this:

\begin{bmatrix} 10&10\\\ 42&42\\\ \end{bmatrix}

Apply an operation of the first type with parameters i = 1 and x = 0 . As a
result, we get the matrix:

\begin{bmatrix} 0&0\\\ 42&42\\\ \end{bmatrix}

Apply an operation of the first type with parameters i = 2 and x = 0 . As a
result, we get the matrix:

\begin{bmatrix} 0&0\\\ 0&0\\\ \end{bmatrix}

Apply an operation of the second type with parameters j = 1 and x = 21 . As a
result, we get the matrix:

\begin{bmatrix} 21&0\\\ 21&0\\\ \end{bmatrix}

Apply an operation of the second type with parameters j = 2 and x = 21 . As a
result, we get the matrix:

\begin{bmatrix} 21&21\\\ 21&21\\\ \end{bmatrix}

Thus, we have transformed matrix A into matrix B .
