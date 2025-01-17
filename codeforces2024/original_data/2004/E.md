Two players, Alice and Bob, are playing a game. They have n piles of stones,
with the i -th pile initially containing a_i stones.

On their turn, a player can choose any pile of stones and take any positive
number of stones from it, with one condition:

  * let the current number of stones in the pile be x . It is not allowed to take from the pile a number of stones y such that the greatest common divisor of x and y is not equal to 1 . 

The player who cannot make a move loses. Both players play optimally (that is,
if a player has a strategy that allows them to win, no matter how the opponent
responds, they will win). Alice goes first.

Determine who will win.

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

Each test case consists of two lines:

  * the first line contains a single integer n (1 \le n \le 3 \cdot 10^5 ); 
  * the second line contains n integers a_1, a_2, \dots, a_n (1 \le a_i \le 10^7 ). 

Additional constraint on the input: the sum of n across all test cases does
not exceed 3 \cdot 10^5 .

Output

For each test case, output Alice if Alice wins, or Bob if Bob wins.

Example

Input

    3
    
    3
    
    3 2 9
    
    4
    
    3 3 6 1
    
    5
    
    1 2 3 4 5

Output

    Bob
    Alice
    Bob
    