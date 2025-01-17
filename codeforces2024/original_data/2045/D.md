You live in an archipelago consisting of N islands (numbered from 1 to N )
laid out in a single line. Island i is adjacent to island i+1 , for 1 \leq i <
N . Between adjacent islands i and i+1 , there is a pair of one-directional
underwater tunnels: one that allows you to walk from island i to island i+1
and one for the opposite direction. Each tunnel can only be traversed at most
once.

You also have a dragon with you. It has a stamina represented by a non-
negative integer. The stamina is required for the dragon to perform its
abilities: swim and fly. Initially, its stamina is 0 .

Your dragon's stamina can be increased as follows. There is a magical shrine
on each island i that will immediately increase your dragon's stamina by P_i
(regardless the position of the dragon) when you visit island i for the first
time. This event takes no time.

When you are on an island, there are 3 moves that you can perform.

  * Swim with your dragon to an adjacent island if your dragon and you are on the same island. You can perform if your dragon's stamina is at least D . This move reduces your dragon's stamina by D , and it takes T_s seconds to perform. 
  * Fly with your dragon to an adjacent island if your dragon and you are on the same island. You can perform this move if your dragon's stamina is not 0 . This move sets your dragon's stamina to 0 , and it takes T_f seconds to perform. 
  * Walk alone without your dragon to an adjacent island through the underwater tunnel. This move takes T_w seconds to perform. Once you walk through this tunnel, it cannot be used again. 

Note that both swimming and flying do not use tunnels.

Your dragon and you are currently on island 1 . Your mission is to go to
island N with your dragon. Determine the minimum possible time to complete
your mission.

Input

The first line consists of five integers N D T_s T_f T_w (2 \leq N \leq
200\,000; 1 \leq D, T_s, T_f, T_w \leq 200\,000 ).

The second line consists of N integers P_i (1 \leq P_i \leq 200\,000) .

Output

Output an integer in a single line representing the minimum possible time to
go to island N with your dragon.

Examples

Input

    5 4 2 9 1
    1 2 4 2 1
    
Output

    28
    
Input

    5 4 2 1 1
    1 2 4 2 1
    
Output

    4
    
Input

    3 4 2 10 1
    3 1 2
    
Output

    16
    
Note

Explanation for the sample input/output #1

The following sequence of events will complete your mission in the minimum
time.

  1. The shrine on island 1 increases your dragon's stamina to 1 . 
  2. Fly with your dragon to island 2 . The shrine on island 2 increases your dragon's stamina to 2 . 
  3. Walk alone to island 3 . The shrine on island 3 increases your dragon's stamina to 6 . 
  4. Walk alone to island 4 . The shrine on island 4 increases your dragon's stamina to 8 . 
  5. Walk alone to island 3 . 
  6. Walk alone to island 2 . 
  7. Swim with your dragon to island 3 . Your dragon's stamina is now 4 . 
  8. Swim with your dragon to island 4 . Your dragon's stamina is now 0 . 
  9. Walk alone to island 5 . The shrine on island 5 increases your dragon's stamina to 1 . 
  10. Walk alone to island 4 . 
  11. Fly with your dragon to island 5 . 

Explanation for the sample input/output #2

Repeat the following process for 1 \leq i < 5 : The shrine on island i
increases your dragon's stamina, then use the stamina to fly with your dragon
to island i+1 .
