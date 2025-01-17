You are given a matrix a of size n \times m , consisting of integers from 0 to
31 inclusive.

Let's call the matrix strange if for every two distinct rows i and j , both of
the following conditions hold:

  * for every set of k indices (x_1, x_2, \dots, x_k) , where 1 \le x_1 < x_2 < \cdots < x_k \le m , the equality a_{i, x_1} \mathbin{\&} a_{j, x_1} \mathbin{\&} a_{i, x_2} \mathbin{\&} a_{j, x_2} \mathbin{\&} \cdots \mathbin{\&} a_{i, x_k} \mathbin{\&} a_{j, x_k} = 0 holds (where \mathbin{\&} — bitwise AND of two numbers); 
  * for every set of k indices (x_1, x_2, \dots, x_k) , where 1 \le x_1 < x_2 < \cdots < x_k \le m , the equality a_{i, x_1} \mathbin{|} a_{j, x_1} \mathbin{|} a_{i, x_2} \mathbin{|} a_{j, x_2} \mathbin{|} \cdots \mathbin{|} a_{i, x_k} \mathbin{|} a_{j, x_k} = 31 holds (where \mathbin{|} — bitwise OR of two numbers). 

You can perform the following operation any number of times: take any row of
the matrix and a number y from 0 to 31 inclusive; then apply the bitwise XOR
with the number y to all elements of the selected row. The cost of such an
operation is equal to y .

Your task is to calculate the minimum cost to make the matrix strange, or
report that it is impossible.

Input

The first line contains one integer t (1 \le t \le 100 ) — the number of test
cases.

The first line of each test case contains three integers n , m , and k (1 \le
n, m \le 50 ; 1 \le k \le m ).

Next, there are n lines, the i -th of which contains m integers a_{i, 1},
a_{i, 2}, \dots, a_{i, m} (0 \le a_{i, j} \le 31 ).

Output

For each test case, output one integer — the minimum cost to make the matrix
strange, or -1 if it is impossible to make the matrix strange.

Example

Input

    3
    
    2 3 1
    
    0 1 0
    
    1 0 1
    
    3 2 2
    
    0 1
    
    2 3
    
    4 5
    
    5 5 5
    
    0 5 17 4 22
    
    8 5 16 21 9
    
    7 25 31 30 8
    
    0 0 5 15 13
    
    1 2 3 4 5

Output

    30
    -1
    24
    