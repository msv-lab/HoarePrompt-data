Mount ICPC can be represented as a grid of R rows (numbered from 1 to R ) and
C columns (numbered from 1 to C ). The cell located at row r and column c is
denoted as (r, c) and has a height of H_{r, c} . Two cells are adjacent to
each other if they share a side. Formally, (r, c) is adjacent to (r-1, c) ,
(r+1, c) , (r, c-1) , and (r, c+1) , if any exists.

You can move only between adjacent cells, and each move comes with a penalty.
With an aura of an odd positive integer X , moving from a cell with height h_1
to a cell with height h_2 gives you a penalty of (h_1 - h_2)^X . Note that the
penalty can be negative.

You want to answer Q independent scenarios. In each scenario, you start at the
starting cell (R_s, C_s) and you want to go to the destination cell (R_f, C_f)
with minimum total penalty. In some scenarios, the total penalty might become
arbitrarily small; such a scenario is called invalid. Find the minimum total
penalty to move from the starting cell to the destination cell, or determine
if the scenario is invalid.

Input

The first line consists of three integers R C X (1 \leq R, C \leq 1000; 1 \leq
X \leq 9; X is an odd integer).

Each of the next R lines consists of a string H_r of length C . Each character
in H_r is a number from 0 to 9. The c -th character of H_r represents the
height of cell (r, c) , or H_{r, c} .

The next line consists of an integer Q (1 \leq Q \leq 100\,000) .

Each of the next Q lines consists of four integers R_s C_s R_f C_f (1 \leq
R_s, R_f \leq R; 1 \leq C_s, C_f \leq C ).

Output

For each scenario, output the following in a single line. If the scenario is
invalid, output INVALID. Otherwise, output a single integer representing the
minimum total penalty to move from the starting cell to the destination cell.

Examples

Input

    3 4 1
    3359
    4294
    3681
    5
    1 1 3 4
    3 3 2 1
    2 2 1 4
    1 3 3 2
    1 1 1 1
    
Output

    2
    4
    -7
    -1
    0
    
Input

    2 4 5
    1908
    2023
    2
    1 1 2 4
    1 1 1 1
    
Output

    INVALID
    INVALID
    
Input

    3 3 9
    135
    357
    579
    2
    3 3 1 1
    2 2 2 2
    
Output

    2048
    0
    
Note

Explanation for the sample input/output #1

For the first scenario, one of the solutions is to move as follows: (1, 1)
\rightarrow (2, 1) \rightarrow (3, 1) \rightarrow (3, 2) \rightarrow (3, 3)
\rightarrow (3, 4) . The total penalty of this solution is (3 - 4)^1 + (4 -
3)^1 + (3 - 6)^1 + (6 - 8)^1 + (8 - 1)^1 = 2 .

Explanation for the sample input/output #2

For the first scenario, the cycle (1, 1) \rightarrow (2, 1) \rightarrow (2, 2)
\rightarrow (1, 2) \rightarrow (1, 1) has a penalty of (1 - 2)^5 + (2 - 0)^5 +
(0 - 9)^5 + (9 - 1)^5 = -26250 . You can keep repeating this cycle to make
your total penalty arbitrarily small. Similarly, for the second scenario, you
can move to (1, 1) first, then repeat the same cycle.
