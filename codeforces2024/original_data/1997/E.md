Monocarp is playing a computer game. He starts the game being level 1 . He is
about to fight n monsters, in order from 1 to n . The level of the i -th
monster is a_i .

For each monster in the given order, Monocarp's encounter goes as follows:

  * if Monocarp's level is strictly higher than the monster's level, the monster flees (runs away); 
  * otherwise, Monocarp fights the monster. 

After every k -th fight with a monster (fleeing monsters do not count),
Monocarp's level increases by 1 . So, his level becomes 2 after k monsters he
fights, 3 after 2k monsters, 4 after 3k monsters, and so on.

You need to process q queries of the following form:

  * i~x : will Monocarp fight the i -th monster (or will this monster flee) if the parameter k is equal to x ? 

Input

The first line contains two integers n and q (1 \le n, q \le 2 \cdot 10^5 ) —
the number of monsters and the number of queries.

The second line contains n integers a_1, a_2, \dots, a_n (1 \le a_i \le 2
\cdot 10^5 ) — the levels of the monsters.

In the j -th of the following q lines, two integers i and x (1 \le i, x \le n
) — the index of the monster and the number of fights required for a level up
in the j -th query.

Output

For each query, output "YES", if Monocarp will fight the i -th monster in this
query, and "NO", if the i -th monster flees.

Examples

Input

    4 16
    
    2 1 2 1
    
    1 1
    
    2 1
    
    3 1
    
    4 1
    
    1 2
    
    2 2
    
    3 2
    
    4 2
    
    1 3
    
    2 3
    
    3 3
    
    4 3
    
    1 4
    
    2 4
    
    3 4
    
    4 4

Output

    YES
    NO
    YES
    NO
    YES
    YES
    YES
    NO
    YES
    YES
    YES
    NO
    YES
    YES
    YES
    YES
    
Input

    7 15
    
    1 1 2 1 1 1 1
    
    5 3
    
    2 2
    
    2 2
    
    1 6
    
    5 1
    
    5 5
    
    7 7
    
    3 5
    
    7 4
    
    4 3
    
    2 5
    
    1 2
    
    5 6
    
    4 1
    
    6 1

Output

    NO
    YES
    YES
    YES
    NO
    YES
    YES
    YES
    NO
    NO
    YES
    YES
    YES
    NO
    NO
    