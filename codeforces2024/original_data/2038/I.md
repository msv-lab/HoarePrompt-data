Berland is this year's host country of the International Collegiate Polyathlon
Competition! Similar to biathlon being a competition of two sports, polyathlon
is a competition of many sports. This year, there are m sports. Also, there
are n participants in the event. The sports are numbered from 1 to m , and the
participants are numbered from 1 to n .

Some participants are skilled in multiple sports. You are given a binary
matrix n \times m such that the j -th character of the i -th row is 1 if the i
-th participant is skilled in the j -th sport, and 0, otherwise. It's also
known that, for each pair of participants, there exists at least one sport
such that one of them is skilled in that sport and the other one isn't.

The order of sports in the competition is determined at the opening ceremony.
Historically, it's done by the almighty Random Number Generator. A random
number x from 1 to m is rolled. The competition then starts with the sport x ,
then the sport (x \bmod m + 1) is played, then the sport ((x + 1) \bmod m + 1)
, and so on.

Each sport is played as follows. If all remaining participants (all
participants which are not eliminated yet) are not skilled in that sport,
everyone goes through to the next sport. Otherwise, all skilled participants
go through to the next sport, and all unskilled participants are eliminated
from the competition. Once there is a single participant remaining in the
competition, the competition ends, and that participant is declared the
winner.

As an organizer of the competition, you are curious of the possible outcomes
of the competition beforehand (not that you are going to rig the random roll,
how could you possibly think that...). For each sport x , print the index of
the winner if the competition starts with the sport x .

Input

The first line contains two integers n and m (2 \le n, m \le 10^6 ; n \le 2^m
; nm \le 2 \cdot 10^6 ) — the number of participants and the number of sports,
respectively.

The i -th of the next n lines contains a binary string consisting of exactly m
characters 0 or 1 — the skillset of the i -th participant. If the j -th
character is 1, the i -th participant is skilled in the j -th sport. If it's
0, the i -th participant is not skilled in the j -th sport.

Additional constraint on the input: for each pair of participants, there
exists at least one sport such that one of them is skilled in that sport and
the other one isn't. In other words, all n binary strings are pairwise
distinct.

Output

Print m integers. For each x from 1 to m , print the index of the winner if
the competition starts with the sport x .

Example

Input

    3 5
    
    10010
    
    01100
    
    10101

Output

    3 2 3 1 3 
    