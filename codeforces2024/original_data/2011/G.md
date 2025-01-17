You are given a permutation p of length n .

You can perform operations of two types:

  * mark all positions i such that 1 \le i < n and p_i < p_{i + 1} , and simultaneously remove the elements at these positions; 
  * mark all positions i such that 2 \le i \le n and p_{i - 1} > p_i , and simultaneously remove the elements at these positions. 

For each integer from 1 to (n-1) , calculate the minimum number of operations
required to remove that integer from the permutation.

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

The first line of each test case contains a single integer n (2 \le n \le
250\,000 ).

The second line of each test case contains n integers p_1, p_2, \dots, p_n (1
\le p_i \le n ). The array p is a permutation.

Additional constraints on the input: the sum of n over all test cases does not
exceed 250\,000 .

Output

For each test case, print (n-1) integers. The i -th of them should be equal to
the minimum number of operations required to remove i from the permutation.

Example

Input

    5
    
    4
    
    4 2 1 3
    
    2
    
    1 2
    
    6
    
    5 4 1 3 2 6
    
    7
    
    5 6 1 3 7 2 4
    
    5
    
    3 1 2 5 4

Output

    1 1 2
    1
    1 1 2 1 3
    1 1 1 2 1 2
    1 1 2 1
    