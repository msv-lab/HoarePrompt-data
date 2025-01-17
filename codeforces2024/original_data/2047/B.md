You're given a string s of length n , consisting of only lowercase English
letters.

You must do the following operation exactly once:

  * Choose any two indices i and j (1 \le i, j \le n ). You can choose i = j . 
  * Set s_i := s_j . 

You need to minimize the number of distinct permutations^\dagger of s . Output
any string with the smallest number of distinct permutations after performing
exactly one operation.

^\dagger A permutation of the string is an arrangement of its characters into
any order. For example, "bac" is a permutation of "abc" but "bcc" is not.

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 500 ). The description of the test cases follows.

The first line of each test case contains n (1 \le n \le 10 ) — the length of
string s .

The second line of each test case contains s of length n . The string contains
only lowercase English letters.

Output

For each test case, output the required s after applying exactly one
operation. If there are multiple solutions, print any of them.

Example

Input

    6
    
    3
    
    abc
    
    4
    
    xyyx
    
    8
    
    alphabet
    
    1
    
    k
    
    10
    
    aabbccddee
    
    6
    
    ttbddq

Output

    cbc
    yyyx
    alphaaet
    k
    eabbccddee
    tttddq
    
Note

In the first test case, we can obtain the following strings in one operation:
"abc", "bbc", "cbc", "aac", "acc", "aba", and "abb".

The string "abc" has 6 distinct permutations: "abc", "acb", "bac", "bca",
"cab", and "cba".

The string "cbc" has 3 distinct permutations: "bcc", "cbc", and "ccb", which
is the lowest of all the obtainable strings. In fact, all obtainable strings
except "abc" have 3 permutations, so any of them would be accepted.
