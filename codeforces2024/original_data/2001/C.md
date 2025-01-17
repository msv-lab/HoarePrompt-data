This is an interactive problem.

Misuki has chosen a secret tree with n nodes, indexed from 1 to n , and asked
you to guess it by using queries of the following type:

  * "? a b" — Misuki will tell you which node x minimizes |d(a,x) - d(b,x)| , where d(x,y) is the distance between nodes x and y . If more than one such node exists, Misuki will tell you the one which minimizes d(a,x) . 

Find out the structure of Misuki's secret tree using at most 15n queries!

Input

Each test consists of multiple test cases. The first line contains a single
integer t (1 \le t \le 200 ) — the number of test cases.

Each test case consists of a single line with an integer n (2 \le n \le 1000
), the number of nodes in the tree.

It is guaranteed that the sum of n across all test cases does not exceed 1000
.

Interaction

The interaction begins by reading the integer n .

Then you can make up to 15n queries.

To make a query, output a line in the format "? a b" (without quotes) (1 \le
a,b \le n ). After each query, read an integer — the answer to your query.

To report the answer, output a line in the format "! a_1 b_1 a_2 b_2 ...
a_{n-1} b_{n-1} " (without quotes), meaning that there is an edge between
nodes a_i and b_i , for each 1 \le i \le n-1 . You can print the edges in any
order.

After 15n queries have been made, the response to any other query will be -1 .
Once you receive such a response, terminate the program to receive the Wrong
Answer verdict.

After printing each line, do not forget to output the end of line and flush
the output buffer. Otherwise, you will receive the Idleness limit exceeded
verdict. To flush, use:

  * fflush(stdout) or cout.flush() in C++;
  * System.out.flush() in Java;
  * flush(output) in Pascal;
  * stdout.flush() in Python;
  * see the documentation for other languages.

Hacks

For hacks, use the following format: The first line contains an integer t (1
\le t \le 200 ) — the number of test cases.

The first line of each test contains an integer n — the number of nodes in the
hidden tree.

Then n-1 lines follow. The i -th of them contains two integers a_i and b_i (1
\le a_i, b_i \le n ), meaning that there is an edge between a_i and b_i in the
hidden tree.

The sum of n over all test cases must not exceed 1000 .

Example

Input

    1
    4
    1
    1
    3

Output

    ? 1 2
    
    ? 1 3
    
    ? 1 4
    
    ! 1 2 1 3 3 4

Note

A tree is an undirected acyclic connected graph. A tree with n nodes will
always have n-1 edges.

In the example case, the answer to "? 1 2" is 1 . This means that there is an
edge between nodes 1 and 2 .

The answer to "? 1 3" is 1 . This means that there is an edge between nodes 1
and 3 .

The answer to "? 1 4" is 3 . It can be proven that this can only happen if
node 3 is connected to both node 1 and 4 .

The edges of the tree are hence (1,2) , (1,3) and (3,4) .
