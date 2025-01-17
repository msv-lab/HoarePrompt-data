Sakurako will soon take a test. The test can be described as an array of
integers n and a task on it:

Given an integer x , Sakurako can perform the following operation any number
of times:

  * Choose an integer i (1\le i\le n ) such that a_i\ge x ; 
  * Change the value of a_i to a_i-x . 

Using this operation any number of times, she must find the minimum possible
median^{\text{∗}} of the array a .

Sakurako knows the array but does not know the integer x . Someone let it slip
that one of the q values of x will be in the next test, so Sakurako is asking
you what the answer is for each such x .

^{\text{∗}} The median of an array of length n is the element that stands in
the middle of the sorted array (at the \frac{n+2}{2} -th position for even n ,
and at the \frac{n+1}{2} -th for odd)

Input

The first line contains one integer t (1\le t\le 10^4 ) — the number of test
cases.

The first line of each test case contains two integers n and q (1\le n,q\le
10^5 ) — the number of elements in the array and the number of queries.

The second line of each test case contains n integers a_1, a_2, \dots, a_n
(1\le a_i\le n ) — the elements of the array.

The following q lines each contain one integer x (1\le x\le n ).

It is guaranteed that the sum of n across all test cases does not exceed 10^5
. The same guarantee applies to the sum of q across all test cases.

Output

For each test case, output q integers — the answer for each query.

Example

Input

    2
    
    5 5
    
    1 2 3 4 5
    
    1
    
    2
    
    3
    
    4
    
    5
    
    6 3
    
    1 2 6 4 1 3
    
    2
    
    1
    
    5

Output

    0 1 1 1 2 
    1 0 2 
    