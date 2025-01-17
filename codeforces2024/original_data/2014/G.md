What is done is done, and the spoilt milk cannot be helped.

Little John is as little as night is day — he was known to be a giant, at
possibly 2.1 metres tall. It has everything to do with his love for milk.

His dairy diary has n entries, showing that he acquired a_i pints of fresh
milk on day d_i . Milk declines in freshness with time and stays drinkable for
a maximum of k days. In other words, fresh milk acquired on day d_i will be
drinkable between days d_i and d_i+k-1 inclusive.

Every day, Little John drinks drinkable milk, up to a maximum of m pints. In
other words, if there are less than m pints of milk, he will drink them all
and not be satisfied; if there are at least m pints of milk, he will drink
exactly m pints and be satisfied, and it's a milk satisfaction day.

Little John always drinks the freshest drinkable milk first.

Determine the number of milk satisfaction days for Little John.

Input

The first line of the input contains a single integer t (1\leq t \leq 10^4 ),
the number of test cases.

The first line of each test case consists of three integers n , m , k (1\le n
, m , k \le 10^5 ), the number of diary entries, the maximum pints needed for
a milk satisfaction day, and the duration of milk's freshness.

Then follow n lines of each test case, each with two integers d_i and a_i
(1\le d_i , a_i \le 10^6 ), the day on which the milk was acquired and the
number of pints acquired. They are sorted in increasing values of d_i , and
all values of d_i are distinct.

It is guaranteed that the sum of n over all test cases does not exceed 2 \cdot
10^5 .

Output

For each test case, output a single integer, the number of milk satisfaction
days.

Example

Input

    6
    
    1 1 3
    
    1 5
    
    2 3 3
    
    1 5
    
    2 7
    
    4 5 2
    
    1 9
    
    2 6
    
    4 9
    
    5 6
    
    5 2 4
    
    4 7
    
    5 3
    
    7 1
    
    11 2
    
    12 1
    
    4 1 3
    
    5 10
    
    9 4
    
    14 8
    
    15 3
    
    5 5 5
    
    8 9
    
    10 7
    
    16 10
    
    21 5
    
    28 9

Output

    3
    3
    4
    5
    10
    6
    
Note

In the first test case, 5 pints of milk are good for 3 days before spoiling.

In the second test case, the following will happen:

  * On day 1 , he will receive 5 pints of milk and drink 3 of them (leaving 2 pints from day 1 ); 
  * On day 2 , he will receive 7 pints of milk and drink 3 of them (leaving 2 pints from day 1 and 4 pints from day 2 ); 
  * On day 3 , he will drink 3 pints from day 2 (leaving 2 pints from day 1 and 1 pint from day 2 ); 
  * On day 4 , the milk acquired on day 1 will spoil, and he will drink 1 pint from day 2 (no more milk is left). 
