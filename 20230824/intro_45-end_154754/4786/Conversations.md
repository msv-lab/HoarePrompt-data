# Question: 4786
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
Catherine is a brilliant software engineer, but she has been having difficulty landing a job, despite having submitted a superb resume to dozens of tech companies. After doing some research, she discovered that most tech companies in her area use an algorithm to prescreen resumes by scanning for certain keywords before the resume is even seen by a human. Any resume that does not contain sufficiently many technology-related keywords is automatically rejected!

Catherine has devised a plan to outwit the prescreening algorithm: she intends to cram as many keywords as possible into her resume to maximize her chances of passing the prescreening process. As a first step, she has downloaded a list of the most common tech buzzwords from an online data bank that includes entries such as “machine learning”, “Big data”, “AI”, “C++”, “Neural-network”, “unix”, “cryptography”, etc. (Note that keyword sometimes really means keyphrase.)

In the early stages of drafting her new resume, Catherine notices that many keywords from the data bank are very similar to each other (e.g., “Machine-learning” vs. “machine learning”, or “MySQL” vs. “MySql”). Since she suspects that including nearly identical keywords won’t help her fool the prescreening algorithm, she wants to filter out such similar keywords in order to save room on her resume. Catherine considers two keywords $k_1$ and $k_2$ to be similar if, after replacing hyphens with spaces and ignoring capitalization, $k_1$ is the same as $k_2$.

Can you help Catherine craft the perfect resume to land her a job?

-----Input-----
The first line contains an integer, $n$ $(1 \leq n \leq 40000)$, the number of keywords in the data bank. This is followed by $n$ lines, each of which contains a keyword string $k$ that is between $1$ and $25$ characters in length (inclusive). All characters in a keyword are guaranteed to fall in the $[32, 126]$ ASCII range, and no keyword begins or ends with a space or a hyphen.

-----Output-----
Output a single line containing the number of (pairwise) non-similar keywords in the data bank.

-----Examples-----
Sample Input 1:
4
c++
C++
c
c#
Sample Output 1:
3

Sample Input 2:
5
cryptography
blockchain
Artificial intelligence
Machine-Learning
Linux
Sample Output 2:
5
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

def filter_keywords(n, keywords):
    filtered_keywords = set()
    for keyword in keywords:
        normalized_keyword = keyword.lower().replace("-", " ")
        filtered_keywords.add(normalized_keyword)
    return len(filtered_keywords)

# Read input
n = int(input())
keywords = [input() for _ in range(n)]

# Call the function to get the result
result = filter_keywords(n, keywords)

# Print the result
print(result)

#@!CODE END!@#
````

---

