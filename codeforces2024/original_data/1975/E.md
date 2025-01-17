You are given a tree of n vertices numbered from 1 to n . Initially, all
vertices are colored white or black.

You are asked to perform q queries:

  * "u" — toggle the color of vertex u (if it was white, change it to black and vice versa). 

After each query, you should answer whether all the black vertices form a
chain. That is, there exist two black vertices such that the simple path
between them passes through all the black vertices and only the black
vertices. Specifically, if there is only one black vertex, they form a chain.
If there are no black vertices, they do not form a chain.

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1\leq t\leq 10^4 ). The description of the test cases follows.

The first line of each test case contains two integers n and q (1\leq n,q\leq
2\cdot 10^5 ).

The second line of each test case contains n integers c_1,c_2,\ldots,c_n (c_i
\in \\{ \mathtt{0}, \mathtt{1} \\} ) — the initial color of the vertices. c_i
denotes the color of vertex i where \mathtt{0} denotes the color white, and
\mathtt{1} denotes the color black.

Then n - 1 lines follow, each line contains two integers x_i and y_i (1 \le
x_i,y_i \le n ), indicating an edge between vertices x_i and y_i . It is
guaranteed that these edges form a tree.

The following q lines each contain an integer u_i (1 \le u_i \le n ),
indicating the color of vertex u_i needs to be toggled.

It is guaranteed that the sum of n and q over all test cases respectively does
not exceed 2\cdot 10^5 .

Output

For each query, output "Yes" if the black vertices form a chain, and output
"No" otherwise.

You can output "Yes" and "No" in any case (for example, strings "yEs", "yes",
"Yes" and "YES" will be recognized as a positive response).

Examples

Input

    2
    
    2 1
    
    1 0
    
    1 2
    
    1
    
    5 4
    
    1 0 0 0 0
    
    1 2
    
    1 3
    
    1 5
    
    3 4
    
    4
    
    3
    
    2
    
    5

Output

    No
    No
    Yes
    Yes
    No
    
Input

    4
    
    5 3
    
    1 1 1 1 1
    
    3 5
    
    2 5
    
    3 4
    
    1 5
    
    1
    
    1
    
    1
    
    4 4
    
    0 0 0 0
    
    1 2
    
    2 3
    
    1 4
    
    1
    
    2
    
    3
    
    2
    
    1 1
    
    1
    
    1
    
    1 1
    
    0
    
    1

Output

    Yes
    No
    Yes
    Yes
    Yes
    Yes
    No
    No
    Yes
    
Note

In the second test case, the color of the vertices are as follows:

The initial tree:

![](https://espresso.codeforces.com/1d5d4720eb877c8be435b5769296b83e8d6f1d0d.png)

The first query toggles the color of vertex 4 :

![](https://espresso.codeforces.com/144c8f6fd1963c026d7697a15da9e9ec6688de26.png)

The second query toggles the color of vertex 3 :

![](https://espresso.codeforces.com/c8e019c4ad3f97632b1d1fdd3fc1bfe184a3fe74.png)

The third query toggles the color of vertex 2 :

![](https://espresso.codeforces.com/c28e2ac36e541e783cb5ce9e4f40782e38497b90.png)

The fourth query toggles the color of vertex 5 :

![](https://espresso.codeforces.com/247edddfe8d5f3c5ee0dbf7873dfda0fd5c025b9.png)
