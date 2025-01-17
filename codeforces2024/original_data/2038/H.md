Monocarp plays a computer game. In this game, he maintains a space empire. The
empire is governed by n political parties. Initially, every party has
political power equal to 0 , and there is no ruling party.

During each of the next m turns, the following happens:

  1. initially, Monocarp has to choose which party he supports. He can support any party, except for the ruling party. When Monocarp supports a party, its political power is increased by 1 . If Monocarp supports the i -th party during the j -th turn, his score increases by a_{i,j} points; 
  2. then, the elections happen, and the party with the maximum political power is chosen as the ruling party (if there are multiple such parties, the party with the lowest index among them is chosen). The former ruling party is replaced, unless it is chosen again; 
  3. finally, an event happens. At the end of the j -th turn, the party p_j must be the ruling party to prevent a bad outcome of the event, otherwise Monocarp loses the game. 

Determine which party Monocarp has to support during each turn so that he
doesn't lose the game due to the events, and the score he achieves is the
maximum possible. Initially, Monocarp's score is 0 .

Input

The first line contains two integers n and m (2 \le n, m \le 50 ) — the number
of political parties and the number of turns, respectively.

The second line contains m integers p_1, p_2, \dots, p_m (1 \le p_j \le n ),
where p_j is the index of the party which should be the ruling party at the
end of the j -th turn.

Then n lines follow. The i -th of them contains m integers a_{i,1}, a_{i,2},
\dots, a_{i,m} (1 \le a_{i,j} \le 10^5 ), where a_{i,j} is the amount of
points Monocarp gets if he supports the i -th party during the j -th turn.

Output

If Monocarp loses the game no matter how he acts, print one integer -1 .

Otherwise, print m integers c_1, c_2, \dots, c_m (1 \le c_j \le n ), where c_j
is the index of the party Monocarp should support during the j -th turn. If
there are multiple answers, print any of them.

Examples

Input

    2 3
    
    2 1 2
    
    1 2 3
    
    4 5 6

Output

    2 1 2 
    
Input

    3 5
    
    1 1 1 2 1
    
    1 1 1 1 1
    
    10 5 7 8 15
    
    7 10 9 8 15

Output

    1 3 2 2 1 
    
Input

    3 5
    
    1 1 1 1 1
    
    1 1 1 1 1
    
    10 5 7 8 15
    
    7 10 9 8 15

Output

    -1
    