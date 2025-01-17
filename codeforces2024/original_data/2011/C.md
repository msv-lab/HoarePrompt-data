You are given a string s of the form <block of digits>+<block of
digits>+...+<block of digits>. Every block of digits consists of at least 2
and at most 13 digits; every digit is from 1 to 9 .

You have to split this string into expressions of the form
<integer>+<integer>. Every expression must be a contiguous part of the given
string, and every character of the given string must belong to exactly one
expression. For example, if you have a string 123+456+789+555, then:

  * you are allowed to split it into 123+4, 56+7 and 89+555; 
  * you are not allowed to split it into 123+456 and +789+555, since the second part begins with a + sign; 
  * you are not allowed to split it into 123+4, 56+7, 8 and 9+555, since the third part does not contain a + sign; 
  * you are not allowed to split it into 123+456+78 and 9+555, since the first part contains two + signs. 

Among all allowed ways to split the string, find one which maximizes the sum
of results of all expressions you get, and print this sum.

Input

The first line contains one integer t (1 \le t \le 100 ) — the number of test
cases.

Each test case consists of one line containing the string s (5 \le |s| \le
1000 ) of the form <block of digits>+<block of digits>+...+<block of digits>.
The string contains at least one '+' sign. Every block of digits consists of
at least 2 and at most 13 digits; every digit is from 1 to 9 .

Output

For each test case, print one integer — the maximum possible sum of results of
all expressions you get after splitting the string.

Example

Input

    3
    
    123+456+789+555
    
    13+37
    
    9999999999999+1111111111111+9999999999999

Output

    834
    50
    20111111111110
    
Note

In the first test case of the example, you should split the string into
expressions 123+4, 56+7 and 89+555. The sum of results of these expressions is
834 .

In the second test case of the example, the given string is already a valid
expression and cannot be split any further.
