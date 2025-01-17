Vladislav has a grid of size 7 \times 7 , where each cell is colored black or
white. In one operation, he can choose any cell and change its color (black
\leftrightarrow white).

Find the minimum number of operations required to ensure that there are no
black cells with four diagonal neighbors also being black.

![](https://espresso.codeforces.com/942fdd5f886d1c58b608e2a8c552064f636e4aa0.png)

The left image shows that initially there are two black cells violating the
condition. By flipping one cell, the grid will work.

Input

The first line of input contains a single integer t (1 \leq t \leq 200 ) — the
number of test cases. Then follows the description of the test cases.

Each test case consists of 7 lines, each containing 7 characters. Each of
these characters is either \texttt{W} or \texttt{B} , denoting a white or
black cell, respectively.

Output

For each test case, output a single integer — the minimum number of operations
required to ensure that there are no black cells with all four diagonal
neighbors also being black.

Example

Input

    4
    
    WWWWWWW
    
    WWWWBBB
    
    WWWWWBW
    
    WWBBBBB
    
    WWWBWWW
    
    WWBBBWW
    
    WWWWWWW
    
    WWWWWWW
    
    WWWWWWW
    
    WBBBBBW
    
    WBBBBBW
    
    WBBBBBW
    
    WWWWWWW
    
    WWWWWWW
    
    WWWWWWW
    
    WWWWWWW
    
    WWWWWWW
    
    WWWWWWW
    
    WWWWWWW
    
    WWWWWWW
    
    WWWWWWW
    
    WBBBBBW
    
    BBBBBBB
    
    BBBBBBB
    
    WWWWWWW
    
    BBBBBBB
    
    BBBBBBB
    
    BBBBBBB

Output

    1
    2
    0
    5
    
Note

The first test case is illustrated in the statement.

The second test case is illustrated below:

![](https://espresso.codeforces.com/5b4e010f2db30aa44997d12bbd4620f739c5b139.png)

In the third test case, the grid already satisfies the condition.
