You are given a number n with a length of no more than 10^5 .

You can perform the following operation any number of times: choose one of its
digits, square it, and replace the original digit with the result. The result
must be a digit (that is, if you choose the digit x , then the value of x^2
must be less than 10 ).

Is it possible to obtain a number that is divisible by 9 through these
operations?

Input

The first line contains an integer t (1 \le t \le 10^4 ) — the number of test
cases.

The only line of each test case contains the number n , without leading zeros.
The length of the number does not exceed 10^5 .

It is guaranteed that the sum of the lengths of the numbers across all test
cases does not exceed 10^5 .

Output

For each test case, output "YES" if it is possible to obtain a number
divisible by 9 using the described operations, and "NO" otherwise.

You can output each letter in any case (lowercase or uppercase). For example,
the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive
answer.

Example

Input

    9
    
    123
    
    322
    
    333333333333
    
    9997
    
    5472778912773
    
    1234567890
    
    23
    
    33
    
    52254522632

Output

    NO
    YES
    YES
    NO
    NO
    YES
    NO
    YES
    YES
    
Note

In the first example, from the integer 123 , it is possible to obtain only 123
, 143 , 129 , and 149 , none of which are divisible by 9 .

In the second example, you need to replace the second digit with its square;
then n will equal 342 = 38 \cdot 9 .

In the third example, the integer is already divisible by 9 .
