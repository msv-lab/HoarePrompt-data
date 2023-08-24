# Question: 2172
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
You have a new professor of graph theory and he speaks very quickly. You come up with the following plan to keep up with his lecture and make notes.

You know two languages, and the professor is giving the lecture in the first one. The words in both languages consist of lowercase English characters, each language consists of several words. For each language, all words are distinct, i.e. they are spelled differently. Moreover, the words of these languages have a one-to-one correspondence, that is, for each word in each language, there exists exactly one word in the other language having has the same meaning.

You can write down every word the professor says in either the first language or the second language. Of course, during the lecture you write down each word in the language in which the word is shorter. In case of equal lengths of the corresponding words you prefer the word of the first language.

You are given the text of the lecture the professor is going to read. Find out how the lecture will be recorded in your notes.


-----Input-----

The first line contains two integers, n and m (1 ≤ n ≤ 3000, 1 ≤ m ≤ 3000) — the number of words in the professor's lecture and the number of words in each of these languages.

The following m lines contain the words. The i-th line contains two strings a_{i}, b_{i} meaning that the word a_{i} belongs to the first language, the word b_{i} belongs to the second language, and these two words have the same meaning. It is guaranteed that no word occurs in both languages, and each word occurs in its language exactly once.

The next line contains n space-separated strings c_1, c_2, ..., c_{n} — the text of the lecture. It is guaranteed that each of the strings c_{i} belongs to the set of strings {a_1, a_2, ... a_{m}}.

All the strings in the input are non-empty, each consisting of no more than 10 lowercase English letters.


-----Output-----

Output exactly n words: how you will record the lecture in your notebook. Output the words of the lecture in the same order as in the input.


-----Examples-----
Input
4 3
codeforces codesecrof
contest round
letter message
codeforces contest letter contest

Output
codeforces round letter round

Input
5 3
joll wuqrd
euzf un
hbnyiyc rsoqqveh
hbnyiyc joll joll euzf joll

Output
hbnyiyc joll joll un joll
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
n, m = map(int, input().split())
word_dict = {}
for _ in range(m):
    lang1, lang2 = input().split()
    word_dict[lang1] = lang2 if len(lang2) < len(lang1) else lang1

lecture = input().split()
notes = [word_dict[word] for word in lecture]
print(' '.join(notes))
#@!CODE END!@#
````

---

