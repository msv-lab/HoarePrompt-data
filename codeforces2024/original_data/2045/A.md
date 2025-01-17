You are playing a word game using a standard set of 26 uppercase English
letters: A — Z. In this game, you can form vowels and consonants as follows.

  * The letters A, E, I, O, and U can only form a vowel. 
  * The letter Y can form either a vowel or a consonant. 
  * Each of the remaining letters other than A, E, I, O, U, and Y can only form a consonant. 
  * The string NG can form a single consonant when concatenated together. 

Denote a syllable as a concatenation of a consonant, a vowel, and a consonant
in that order. A word is a concatenation of one or more syllables.

You are given a string S and you want to create a word from it. You are
allowed to delete zero or more letters from S and rearrange the remaining
letters to form the word. Find the length of the longest word that can be
created, or determine if no words can be created.

Input

A single line consisting of a string S (1 \leq |S| \leq 5000 ). The string S
consists of only uppercase English letters.

Output

If a word cannot be created, output 0. Otherwise, output a single integer
representing the length of longest word that can be created.

Examples

Input

    ICPCJAKARTA
    
Output

    9
    
Input

    NGENG
    
Output

    5
    
Input

    YYY
    
Output

    3
    
Input

    DANGAN
    
Output

    6
    
Input

    AEIOUY
    
Output

    0
    
Note

Explanation for the sample input/output #1

A possible longest word is JAKCARTAP, consisting of the syllables JAK, CAR,
and TAP.

Explanation for the sample input/output #2

The whole string S is a word consisting of one syllable which is the
concatenation of the consonant NG, the vowel E, and the consonant NG.

Explanation for the sample input/output #3

The whole string S is a word consisting of one syllable which is the
concatenation of the consonant Y, the vowel Y, and the consonant Y.

Explanation for the sample input/output #4

The whole string S is a word consisting of two syllables: DAN and GAN.
