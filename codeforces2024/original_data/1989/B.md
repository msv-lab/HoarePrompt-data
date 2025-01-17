You are given two strings a and b , both consisting of lowercase Latin
letters.

A subsequence of a string is a string which can be obtained by removing
several (possibly zero) characters from the original string. A substring of a
string is a contiguous subsequence of that string.

For example, consider the string abac:

  * a, b, c, ab, aa, ac, ba, bc, aba, abc, aac, bac and abac are its subsequences; 
  * a, b, c, ab, ba, ac, aba, bac and abac are its substrings. 

Your task is to calculate the minimum possible length of the string that
contains a as a substring and b as a subsequence.

Input

The first line contains a single integer t (1 \le t \le 10^3 ) — the number of
test cases.

The first line of each test case contains a string a (1 \le |a| \le 100 ),
consisting of lowercase Latin letters.

The second line of each test case contains a string b (1 \le |b| \le 100 ),
consisting of lowercase Latin letters.

Output

For each test case, print a single integer — the minimum possible length of
the string that contains a as a substring and b as a subsequence.

Example

Input

    5
    
    aba
    
    cb
    
    er
    
    cf
    
    mmm
    
    mmm
    
    contest
    
    test
    
    cde
    
    abcefg

Output

    4
    4
    3
    7
    7
    
Note

In the examples below, the characters that correspond to the subsequence equal
to b are bolded.

In the first example, one of the possible answers is caba.

In the second example, one of the possible answers is ercf.

In the third example, one of the possible answers is mmm.

In the fourth example, one of the possible answers is contest.

In the fifth example, one of the possible answers is abcdefg.
