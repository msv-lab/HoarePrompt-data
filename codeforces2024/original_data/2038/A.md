There is a team of n software engineers numbered from 1 to n . Their boss
promises to give them a bonus if they complete an additional project. The
project requires k units of work in total. The bonus promised to the i -th
engineer is a_i burles. The boss doesn't assign specific tasks to engineers;
it is expected that every engineer will voluntarily complete some integer
amount of work units. The bonus will be paid to the entire team only if the
project is completed; in other words, if the total amount of voluntary work
units on the project is greater than or equal to k .

The amount of work that can be performed by each engineer is not limited.
However, all engineers value their labour. The i -th engineer estimates one
unit of their work as b_i burles. If the bonus is paid, the benefit s_i of the
i -th engineer for completing c units of work is defined as s_i = a_i - c
\cdot b_i . If the bonus is not paid, the engineer will not volunteer to do
any work.

Engineers work together for many years, so they know how the bonus is going to
be distributed and how much their colleagues value the labour. That is, all
a_i and all b_i are known to every engineer in the team.

Engineers are eager to get the bonus, so they agreed on the following process
of work distribution between them:

  * the first engineer says: "I will complete c_1 units of work", where c_1 is a non-negative integer; 
  * then, the second engineer says: "I will complete c_2 units of work", where c_2 is a non-negative integer; 
  * ... and so on; 
  * finally, the n -th engineer says: "I will complete c_n units of work", where c_n is a non-negative integer. 

Every engineer voices c_i in a way to maximize their own benefit s_i . If the
expected benefit is going to be zero, an engineer will still agree to work to
get the experience and to help their colleagues obtain the bonus. However, if
the benefit is expected to be negative for some reason (an engineer needs to
perform an excessive amount of work or the project is not going to be
completed), that engineer will not work at all (completes zero amount of work
units).

Given that every engineer acts perfectly, your task is to find out the numbers
c_i voiced by every engineer.

Input

The first line contains two integers n and k (1 \le n \le 1000 ; 1 \le k \le
10^6 ) — the number of engineers in the company and the number of work units
the project requires, respectively.

The second line contains n integers a_1, a_2, \dots, a_n (1 \le a_i \le 10^9
), where a_i is the bonus which will be paid to the i -th engineer if the
project is completed.

The third line contains n integers b_1, b_2, \dots, b_n (1 \le b_i \le 1000 ),
where b_i is the work unit cost for the i -th engineer.

Output

Print n integers c_1, c_2, \dots, c_n (0 \le c_i \le k ) — the amount of work
completed by each engineer given that every engineer behaves optimally. Note
that the answer is unique.

Examples

Input

    3 6
    
    4 7 6
    
    1 2 3

Output

    1 3 2
    
Input

    3 12
    
    4 7 6
    
    1 2 3

Output

    0 0 0
    
Input

    3 11
    
    6 7 8
    
    1 2 3

Output

    6 3 2
    
Note

In the first example, engineers distributed the work across them and got the
bonus, even though the benefit for the third engineer is zero.

In the second example, the bonus project requires too many work units to
complete, so it's more beneficial for engineers not to work at all.
