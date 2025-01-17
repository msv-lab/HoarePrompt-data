You are given two strongly connected^{\dagger} directed graphs, each with
exactly n vertices, but possibly different numbers of edges. Upon closer
inspection, you noticed an important feature — the length of any cycle in
these graphs is divisible by k .

Each of the 2n vertices belongs to exactly one of two types: incoming or
outgoing. For each vertex, its type is known to you.

You need to determine whether it is possible to draw exactly n directed edges
between the source graphs such that the following four conditions are met:

  * The ends of any added edge lie in different graphs. 
  * From each outgoing vertex, exactly one added edge originates. 
  * Into each incoming vertex, exactly one added edge enters. 
  * In the resulting graph, the length of any cycle is divisible by k . 

^{\dagger} A strongly connected graph is a graph in which there is a path from
every vertex to every other vertex.

Input

Each test consists of multiple test cases. The first line contains a single
integer t (1 \le t \le 10^4 ) — the number of test cases. The description of
the test cases follows.

The first line of each test case contains two integers n and k (2 \le k \le n
\le 2 \cdot 10^5 ) — the number of vertices in each graph and the value by
which the length of each cycle is divisible.

The second line of each test case contains n integers a_1, a_2, \ldots, a_n
(a_i \in \\{0, 1\\} ). If a_i = 0 , then vertex i of the first graph is
incoming. If a_i = 1 , then vertex i of the first graph is outgoing.

The third line of each test case contains a single integer m_1 (1 \le m_1 \le
5 \cdot 10^5 ) — the number of edges in the first graph.

The next m_1 lines contain descriptions of the edges of the first graph. The i
-th of them contains two integers v_i and u_i (1 \le v_i, u_i \le n ) — an
edge in the first graph leading from vertex v_i to vertex u_i .

Next, in the same format, follows the description of the second graph.

The next line contains n integers b_1, b_2, \ldots, b_n (b_i \in \\{0, 1\\} ).
If b_i = 0 , then vertex i of the second graph is incoming. If b_i = 1 , then
vertex i of the second graph is outgoing.

The next line contains a single integer m_2 (1 \le m_2 \le 5 \cdot 10^5 ) —
the number of edges in the second graph.

The next m_2 lines contain descriptions of the edges of the second graph. The
i -th of them contains two integers v_i and u_i (1 \le v_i, u_i \le n ) — an
edge in the second graph leading from vertex v_i to vertex u_i .

It is guaranteed that both graphs are strongly connected, and the lengths of
all cycles are divisible by k .

It is guaranteed that the sum of n over all test cases does not exceed 2 \cdot
10^5 . It is guaranteed that the sum of m_1 and the sum of m_2 over all test
cases does not exceed 5 \cdot 10^5 .

Output

For each test case, output "YES" (without quotes) if it is possible to draw n
new edges such that all conditions are met, and "NO" (without quotes)
otherwise.

You may output the answer in any case (for example, the strings "yEs", "yes",
"Yes", and "YES" will be recognized as a positive answer).

Example

Input

    3
    
    4 2
    
    1 0 0 1
    
    4
    
    1 2
    
    2 3
    
    3 4
    
    4 1
    
    1 0 0 1
    
    4
    
    1 3
    
    3 2
    
    2 4
    
    4 1
    
    3 3
    
    0 0 0
    
    3
    
    1 2
    
    2 3
    
    3 1
    
    1 1 0
    
    3
    
    1 2
    
    2 3
    
    3 1
    
    4 2
    
    1 1 1 1
    
    4
    
    1 2
    
    2 3
    
    3 4
    
    4 1
    
    0 0 0 0
    
    6
    
    1 2
    
    2 1
    
    1 3
    
    3 1
    
    1 4
    
    4 1

Output

    YES
    NO
    YES
    
Note

In the first test case, it is possible to draw edges from the first graph to
the second graph as (1, 3) and (4, 2) (the first number in the pair is the
vertex number in the first graph, and the second number in the pair is the
vertex number in the second graph), and from the second graph to the first
graph as (1, 2) , (4, 3) (the first number in the pair is the vertex number in
the second graph, and the second number in the pair is the vertex number in
the first graph).

In the second test case, there are a total of 4 incoming vertices and 2
outgoing vertices, so it is not possible to draw 3 edges.
