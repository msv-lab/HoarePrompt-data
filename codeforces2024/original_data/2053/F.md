3, 2, 1, ... We are the — RiOI Team!

— Felix & All, [Special Thanks 3](https://www.luogu.com.cn/problem/T351681)

  * Peter: Good news: My problem T311013 is approved!
  * \delta : I'm glad my computer had gone out of battery so that I wouldn't have participated in wyrqwq's round and gained a negative delta.
  * Felix: [thumbs_up] The problem statement concerning a removed song!
  * Aquawave: Do I mourn my Chemistry?
  * E.Space: ahh?
  * Trine: Bread.
  * Iris: So why am I always testing problems?

Time will pass, and we might meet again. Looking back at the past, everybody
has lived the life they wanted.

Aquawave has a matrix A of size n\times m , whose elements can only be
integers in the range [1, k] , inclusive. In the matrix, some cells are
already filled with an integer, while the rest are currently not filled,
denoted by -1 .

You are going to fill in all the unfilled places in A . After that, let
c_{u,i} be the number of occurrences of element u in the i -th row. Aquawave
defines the beauty of the matrix as

You have to find the maximum possible beauty of A after filling in the blanks
optimally.

Input

The first line of input contains a single integer t (1 \leq t \leq 2\cdot 10^4
) — the number of test cases. The description of test cases follows.

The first line of each test case contains three integers n , m , and k (2 \leq
n \leq 2\cdot 10^5 , 2 \leq m \leq 2\cdot 10^5 , n \cdot m \leq 6\cdot 10^5 ,
1 \leq k \leq n\cdot m ) — the number of rows and columns of the matrix A ,
and the range of the integers in the matrix, respectively.

Then n lines follow, the i -th line containing m integers
A_{i,1},A_{i,2},\ldots,A_{i,m} (1 \leq A_{i,j} \leq k or A_{i,j} = -1 ) — the
elements in A .

It is guaranteed that the sum of n\cdot m over all test cases does not exceed
6\cdot 10^5 .

Output

For each test case, output a single integer — the maximum possible beauty.

Example

Input

    9
    
    3 3 3
    
    1 2 2
    
    3 1 3
    
    3 2 1
    
    2 3 3
    
    -1 3 3
    
    2 2 -1
    
    3 3 6
    
    -1 -1 1
    
    1 2 -1
    
    -1 -1 4
    
    3 4 5
    
    1 3 2 3
    
    -1 -1 2 -1
    
    3 1 5 1
    
    5 3 8
    
    5 -1 2
    
    1 8 -1
    
    -1 5 6
    
    7 7 -1
    
    4 4 4
    
    6 6 5
    
    -1 -1 5 -1 -1 -1
    
    -1 -1 -1 -1 2 -1
    
    -1 1 3 3 -1 -1
    
    -1 1 -1 -1 -1 4
    
    4 2 -1 -1 -1 4
    
    -1 -1 1 2 -1 -1
    
    6 6 4
    
    -1 -1 -1 -1 1 -1
    
    3 -1 2 2 4 -1
    
    3 1 2 2 -1 -1
    
    3 3 3 3 -1 2
    
    -1 3 3 -1 1 3
    
    3 -1 2 2 3 -1
    
    5 5 3
    
    1 1 3 -1 1
    
    2 2 -1 -1 3
    
    -1 -1 -1 2 -1
    
    3 -1 -1 -1 2
    
    -1 1 2 3 -1
    
    6 2 7
    
    -1 7
    
    -1 6
    
    7 -1
    
    -1 -1
    
    -1 -1
    
    2 2

Output

    4
    4
    10
    10
    8
    102
    93
    58
    13
    
Note

In the first test case, the matrix A is already determined. Its beauty is

In the second test case, one can fill the matrix as follows:

and get the value 4 . It can be proven this is the maximum possible answer one
can get.

In the third test case, one of the possible optimal configurations is:

In the fourth test case, one of the possible optimal configurations is:

In the fifth test case, one of the possible optimal configurations is:
