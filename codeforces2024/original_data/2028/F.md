Note that the memory limit is unusual.

The Cheshire Cat has a riddle for Alice: given n integers a_1, a_2, \ldots,
a_n and a target m , is there a way to insert + and \times into the circles of
the expression

to make it true? We follow the usual order of operations: \times is done
before + .

Although Alice is excellent at chess, she is not good at math. Please help her
so she can find a way out of Wonderland!

Input

Each test contains multiple test cases. The first line of input contains a
single integer t (1 \le t \le 10^4 ) — the number of test cases. The
description of the test cases follows.

The first line of each test case contains two integers n, m (1\le n\le 2\cdot
10^5 ; 1\le m\le 10^4 ) — the number of integers and the target, respectively.

The second line of each test case contains n integers a_1, a_2, \ldots, a_n
(0\le a_i\le 10^4 ) — the elements of the array a .

The sum of n over all test cases does not exceed 2\cdot 10^5 .

Output

For each test case, output "YES" without quotes if it is possible to get the
target by inserting + or \times and "NO" otherwise.

You can output each letter in any case (for example, the strings "yEs", "yes",
"Yes", and "YES" will be recognized as a positive answer).

Example

Input

    6
    
    5 4
    
    2 1 1 1 2
    
    5 5
    
    2 1 1 1 2
    
    5 6
    
    2 1 1 1 2
    
    5 7
    
    2 1 1 1 2
    
    5 8
    
    2 1 1 1 2
    
    5 6
    
    2 0 2 2 3

Output

    YES
    YES
    YES
    YES
    NO
    YES
    
Note

Possible solutions for the first four test cases are shown below.

It is impossible to get a result of 8 in the fifth test case.
