Alice has been giving gifts to Bob for many years, and she knows that what he
enjoys the most is performing [bitwise XOR](http://tiny.cc/xor_wiki_eng) of
interesting integers. Bob considers a positive integer x to be interesting if
it satisfies x \not\equiv k (\bmod 2^i) . Therefore, this year for his
birthday, she gifted him a super-powerful "XORificator 3000", the latest
model.

Bob was very pleased with the gift, as it allowed him to instantly compute the
XOR of all interesting integers in any range from l to r , inclusive. After
all, what else does a person need for happiness? Unfortunately, the device was
so powerful that at one point it performed XOR with itself and disappeared.
Bob was very upset, and to cheer him up, Alice asked you to write your version
of the "XORificator".

Input

The first line of input contains a single integer t (1 \leq t \leq 10^4) — the
number of XOR queries on the segment. The following t lines contain the
queries, each consisting of the integers l , r , i , k (1 \leq l \leq r \leq
10^{18} , 0 \leq i \leq 30 , 0 \leq k < 2^i) .

Output

For each query, output a single integer — the XOR of all integers x in the
range [l, r] such that x \not\equiv k \mod 2^i .

Example

Input

    6
    
    1 3 1 0
    
    2 28 3 7
    
    15 43 1 0
    
    57 2007 1 0
    
    1010 1993 2 2
    
    1 1000000000 30 1543

Output

    2
    2
    13
    0
    4
    1000000519
    
Note

In the first query, the interesting integers in the range [1, 3] are 1 and 3 ,
so the answer will be 1 \oplus 3 = 2 .
