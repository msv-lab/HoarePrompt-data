Rock-Paper-Scissors is a game for two players. It is played in rounds. During
each round, every player chooses one of three moves: Rock, Paper, or Scissors.
Depending on the chosen moves, the following happens:

  * if one player chooses Rock and the other player chooses Paper, the player who chooses Paper wins and gets a point; 
  * if one player chooses Scissors and the other player chooses Paper, the player who chooses Scissors wins and gets a point; 
  * if one player chooses Scissors and the other player chooses Rock, the player who chooses Rock wins and gets a point; 
  * and if both players choose the same move, nobody wins and nobody gets a point. 

Monocarp decided to play against a bot. During the game, Monocarp noticed that
the bot's behavior is very predictable:

  * in the first round, it chooses Rock; 
  * in every round except the first, it chooses the move that beats the opponent's move in the previous round (for example, if in the previous round its opponent played Scissors, then the bot chooses Rock now). 

Monocarp has a favorite string s , consisting of the characters R, P, and/or
S. Monocarp decided to play a series of rounds against the bot. However, he
wants both of the following conditions to be met:

  * the final score is in favor of Monocarp (i. e., the number of rounds he won is strictly greater than the number of rounds the bot won); 
  * the string s appears as a contiguous substring in the sequence of the bot's moves (where R denotes Rock, P denotes Paper, and S denotes Scissors). 

Help Monocarp and calculate the minimum number of rounds he needs to play
against the bot to satisfy both of the aforementioned conditions.

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

The only line of each test case contains a string s (1 \le |s| \le 2 \cdot
10^5 ), consisting of the characters R, P, and/or S.

Additional constraint on the input: the sum of the lengths of the strings s
over all test cases does not exceed 2 \cdot 10^5 .

Output

For each test case, print a single integer — the minimum number of rounds
Monocarp needs to play against the bot to satisfy both of the aforementioned
conditions.

Example

Input

    7
    
    SS
    
    R
    
    RPS
    
    RPPP
    
    SPPRSP
    
    PPP
    
    PR

Output

    3
    1
    3
    6
    7
    5
    3
    
Note

In the first example, Monocarp can play PPR, then the bot's moves are RSS, and
the score is 2:1 in favor of Monocarp.

In the second example, Monocarp can play P, then the bot's moves are R, and
the score is 1:0 in favor of Monocarp.

In the third example, Monocarp can play RPR, then the bot's moves are RPS, and
the score is 1:0 in favor of Monocarp.

In the fourth example, Monocarp can play RRRSPR, then the bot's moves are
RPPPRS, and the score is 3:2 in favor of Monocarp.

In the fifth example, Monocarp can play PRRSPRS, then the bot's moves are
RSPPRSP, and the score is 6:1 in favor of Monocarp.

In the sixth example, Monocarp can play PRRRS, then the bot's moves are RSPPP,
and the score is 3:2 in favor of Monocarp.

In the seventh example, Monocarp can play RSR, then the bot's moves are RPR,
and the score is 1:0 in favor of Monocarp.
