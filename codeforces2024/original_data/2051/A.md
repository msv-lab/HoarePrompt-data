Monocarp and Stereocarp are preparing for the Olympiad. There are n days left
until the Olympiad. On the i -th day, if Monocarp plans to practice, he will
solve a_i problems. Similarly, if Stereocarp plans to practice on the same
day, he will solve b_i problems.

Monocarp can train on any day he wants. However, Stereocarp watches Monocarp
and follows a different schedule: if Monocarp trained on day i and i < n ,
then Stereocarp will train on day (i+1) .

Monocarp wants to organize his training process in a way that the difference
between the number of problems he solves and the number of problems Stereocarp
solves is as large as possible. Formally, Monocarp wants to maximize the value
of (m-s) , where m is the number of problems he solves, and s is the number of
problems Stereocarp solves. Help Monocarp determine the maximum possible
difference in the number of solved problems between them.

Input

The first line contains a single integer t (1 \le t \le 10^3 ) — the number of
test cases.

The first line of each test case contains a single integer n (1 \le n \le 100
).

The second line contains n integers a_1, a_2, \dots, a_n (1 \le a_i \le 100 ).

The third line contains n integers b_1, b_2, \dots, b_n (1 \le b_i \le 100 ).

Output

For each test case, print a single integer — the maximum possible difference
between the number of problems Monocarp solves and the number of problems
Stereocarp solves.

Example

Input

    4
    
    2
    
    3 2
    
    2 1
    
    1
    
    5
    
    8
    
    3
    
    1 1 1
    
    2 2 2
    
    6
    
    8 2 5 6 2 6
    
    8 2 7 4 3 4

Output

    4
    5
    1
    16
    
Note

Let's analyze the example from the statement:

  * In the first test case, it is optimal for Monocarp to train both days; then Stereocarp will train on day 2 . 
  * In the second test case, it is optimal for Monocarp to train on the only day, and Stereocarp will not train at all. 
  * In the third test case, it is optimal for Monocarp to train on the last day (and only on that day). 
  * In the fourth test case, it is optimal for Monocarp to train on days 1, 3, 4, 6 ; then Stereocarp will train on days 2, 4, 5 . 
