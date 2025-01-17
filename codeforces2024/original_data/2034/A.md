There is a tale about the wise [King
Keykhosrow](https://en.wikipedia.org/wiki/Kay_Khosrow) who owned a grand
treasury filled with treasures from across the Persian Empire. However, to
prevent theft and ensure the safety of his wealth, King Keykhosrow's vault was
sealed with a magical lock that could only be opened by solving a riddle.

![](https://espresso.codeforces.com/02ff1013de2c71e8f78fd7d74b43bd365dcc6a3b.webp)

The riddle involves two sacred numbers a and b . To unlock the vault, the
challenger must determine the smallest key number m that satisfies two
conditions:

  * m must be greater than or equal to at least one of a and b . 
  * The remainder when m is divided by a must be equal to the remainder when m is divided by b . 

Only by finding the smallest correct value of m can one unlock the vault and
access the legendary treasures!

Input

The first line of the input contains an integer t (1 \leq t \leq 100 ), the
number of test cases.

Each test case consists of a single line containing two integers a and b (1
\leq a, b \leq 1000 ).

Output

For each test case, print the smallest integer m that satisfies the conditions
above.

Example

Input

    2
    
    4 6
    
    472 896

Output

    12
    52864
    
Note

In the first test case, you can see that:

  * 4 \bmod 4 = 0 but 4 \bmod 6 = 4 
  * 5 \bmod 4 = 1 but 5 \bmod 6 = 5 
  * 6 \bmod 4 = 2 but 6 \bmod 6 = 0 
  * 7 \bmod 4 = 3 but 7 \bmod 6 = 1 
  * 8 \bmod 4 = 0 but 8 \bmod 6 = 2 
  * 9 \bmod 4 = 1 but 9 \bmod 6 = 3 
  * 10 \bmod 4 = 2 but 10 \bmod 6 = 4 
  * 11 \bmod 4 = 3 but 11 \bmod 6 = 5 

so no integer less than 12 satisfies the desired properties.
