If it was so, then let's make it a deal...

— MayDay,
[Gentleness](https://www.youtube.com/watch?v=mtAc_bMYBsM&list=PLj6NQzHFCvkHKIm0Vnk9LH3odqTIBRZ1Q&index=15)

Even after copying the paintings from famous artists for ten years,
unfortunately, Eric is still unable to become a skillful impressionist
painter. He wants to forget something, but the white bear phenomenon just
keeps hanging over him.

Eric still remembers n pieces of impressions in the form of an integer array.
He records them as w_1, w_2, \ldots, w_n . However, he has a poor memory of
the impressions. For each 1 \leq i \leq n , he can only remember that l_i \leq
w_i \leq r_i .

Eric believes that impression i is unique if and only if there exists a
possible array w_1, w_2, \ldots, w_n such that w_i \neq w_j holds for all 1
\leq j \leq n with j \neq i .

Please help Eric determine whether impression i is unique for every 1 \leq i
\leq n , independently for each i . Perhaps your judgment can help rewrite the
final story.

Input

Each test contains multiple test cases. The first line of the input contains a
single integer t (1 \leq t \leq 10^4 ) — the number of test cases. The
description of test cases follows.

The first line of each test case contains a single integer n (1 \leq n \leq
2\cdot 10^5 ) — the number of impressions.

Then n lines follow, the i -th containing two integers l_i and r_i (1 \leq l_i
\leq r_i \leq 2\cdot n ) — the minimum possible value and the maximum possible
value of w_i .

It is guaranteed that the sum of n over all test cases does not exceed 2\cdot
10^5 .

Output

For each test case, output a binary string s of length n : for each 1 \leq i
\leq n , if impression i is unique, s_i=\texttt{1} ; otherwise, s_i=\texttt{0}
. Do not output spaces.

Example

Input

    5
    
    2
    
    1 1
    
    1 1
    
    4
    
    1 3
    
    1 3
    
    1 3
    
    1 3
    
    6
    
    3 6
    
    2 2
    
    1 2
    
    1 1
    
    3 4
    
    2 2
    
    7
    
    3 4
    
    4 4
    
    4 4
    
    1 3
    
    2 5
    
    1 4
    
    2 2
    
    3
    
    4 5
    
    4 4
    
    5 5

Output

    00
    1111
    100110
    1001111
    011
    
Note

In the first test case, the only possible array w is [1, 1] , making neither
impression 1 nor 2 unique (since w_1 = w_2 ).

In the second test case, all impressions can be made unique:

  * For i = 1 , we can set w to [1, 3, 2, 3] , in which w_1 \neq w_2 , w_1 \neq w_3 , and w_1 \neq w_4 ; 
  * For i = 2 , we can set w to [2, 3, 1, 2] , in which w_2 \neq w_1 , w_2 \neq w_3 , and w_2 \neq w_4 ; 
  * For i = 3 , we can set w to [1, 1, 3, 1] ; 
  * For i = 4 , we can set w to [2, 3, 3, 1] . 

In the third test case, for i = 4 , we can set w to [3, 2, 2, 1, 3, 2] . Thus,
impression 4 is unique.
