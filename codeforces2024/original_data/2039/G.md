Shohag has a tree with n nodes.

Pebae has an integer m . She wants to assign each node a value — an integer
from 1 to m . So she asks Shohag to count the number, modulo 998\,244\,353 ,
of assignments such that following conditions are satisfied:

  * For each pair 1 \le u \lt v \le n , the [least common multiple (LCM)](https://en.wikipedia.org/wiki/Least_common_multiple) of the values of the nodes in the unique simple path from u to v is not divisible by the number of nodes in the path. 
  * The [greatest common divisor (GCD)](https://en.wikipedia.org/wiki/Greatest_common_divisor) of the values of all nodes from 1 to n is 1 . 

But this problem is too hard for Shohag to solve. As Shohag loves Pebae, he
has to solve the problem. Please save Shohag!

Input

The first line contains two space-separated integers n and m (2 \le n \le 10^6
, 1 \le m \le 10^{9} ).

Each of the next n - 1 lines contains two integers u and v (1 \le u, v \le n )
indicating there is an edge between vertices u and v . It is guaranteed that
the given edges form a tree.

Output

Print a single integer — the number of valid ways to assign each vertex a
value, modulo 998\,244\,353 .

Examples

Input

    6 6
    
    1 2
    
    2 3
    
    3 4
    
    4 5
    
    3 6

Output

    2
    
Input

    2 5
    
    1 2

Output

    7
    
Input

    12 69
    
    3 5
    
    1 4
    
    2 3
    
    4 5
    
    5 6
    
    8 9
    
    7 3
    
    4 8
    
    9 10
    
    1 11
    
    12 1

Output

    444144548
    
Note

In the first test case, the valid assignments are [1, 1, 1, 1, 1, 1] and [1,
1, 1, 1, 1, 5] .

In the second test case, the valid assignments are [1, 1] , [1, 3] , [1, 5] ,
[3, 1] , [3, 5] , [5, 1] and [5, 3] .
