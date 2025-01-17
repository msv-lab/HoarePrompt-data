Given a tree^{\text{∗}} with n vertices. You can choose two vertices a and b
once and remove all vertices on the path from a to b , including the vertices
themselves. If you choose a=b , only one vertex will be removed.

Your task is to find the maximum number of connected components^{\text{†}}
that can be formed after removing the path from the tree.

^{\text{∗}} A tree is a connected graph without cycles.

^{\text{†}} A connected component is a set of vertices such that there is a
path along the edges from any vertex to any other vertex in the set (and it is
not possible to reach vertices not belonging to this set)

Input

The first line of the input contains one integer t (1 \le t \le 10^4 ) — the
number of test cases.

The first line of each test case contains one integer n (2 \le n \le 2 \cdot
10^5 ) — the size of the tree.

The next n-1 lines contain two integers u and v (1 \le u, v \le n , u \ne v )
— the vertices connected by an edge. It is guaranteed that the edges form a
tree.

It is guaranteed that the sum of n across all test cases does not exceed 2
\cdot 10^5 .

Output

For each test case, output one integer — the maximum number of connected
components that can be achieved using the described operation.

Example

Input

    6
    
    2
    
    1 2
    
    5
    
    1 2
    
    2 3
    
    3 4
    
    3 5
    
    4
    
    1 2
    
    2 3
    
    3 4
    
    5
    
    2 1
    
    3 1
    
    4 1
    
    5 4
    
    6
    
    2 1
    
    3 1
    
    4 1
    
    5 3
    
    6 3
    
    6
    
    2 1
    
    3 2
    
    4 2
    
    5 3
    
    6 4

Output

    1
    3
    2
    3
    4
    3
    