Suppose you play a game where the game field looks like a strip of 1 \times
10^9 square cells, numbered from 1 to 10^9 .

You have n snakes (numbered from 1 to n ) you need to place into some cells.
Initially, each snake occupies exactly one cell, and you can't place more than
one snake into one cell. After that, the game starts.

The game lasts for q seconds. There are two types of events that may happen
each second:

  * snake s_i enlarges: if snake s_i occupied cells [l, r] , it enlarges to a segment [l, r + 1] ; 
  * snake s_i shrinks: if snake s_i occupied cells [l, r] , it shrinks to a segment [l + 1, r] . 

Each second, exactly one of the events happens.

If at any moment of time, any snake runs into some obstacle (either another
snake or the end of the strip), you lose. Otherwise, you win with the score
equal to the maximum cell occupied by any snake so far.

What is the minimum possible score you can achieve?

Input

The first line contains two integers n and q (1 \le n \le 20 ; 1 \le q \le 2
\cdot 10^5 ) — the number of snakes and the number of events. Next q lines
contain the description of events — one per line.

The i -th line contains

  * either "s_i +" (1 \le s_i \le n ) meaning that the s_i -th snake enlarges 
  * or "s_i -" (1 \le s_i \le n ) meaning that the s_i -th snake shrinks. 

Additional constraint on the input: the given sequence of events is valid, i.
e. a snake of length 1 never shrinks.

Output

Print one integer — the minimum possible score.

Examples

Input

    3 6
    
    1 +
    
    1 -
    
    3 +
    
    3 -
    
    2 +
    
    2 -

Output

    4
    
Input

    5 13
    
    5 +
    
    3 +
    
    5 -
    
    2 +
    
    4 +
    
    3 +
    
    5 +
    
    5 -
    
    2 +
    
    3 -
    
    3 +
    
    3 -
    
    2 +

Output

    11
    
Note

In the first test, the optimal strategy is to place the second snake at cell 1
, the third snake — at 2 , and the first one — at 3 . The maximum occupied
cell is cell 4 , and it's the minimum possible score.

In the second test, one of the optimal strategies is to place:

  * snake 2 at position 1 ; 
  * snake 3 at position 4 ; 
  * snake 5 at position 6 ; 
  * snake 1 at position 9 ; 
  * snake 4 at position 10 . 
