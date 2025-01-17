ICPC Square is a hotel provided by the ICPC Committee for the accommodation of
the participants. It consists of N floors (numbered from 1 to N ). This hotel
has a very unique elevator. If a person is currently at floor x , by riding
the elevator once, they can go to floor y if and only if y is a multiple of x
and y - x \leq D .

You are currently at floor S . You want to go to the highest possible floor by
riding the elevator zero or more times. Determine the highest floor you can
reach.

Input

A single line consisting of three integers N D S (2 \leq N \leq 10^{12}; 1
\leq D \leq N - 1; 1 \leq S \leq N ).

Output

Output a single integer representing the highest floor you can reach by riding
the elevator zero or more times.

Examples

Input

    64 35 3
    
Output

    60
    
Input

    2024 2023 1273
    
Output

    1273
    
Note

Explanation for the sample input/output #1

First, ride the elevator from floor 3 to floor 15 . This is possible because
15 is a multiple of 3 and 15 - 3 \leq 35 . Then, ride the elevator from floor
15 to floor 30 . This is possible because 30 is a multiple of 15 and 30 - 15
\leq 35 . Finally, ride the elevator from floor 30 to floor 60 . This is
possible because 60 is a multiple of 30 and 60 - 30 \leq 35 .
