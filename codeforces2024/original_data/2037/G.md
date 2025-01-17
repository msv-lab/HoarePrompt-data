You are exploring the stunning region of Natlan! This region consists of n
cities, and each city is rated with an attractiveness a_i . A directed edge
exists from City i to City j if and only if i < j and \gcd(a_i,a_j)\neq 1 ,
where \gcd(x, y) denotes the [greatest common divisor
(GCD)](https://en.wikipedia.org/wiki/Greatest_common_divisor) of integers x
and y .

Starting from City 1 , your task is to determine the total number of distinct
paths you can take to reach City n , modulo 998\,244\,353 . Two paths are
different if and only if the set of cities visited is different.

Input

The first line contains an integer n (2 \leq n \leq 2 \cdot 10^5 ) — the
number of cities.

The second line contains n integers a_1, a_2, \ldots, a_n (2 \leq a_i \leq
10^6 ) — the attractiveness of each city.

Output

Output the total number of distinct paths you can take to reach City n ,
modulo 998\,244\,353 .

Examples

Input

    5
    
    2 6 3 4 6

Output

    5
    
Input

    5
    
    4 196 2662 2197 121

Output

    2
    
Input

    7
    
    3 6 8 9 11 12 20

Output

    7
    
Input

    2
    
    2 3

Output

    0
    
Note

In the first example, the five paths are the following:

  * City 1\rightarrow City 5 
  * City 1\rightarrow City 2\rightarrow City 5 
  * City 1\rightarrow City 2\rightarrow City 3\rightarrow City 5 
  * City 1\rightarrow City 2\rightarrow City 4\rightarrow City 5 
  * City 1\rightarrow City 4\rightarrow City 5 

In the second example, the two paths are the following:

  * City 1\rightarrow City 3\rightarrow City 5 
  * City 1\rightarrow City 2\rightarrow City 3\rightarrow City 5 
