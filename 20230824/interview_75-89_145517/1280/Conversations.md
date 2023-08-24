# Question: 1280
## Generation 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Coding Contest Participant. Imagine that you are taking part in a prestigious coding competition. Your task is to design an efficient algorithm for a complex problem. You need to consider all possible edge cases, optimize for efficiency, and ensure that your solution is clean and readable. In addition, provide a Python code of your solution, and put the solution in a code delimiter.For example:
### QUESTION
A. Watermelon
time limit per test: 1 second
memory limit per test: 64 megabytes
input: standard input
output: standard output
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 <= w <= 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
input
8
output
YES
Note
For example, the boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos).

### Expected response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w < 4:
print("NO")
else:
print("YES")
#@!CODE END!@#
````

---

**role**: 
````markdown
user
````

---

**content**: 
````markdown
### QUESTION
You've got string s, consisting of small English letters. Some of the English letters are good, the rest are bad.

A substring s[l...r] (1 ≤ l ≤ r ≤ |s|) of string s  =  s_1s_2...s_{|}s| (where |s| is the length of string s) is string  s_{l}s_{l} + 1...s_{r}.

The substring s[l...r] is good, if among the letters  s_{l}, s_{l} + 1, ..., s_{r} there are at most k bad ones (look at the sample's explanation to understand it more clear).

Your task is to find the number of distinct good substrings of the given string s. Two substrings s[x...y] and s[p...q] are considered distinct if their content is different, i.e. s[x...y] ≠ s[p...q].


-----Input-----

The first line of the input is the non-empty string s, consisting of small English letters, the string's length is at most 1500 characters.

The second line of the input is the string of characters "0" and "1", the length is exactly 26 characters. If the i-th character of this string equals "1", then the i-th English letter is good, otherwise it's bad. That is, the first character of this string corresponds to letter "a", the second one corresponds to letter "b" and so on.

The third line of the input consists a single integer k (0 ≤ k ≤ |s|) — the maximum acceptable number of bad characters in a good substring.


-----Output-----

Print a single integer — the number of distinct good substrings of string s.


-----Examples-----
Input
ababab
01000000000000000000000000
1

Output
5

Input
acbacbacaa
00000000000000000000000000
2

Output
8



-----Note-----

In the first example there are following good substrings: "a", "ab", "b", "ba", "bab".

In the second example there are following good substrings: "a", "aa", "ac", "b", "ba", "c", "ca", "cb".
### Requirements
1. Use Standard Input Format (read inputs with `input()`, write results with `print()`)
2. You will NOT return anything except for the program. 
3. DO NOT WRITE PLANS OR EXPLANATIONS
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
#@!CODE START!@#
s = input()
good_letters = input()
k = int(input())

# Create a set to store the distinct good substrings
good_substrings = set()

# Iterate through each possible starting position of the substring
for i in range(len(s)):
    bad_count = 0 # Counter for the number of bad letters in the current substring
    
    # Iterate through each letter in the substring starting from position i
    for j in range(i, len(s)):
        letter = s[j]
        
        # If the letter is bad, increment the bad count
        if good_letters[ord(letter) - ord('a')] == '0':
            bad_count += 1
        
        # If the bad count is within the acceptable limit (k), add the current substring to the set
        if bad_count <= k:
            good_substrings.add(s[i:j+1])
        
        # If the bad count exceeds the acceptable limit, break the loop as further extensions of the substring will also exceed the limit
        else:
            break

# Output the number of distinct good substrings
print(len(good_substrings))
#@!CODE END!@#
````

---

