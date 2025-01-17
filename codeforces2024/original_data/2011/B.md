Yes, this is another one of those constructive permutation problems.

You are given an integer n . You have to construct a permutation p of size n ,
i. e. an array of n integers, where every integer from 1 to n appears exactly
once.

Every pair of adjacent elements in the permutation (p_i and p_{i+1} ) must
meet the following condition:

  * if one of them is divisible by the other, the condition p_i < p_{i+1} must hold; 
  * otherwise, the condition p_i > p_{i+1} must hold. 

Input

The first line contains one integer t (1 \le t \le 99 ) — the number of test
cases.

Each test case consists of one line, containing one integer n (2 \le n \le 100
).

Output

For each test case, print the answer as follows:

  * if no permutation of size n meeting the conditions from the statement exists, print -1 ; 
  * otherwise, print n distinct integers from 1 to n — the required permutation. If there are mutliple answers, print any of them. 

Example

Input

    2
    
    5
    
    10

Output

    1 5 2 4 3
    1 2 10 9 7 4 8 3 6 5
    