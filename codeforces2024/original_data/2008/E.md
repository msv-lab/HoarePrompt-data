Sakurako really loves alternating strings. She calls a string s of lowercase
Latin letters an alternating string if characters in the even positions are
the same, if characters in the odd positions are the same, and the length of
the string is even.

For example, the strings 'abab' and 'gg' are alternating, while the strings
'aba' and 'ggwp' are not.

As a good friend, you decided to gift such a string, but you couldn't find
one. Luckily, you can perform two types of operations on the string:

  1. Choose an index i and delete the i -th character from the string, which will reduce the length of the string by 1 . This type of operation can be performed no more than 1 time; 
  2. Choose an index i and replace s_i with any other letter. 

Since you are in a hurry, you need to determine the minimum number of
operations required to make the string an alternating one.

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

The first line of each test case contains a single number n (1 \le n\le 2\cdot
10^5 ) — the length of the string.

The second line of each test case contains a string s , consisting of
lowercase Latin letters.

It is guaranteed that the sum of n across all test cases does not exceed 2
\cdot 10^5 .

Output

For each test case, output a single integer — the minimum number of operations
required to turn the string s into an alternating one.

Example

Input

    10
    
    1
    
    a
    
    2
    
    ca
    
    3
    
    aab
    
    5
    
    ababa
    
    6
    
    acdada
    
    9
    
    ejibmyyju
    
    6
    
    bbccbc
    
    6
    
    abacba
    
    5
    
    bcbca
    
    5
    
    dcbdb

Output

    1
    0
    1
    1
    2
    6
    2
    3
    1
    1
    
Note

For the string ababa, you can delete the first character to get baba, which is
an alternating string.

For the string acdada, you can change the first two characters to get dadada,
which is an alternating string.
