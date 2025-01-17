You are given an integer array a of size n .

Let's call an array good if it can be obtained using the following algorithm:
create an array consisting of any single integer; and then perform the
following operation an arbitrary number of times: choose an element from the
already existing array (let's call it x ) and add x , (x-1) , or (x+1) to the
end of the array.

For example, the arrays [1, 2, 1] , [5] and [3, 2, 1, 4] are good, while [2,
4] and [3, 1, 2] are not.

Your task is to count the number of good contiguous subarrays of the array a .
Two subarrays that have the same elements but are in different positions of
the array a are considered different.

Input

The first line contains a single integer t (1 \le t \le 10^4 ) — the number of
test cases.

The first line of each test case contains a single integer n (1 \le n \le 3
\cdot 10^5 ).

The second line of each test case contains n integers a_1, a_2, \dots, a_n ( 1
\le a_i \le n) .

Additional constraint on the input: the sum of n over all test cases does not
exceed 3 \cdot 10^5 .

Output

For each test case, print a single integer — the number of good contiguous
subarrays of the array a .

Example

Input

    4
    
    3
    
    1 1 3
    
    4
    
    3 2 3 1
    
    1
    
    1
    
    8
    
    4 5 6 5 3 2 3 1

Output

    4
    9
    1
    23
    
Note

In the first example, the following four subarrays are good:

  * from the 1 -st to the 1 -st element; 
  * from the 1 -st to the 2 -nd element; 
  * from the 2 -nd to the 2 -nd element; 
  * from the 3 -rd to the 3 -rd element. 

In the second example, the only subarray which is not good is the subarray
from the 3 -rd element to the 4 -th element.
