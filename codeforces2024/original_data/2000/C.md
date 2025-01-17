Kristina has an array a , called a template, consisting of n integers. She
also has m strings, each consisting only of lowercase Latin letters. The
strings are numbered from 1 to m . She wants to check which strings match the
template.

A string s is considered to match the template if all of the following
conditions are simultaneously satisfied:

  * The length of the string s is equal to the number of elements in the array a .
  * The same numbers from a correspond to the same symbols from s . So, if a_i = a_j , then s_i = s_j for (1 \le i, j \le n ).
  * The same symbols from s correspond to the same numbers from a . So, if s_i = s_j , then a_i = a_j for (1 \le i, j \le n ).

In other words, there must be a one-to-one correspondence between the
characters of the string and the elements of the array.

For example, if a = [3, 5, 2, 1, 3 ], then the string "abfda" matches the
template, while the string "afbfa" does not, since the character "f"
corresponds to both numbers 1 and 5 .

Input

The first line of input contains a single integer t (1 \le t \le 10^4 ) — the
number of test cases.

The following descriptions are for the test cases.

The first line of each test case contains a single integer n (1 \le n \le 2
\cdot 10^5 ) — the number of elements in the array a .

The second line of each test case contains exactly n integers a_i (-10^9 \le
a_i \le 10^9 ) — the elements of the array a .

The third line of each test case contains a single integer m (1 \le m \le 2
\cdot 10^5 ) — the number of strings to check for template matching.

Following are m strings, each containing a non-empty string s_j (1 \le |s_j|
\le 2 \cdot 10^5 ), consisting of lowercase Latin letters.

It is guaranteed that the sum of n across all test cases does not exceed 2
\cdot 10^5 , and that the sum of the lengths of all strings does not exceed 2
\cdot 10^5 .

Output

For each test case, output m lines. On the i -th line (1 \le i \le m ) output:

  * "YES", if the string with index i matches the template; 
  * "NO" otherwise. 

You may output the answer in any case (for example, the strings "yEs", "yes",
"Yes", and "YES" will be recognized as a positive answer).

Example

Input

    3
    
    5
    
    3 5 2 1 3
    
    2
    
    abfda
    
    afbfa
    
    2
    
    1 2
    
    3
    
    ab
    
    abc
    
    aa
    
    4
    
    5 -3 5 -3
    
    4
    
    aaaa
    
    bcbc
    
    aba
    
    cbcb

Output

    YES
    NO
    YES
    NO
    NO
    NO
    YES
    NO
    YES

Note

The first test case is explained in the problem statement.
