Recall the rules of the game "Nim". There are n piles of stones, where the i
-th pile initially contains some number of stones. Two players take turns
choosing a non-empty pile and removing any positive (strictly greater than 0 )
number of stones from it. The player unable to make a move loses the game.

You are given an array a , consisting of n integers. Artem and Ruslan decided
to play Nim on segments of this array. Each of the q rounds is defined by a
segment (l_i, r_i) , where the elements a_{l_i}, a_{l_i+1}, \dots, a_{r_i}
represent the sizes of the piles of stones.

Before the game starts, Ruslan can remove any number of piles from the chosen
segment. However, at least one pile must remain, so in a single round he can
remove at most (r_i - l_i) piles. He is allowed to remove 0 piles. After the
removal, the game is played on the remaining piles within the segment.

All rounds are independent: the changes made in one round do not affect the
original array or any other rounds.

Ruslan wants to remove as many piles as possible so that Artem, who always
makes the first move, loses.

For each round, determine:

  1. the maximum number of piles Ruslan can remove; 
  2. the number of ways to choose the maximum number of piles for removal. 

Two ways are considered different if there exists an index i such that the
pile at index i is removed in one way but not in the other. Since the number
of ways can be large, output it modulo 998\,244\,353 .

If Ruslan cannot ensure Artem's loss in a particular round, output -1 for that
round.

Input

The first line of input contains two integers n and q (1 \le n, q \le 10^5 ) —
the size of the array and the number of segments for which the answers need to
be calculated.

The second line of input contains n integers a_1, a_2, \dots, a_n (0 \le a_i
\le 50 ) — the elements of the initial array.

The i -th of the next q lines contains two integers l_i, r_i (1 \le l_i \le
r_i \le n ) — the bounds of the segment on which the boys want to play the
game during the i -th round.

Output

For each round:

  * if Ruslan can win, print two integers — the maximum number of piles that can be removed, and the number of ways to remove the maximum number of piles, taken modulo 998\,244\,353 ; 
  * otherwise print -1. 

Example

Input

    9 5
    
    0 1 2 1 3 4 5 6 0
    
    1 5
    
    2 5
    
    3 5
    
    4 5
    
    1 9

Output

    4 1
    2 1
    0 1
    -1
    8 2
    