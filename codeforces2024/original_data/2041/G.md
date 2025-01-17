Claire loves drawing lines. She receives a sheet of paper with an n \times n
grid and begins drawing "lines" on it. Well—the concept of a "line" here is
not what we usually think of. Claire refers each line to be a set of
consecutive vertical grid cells. When she draws a line, these cells are all
covered with black ink. Initially, all the cells are white, and drawing lines
turns some of them black. After drawing a few lines, Claire wonders: how many
ways she can color an additional white cell black so that the remaining white
cells do not form a single connected component.

Two cells are directly connected if they share an edge. Two cells x and y are
indirectly connected if there exists a sequence of cells c_0, c_1, \ldots, c_k
with k > 1 such that c_0 = x , c_k = y , and for every i \in \\{1, 2, \ldots,
k\\} the cells c_i and c_{i-1} are directly connected. A set of cells forms a
single connected component if each pair of cells in the set is either directly
or indirectly connected.

The grid has n rows and n columns, both indexed from 1 to n . Claire will draw
q lines. The i -th line is drawn in the y_i -th column, from the s_i -th row
to the f_i -th row, where s_i \leq f_i for each i \in \\{1, 2, \ldots, q\\} .
Note that the cells that are passed by at least one of the q lines are colored
black. The following figure shows an example of a 20\times 20 grid with q=67
lines. The grid cells marked with red star symbols refer to the cells such
that, if Claire colors that cell black, all white cells no longer form a
single connected component.

![](https://espresso.codeforces.com/2500599b3ae99128cfe43e4b77674cbb08176e4d.png)

You may assume that, after drawing the q lines, the remaining white cells form
a single connected component with at least three white cells.

Input

The first line contains exactly one integer t , indicating the number of test
cases. For each test case, it begins with a line containing exactly two
integers n and q . This indicates that the grid is n by n and that Claire
draws q lines on it. Then q lines follow. For each i \in \\{1, 2, \ldots, q\\}
, the i -th line among the q lines contains exactly three integers y_i , s_i ,
and f_i .

  * 1\le t \le 125 
  * 2\leq n \leq 10^9 
  * q\ge 1 ; the sum of all q values is at most 10^5 . 
  * 1\leq y_i \leq n 
  * 1\leq s_i \leq f_i \leq n 
  * There are at least three white cells and all white cells form a connected component. 

Output

Print an integer on a line, indicating how many ways Claire can color an
additional white cell black so that the remaining white cells do not form a
single connected component.

Example

Input

    2
    3 1
    2 1 2
    5 2
    2 1 4
    4 2 5
    
Output

    5
    15
    