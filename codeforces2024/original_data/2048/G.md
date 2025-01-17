Kevin has been transported to Sacred Heart Hospital, which contains all the n
\times m matrices with integer values in the range [1,v] .

Now, Kevin wants to befriend some matrices, but he is willing to befriend a
matrix a if and only if the following condition is satisfied:

Please count how many matrices in Sacred Heart Hospital can be friends with
Kevin.

Since Kevin is very friendly, there could be many matrices that meet this
condition. Therefore, you only need to output the result modulo 998\,244\,353
.

Input

Each test contains multiple test cases. The first line contains the number of
test cases t ( 1 \le t \le 8\cdot 10^3 ).

The only line of each test case contains three integers n , m , v ( 1 \le n,
v, n \cdot v \leq 10^6 , 1 \le m \le 10^9 ).

It is guaranteed that the sum of n \cdot v over all test cases doesn't exceed
10^6 .

Output

For each test case, output one integer — the number of matrices that can be
friends with Kevin modulo 998\,244\,353 .

Example

Input

    3
    
    2 2 2
    
    2 3 4
    
    11 45 14

Output

    14
    2824
    883799966
    
Note

In the first test case, besides the matrices
a=\begin{bmatrix}1&2\\\2&1\end{bmatrix} and
a=\begin{bmatrix}2&1\\\1&2\end{bmatrix} , which do not satisfy the condition,
the remaining 2^{2 \cdot 2} - 2 = 14 matrices can all be friends with Kevin.
