For a string p , let f(p) be the number of distinct non-empty
substrings^{\text{∗}} of p .

Shohag has a string s . Help him find a non-empty string p such that p is a
substring of s and f(p) is even or state that no such string exists.

^{\text{∗}} A string a is a substring of a string b if a can be obtained from
b by deletion of several (possibly, zero or all) characters from the beginning
and several (possibly, zero or all) characters from the end.

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

The first and only line of each test case contains a string s (1 \le |s| \le
10^5 ) consisting of lowercase English letters.

It is guaranteed that the sum of the length of s over all test cases doesn't
exceed 3 \cdot 10^5 .

Output

For each test case, print a non-empty string that satisfies the conditions
mentioned in the statement, or -1 if no such string exists. If there are
multiple solutions, output any.

Example

Input

    5
    
    dcabaac
    
    a
    
    youknowwho
    
    codeforces
    
    bangladesh

Output

    abaa
    -1
    youknowwho
    eforce
    bang
    
Note

In the first test case, we can set p = abaa because it is a substring of s and
the distinct non-empty substrings of p are a, b, aa, ab, ba, aba, baa and
abaa, so it has a total of 8 distinct substrings which is even.

In the second test case, we can only set p = a but it has one distinct non-
empty substring but this number is odd, so not valid.

In the third test case, the whole string contains 52 distinct non-empty
substrings, so the string itself is a valid solution.
