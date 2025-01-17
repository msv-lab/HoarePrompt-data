In a game you started playing recently, there is a field that can be
represented as a rectangular grid. The field has 2 rows and n columns — 2n
cells in total.

Some cells are empty, but some are occupied by wolves. In the beginning of the
game, you have one sheep in some cell, and you'd like to save it from wolves.

Wolves will attack you at night, so you still have some time for preparation.
You have two ways to deal with wolves:

  1. You pay h coins to hunters and choose a cell occupied by a wolf. Hunters will clear the cell, eradicating the wolf in it. 
  2. You pay b coins to builders and choose an empty cell. Builders will dig a trench in the chosen cell that wolves can't cross. 

You can use both methods mentioned above any number of times and in any order.

Let's say that a wolf can reach the sheep if there is a path that starts at
the wolf's cell and finishes at the sheep's cell. This path shouldn't contain
any cells with trenches, and each two consecutive cells in the path should be
neighbors (share a side).

What is the minimum total amount of money you should pay to ensure that none
of the wolves can reach the sheep?

Input

The first line contains a single integer t (1 \le t \le 1200 ) — the number of
test cases. Next, t independent cases follow.

The first line of each test case contains three integers n , h , and b (2 \le
n \le 2 \cdot 10^5 ; 1 \le h, b \le 10^9 ) — the size of the grid and
corresponding costs.

The next two lines contain a description of the grid. The j -th character in
the i -th line is either '.', 'S' or 'W':

  * '.' means that the cell is empty; 
  * 'S' means that the cell is occupied by the sheep; there is exactly one such cell on the grid; 
  * 'W' means that the cell is occupied by a wolf. 

Additional constraints:

  * there are no wolves in cells neighboring the sheep cell; 
  * the sum of n over all test cases doesn't exceed 2 \cdot 10^5 . 

Output

For each test case, print a single integer — the minimum total amount of money
you should pay to save your sheep.

Examples

Input

    4
    
    2 3 7
    
    S.
    
    ..
    
    2 3 7
    
    S.
    
    .W
    
    2 7 3
    
    S.
    
    .W
    
    4 999999999 1000000000
    
    W.S.
    
    W..W

Output

    0
    3
    6
    2999999997
    
Input

    2
    
    6 6 7
    
    W....W
    
    W.S..W
    
    6 6 7
    
    W...WW
    
    ..S..W

Output

    21
    20
    
Note

One of the optimal strategies in the first test case of the second test can be
shown like this:

W....W| \Rightarrow | W.#..W  
---|---|---  
W.S..W| | W#S#.W  
Analogically, one of the answers for the second case is the following:  W...WW| \Rightarrow | W..#WW  
---|---|---  
..S..W| | ..S#.W  
Here, '#' means a trench and 'W' means an eradicated wolf.
