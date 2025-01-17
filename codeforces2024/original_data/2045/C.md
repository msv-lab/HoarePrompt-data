The word saraga is an abbreviation of sarana olahraga, an Indonesian term for
a sports facility. It is created by taking the prefix sara of the word sarana
and the suffix ga of the word olahraga. Interestingly, it can also be created
by the prefix sa of the word sarana and the suffix raga of the word olahraga.

An abbreviation of two strings S and T is interesting if there are at least
two different ways to split the abbreviation into two non-empty substrings
such that the first substring is a prefix of S and the second substring is a
suffix of T .

You are given two strings S and T . You want to create an interesting
abbreviation of strings S and T with minimum length, or determine if it is
impossible to create an interesting abbreviation.

Input

The first line consists of a string S (1 \leq |S| \leq 200\,000 ).

The second line consists of a string T (1 \leq |T| \leq 200\,000 ).

Both strings S and T only consist of lowercase English letters.

Output

If it is impossible to create an interesting abbreviation, output -1.

Otherwise, output a string in a single line representing an interesting
abbreviation of strings S and T with minimum length. If there are multiple
solutions, output any of them.

Examples

Input

    sarana
    olahraga
    
Output

    saga

Input

    berhiber
    wortelhijau
    
Output

    berhijau

Input

    icpc
    icpc
    
Output

    icpc

Input

    icpc
    jakarta
    
Output

    -1

Note

Explanation for the sample input/output #1

You can split saga into s and aga, or sa and ga. The abbreviation saraga is
interesting, but saga has a smaller length.

Explanation for the sample input/output #2

The abbreviation belhijau is also interesting with minimum length, so it is
another valid solution.
