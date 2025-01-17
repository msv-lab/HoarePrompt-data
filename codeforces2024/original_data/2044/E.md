Wave is given five integers k , l_1 , r_1 , l_2 , and r_2 . Wave wants you to
help her count the number of ordered pairs (x, y) such that all of the
following are satisfied:

  * l_1 \leq x \leq r_1 . 
  * l_2 \leq y \leq r_2 . 
  * There exists a non-negative integer n such that \frac{y}{x} = k^n . 

Input

The first line contains an integer t (1 \leq t \leq 10^4 ) — the number of
test cases.

The only line of each test case contains five integers k , l_1 , r_1 , l_2 ,
and r_2 (2 \leq k \leq 10^9, 1 \leq l_1 \leq r_1 \leq 10^9, 1 \leq l_2 \leq
r_2 \leq 10^9 ).

Output

For each test case, output the number of matching ordered pairs (x, y) on a
new line.

Example

Input

    5
    
    2 2 6 2 12
    
    2 1 1000000000 1 1000000000
    
    3 5 7 15 63
    
    1000000000 1 5 6 1000000000
    
    15 17 78 2596 20914861

Output

    12
    1999999987
    6
    1
    197
    
Note

In the third test case, the matching ordered pairs are the following:

  * (5,15) 
  * (5,45) 
  * (6,18) 
  * (6,54) 
  * (7,21) 
  * (7,63) 

In the fourth test case, the only valid ordered pair is (1,1\,000\,000\,000)
