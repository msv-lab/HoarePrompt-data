You are playing the Greatest Common Divisor Deck-Building Card Game (GCDDCG).
There are N cards (numbered from 1 to N ). Card i has the value of A_i , which
is an integer between 1 and N (inclusive).

The game consists of N rounds (numbered from 1 to N ). Within each round, you
need to build two non-empty decks, deck 1 and deck 2 . A card cannot be inside
both decks, and it is allowed to not use all N cards. In round i , the
greatest common divisor (GCD) of the card values in each deck must equal i .

Your creativity point during round i is the product of i and the number of
ways to build two valid decks. Two ways are considered different if one of the
decks contains different cards.

Find the sum of creativity points across all N rounds. Since the sum can be
very large, calculate the sum modulo 998\,244\,353 .

Input

The first line consists of an integer N (2 \leq N \leq 200\,000) .

The second line consists of N integers A_i (1 \leq A_i \leq N ).

Output

Output a single integer representing the sum of creativity points across all N
rounds modulo 998\,244\,353 .

Examples

Input

    3
    3 3 3
    
Output

    36
    
Input

    4
    2 2 4 4
    
Output

    44
    
Input

    9
    4 2 6 9 7 7 7 3 3
    
Output

    10858
    
Note

Explanation for the sample input/output #1

The creativity point during each of rounds 1 and 2 is 0 .

During round 3 , there are 12 ways to build both decks. Denote B and C as the
set of card numbers within deck 1 and deck 2 , respectively. The 12 ways to
build both decks are:

  * B = \\{ 1 \\}, C = \\{ 2 \\} ; 
  * B = \\{ 1 \\}, C = \\{ 3 \\} ; 
  * B = \\{ 1 \\}, C = \\{ 2, 3 \\} ; 
  * B = \\{ 2 \\}, C = \\{ 1 \\} ; 
  * B = \\{ 2 \\}, C = \\{ 3 \\} ; 
  * B = \\{ 2 \\}, C = \\{ 1, 3 \\} ; 
  * B = \\{ 3 \\}, C = \\{ 1 \\} ; 
  * B = \\{ 3 \\}, C = \\{ 2 \\} ; 
  * B = \\{ 3 \\}, C = \\{ 1, 2 \\} ; 
  * B = \\{ 1, 2 \\}, C = \\{ 3 \\} ; 
  * B = \\{ 2, 3 \\}, C = \\{ 1 \\} ; and 
  * B = \\{ 1, 3 \\}, C = \\{ 2 \\} . 

Explanation for the sample input/output #2

For rounds 1 , 2 , 3 and 4 , there are 0 , 18 , 0 , and 2 ways to build both
decks, respectively.
