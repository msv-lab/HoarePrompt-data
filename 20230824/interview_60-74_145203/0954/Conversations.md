# Question: 0954
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
Hongcow is learning to spell! One day, his teacher gives him a word that he needs to learn to spell. Being a dutiful student, he immediately learns how to spell the word.

Hongcow has decided to try to make new words from this one. He starts by taking the word he just learned how to spell, and moves the last character of the word to the beginning of the word. He calls this a cyclic shift. He can apply cyclic shift many times. For example, consecutively applying cyclic shift operation to the word "abracadabra" Hongcow will get words "aabracadabr", "raabracadab" and so on.

Hongcow is now wondering how many distinct words he can generate by doing the cyclic shift arbitrarily many times. The initial string is also counted.


-----Input-----

The first line of input will be a single string s (1 ≤ |s| ≤ 50), the word Hongcow initially learns how to spell. The string s consists only of lowercase English letters ('a'–'z').


-----Output-----

Output a single integer equal to the number of distinct strings that Hongcow can obtain by applying the cyclic shift arbitrarily many times to the given string.


-----Examples-----
Input
abcd

Output
4

Input
bbb

Output
1

Input
yzyz

Output
2



-----Note-----

For the first sample, the strings Hongcow can generate are "abcd", "dabc", "cdab", and "bcda".

For the second sample, no matter how many times Hongcow does the cyclic shift, Hongcow can only generate "bbb".

For the third sample, the two strings Hongcow can generate are "yzyz" and "zyzy".
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
distinct_words = set()
for i in range(len(s)):
    distinct_words.add(s)
    s = s[-1] + s[:-1]
print(len(distinct_words))
#@!CODE END!@#
````

---

