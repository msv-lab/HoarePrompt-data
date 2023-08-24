# Question: 4862
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
Virtually every single book, play, movie, novel, and game has at least one character. Most have more, and some even have thousands! As every good writer knows, the difficulty of creating a character increases with each new major character added. This is because fictional characters are truly developed through their relationships with others.

If there are no characters or only one character, no relationships need to be explored. With two characters, there is one relationship. If there are three characters, however, there are four relationships: the ones between each pair of characters, and finally the relationship when all three are together. In general, the relationship between all subsets of at least two characters must be explored.

Given a literary work with $N$ characters, how many relationships need to be explored?

-----Input-----
The input contains a single integer, $N$ ($0 \leq N \leq 30$), the number of characters.

-----Output-----
Output a single line with the number of relationships that need to be explored.

-----Examples-----
Sample Input:
1
Sample Output:
0
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
N = int(input())

if N == 0 or N == 1:
    print(0)
else:
    relationships = (2 ** N) - N - 1
    print(relationships)
#@!CODE END!@#
````

---

