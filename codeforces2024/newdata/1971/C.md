There is a clock labeled with the numbers 1 through 12 in clockwise order, as
shown below.

![](https://espresso.codeforces.com/1e87df1aba4cbffb31068e202e70b895a23a5586.png)

In this example, (a,b,c,d)=(2,9,10,6) , and the strings intersect.

Alice and Bob have four distinct integers a , b , c , d not more than 12 .
Alice ties a red string connecting a and b , and Bob ties a blue string
connecting c and d . Do the strings intersect? (The strings are straight line
segments.)

Input

The first line contains a single integer t (1 \leq t \leq 5940 ) — the number
of test cases.

The only line of each test case contains four distinct integers a , b , c , d
(1 \leq a, b, c, d \leq 12 ).

Output

For each test case, output "YES" (without quotes) if the strings intersect,
and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes",
and "Yes" will be recognized as a positive response).

Example

Input

    15
    
    2 9 10 6
    
    3 8 9 1
    
    1 2 3 4
    
    5 3 4 12
    
    1 8 2 10
    
    3 12 11 8
    
    9 10 12 1
    
    12 1 10 2
    
    3 12 6 9
    
    1 9 8 4
    
    6 7 9 12
    
    7 12 9 6
    
    10 12 11 1
    
    3 9 6 12
    
    1 4 3 5

Output

    YES
    NO
    NO
    YES
    YES
    NO
    NO
    NO
    NO
    NO
    NO
    YES
    YES
    YES
    YES
    
Note

The first test case is pictured in the statement.

In the second test case, the strings do not intersect, as shown below.

![](https://espresso.codeforces.com/e089e5742688ef3918a5843591edd82871f9f7dc.png)
