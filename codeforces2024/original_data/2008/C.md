Today, Sakurako was studying arrays. An array a of length n is considered good
if and only if:

  * the array a is increasing, meaning a_{i - 1} < a_i for all 2 \le i \le n ; 
  * the differences between adjacent elements are increasing, meaning a_i - a_{i-1} < a_{i+1} - a_i for all 2 \le i < n . 

Sakurako has come up with boundaries l and r and wants to construct a good
array of maximum length, where l \le a_i \le r for all a_i .

Help Sakurako find the maximum length of a good array for the given l and r .

Input

The first line contains a single integer t (1\le t\le 10^4 ) — the number of
test cases.

The only line of each test case contains two integers l and r (1\le l\le r\le
10^9 ).

Output

For each test case, output a single integer — the length of the longest good
array Sakurako can form given l and r .

Example

Input

    5
    
    1 2
    
    1 5
    
    2 2
    
    10 20
    
    1 1000000000

Output

    2
    3
    1
    5
    44721
    
Note

For l=1 and r=5 , one possible array could be (1,2,5) . It can be proven that
an array of length 4 does not exist for the given l and r .

For l=2 and r=2 , the only possible array is (2) .

For l=10 and r=20 , the only possible array is (10,11,13,16,20) .
