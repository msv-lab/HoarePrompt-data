You are given a matrix, consisting of n rows and m columns.

You can perform two types of actions on it:

  * paint the entire column in blue; 
  * paint the entire row in red. 

Note that you cannot choose which color to paint the row or column.

In one second, you can perform either one action or multiple actions at the
same time. If you perform one action, it will be free. If you perform k > 1
actions at the same time, it will cost k^2 coins. When multiple actions are
performed at the same time, for each cell affected by actions of both types,
the color can be chosen independently.

You are asked to process q queries. Before each query, all cells become
colorless. Initially, there are no restrictions on the color of any cells. In
the i -th query, a restriction of the following form is added:

  * x_i~y_i~c_i — the cell in row x_i in column y_i should be painted in color c_i . 

Thus, after i queries, there are i restrictions on the required colors of the
matrix cells. After each query, output the minimum cost of painting the matrix
according to the restrictions.

Input

The first line contains three integers n, m and q (1 \le n, m, q \le 2 \cdot
10^5 ) — the size of the matrix and the number of queries.

In the i -th of the next q lines, two integers x_i, y_i and a character c_i (1
\le x_i \le n ; 1 \le y_i \le m ; c_i \in {'R', 'B'}, where 'R' means red, and
'B' means blue) — description of the i -th restriction. The cells in all
queries are pairwise distinct.

Output

Print q integers — after each query, output the minimum cost of painting the
matrix according to the restrictions.

Examples

Input

    2 2 4
    
    1 1 R
    
    2 2 R
    
    1 2 B
    
    2 1 B

Output

    0
    0
    0
    16
    
Input

    3 5 10
    
    1 1 B
    
    2 5 B
    
    2 2 B
    
    2 3 R
    
    2 1 B
    
    3 2 R
    
    3 3 B
    
    1 2 R
    
    1 3 B
    
    3 1 B

Output

    0
    0
    0
    0
    0
    0
    16
    16
    25
    25
    