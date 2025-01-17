Kevin is a master of permutation-related problems. You are taking a walk with
Kevin in Darkwoods, and during your leisure time, he wants to ask you the
following question.

Given two positive integers n and k , construct a permutation^{\text{∗}} p of
length n to minimize the sum of the minimum values of all subarrays^{\text{†}}
of length k . Formally, you need to minimize

^{\text{∗}} A permutation of length n is an array consisting of n distinct
integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a
permutation, but [1,2,2] is not a permutation (2 appears twice in the array),
and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

^{\text{†}} An array a is a subarray of an array b if a can be obtained from b
by the deletion of several (possibly, zero or all) elements from the beginning
and several (possibly, zero or all) elements from the end. Two subarrays are
considered different if the sets of positions of the deleted elements are
different.

Input

Each test consists of multiple test cases. The first line contains the number
of test cases t (1 \le t \le 10^3 ).

The only line of each test case contains two integers n and k ( 1\le k\le n\le
10^5 ).

It is guaranteed that the sum of n over all test cases doesn't exceed 10^5 .

Output

For each test case, output n integers on a single line — the permutation p you
constructed.

If there are multiple answers, you can print any of them.

Example

Input

    3
    4 2
    6 1
    8 3
    
Output

    3 1 2 4
    5 2 1 6 4 3
    4 6 2 8 3 1 5 7
    
Note

In the first test case, with k=2 , consider all subarrays of length 2 : the
minimum value of p_1,p_2 is 1 , the minimum value of p_2,p_3 is 1 , and the
minimum value of p_3,p_4 is 2 . The sum 1+1+2=4 is the smallest among all
possible permutations.

In the second test case, all subarrays of length 1 have minimum values of 5,
2, 1, 6, 4, 3 , and the sum 5+2+1+6+4+3=21 is proven to be the smallest.
