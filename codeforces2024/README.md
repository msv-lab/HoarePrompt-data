# Codeforces 2024 Dataset Construction

## Data Selection Strategy

1. Include at least one (up to three) consecutive True/False code pairs.  
2. If available, include one code with a test passed rate of 50% (or close to 50% due to odd counts), and one code with only a single error point.

## Datasets

- **codeforces2024_172.json**: All collected data.  
- **codeforces2024_100wz6.json**: Randomly selected 100 problems, each containing exactly 3 True/False code pairs. 
- **codeforces2024_top100.json**: Problems with the most code samples (6 to 8 code pairs per problem).

## Format

Each problem contains a list comprising multiple dictionaries (each representing a solution sample for the problem) . **Ideally**, the data is like:

```python
[
  # ...
  [
    {
      # sample with 50% pass rate (if we have)
    },
    {
      # sample with almost 100% pass rate (if we have)
    },
    {
      # the correct sample of pair 1
    },
    {
      # the incorrect sample of pair 1
    },
    {
      # the correct sample of pair 2
    },
    {
      # the incorrect sample of pair 2
    },
    {
      # the correct sample of pair 3
    },
    {
      # the incorrect sample of pair 3
    }
  ],
  # ...
]
```

For a  **correct** code sample, it looks like:

```json
{
    "description": "...",
    "task_name": "1926_C",
    "dataset": "codeforces2024",
    "model": "human",
    "generated_code": "...",
    "correct": true,
    "task_id": "1926_C",
    "counterexample": null,
    "unique_id": "1926_C_vjudge.10_100%",
    "test_passed": 19
}
```

For an **incorrect** code sample, it looks like:

```json
{
    "description": "...",
    "task_name": "1926_C",
    "dataset": "codeforces2024",
    "model": "human",
    "generated_code": "...",
    "correct": false,
    "task_id": "1926_C",
    "counterexample": {
        "input": "7\r\n12\r\n1\r\n2\r\n3\r\n1434\r\n2024\r\n200000",
        "output": "4646667",
        "expected": "51\r\n1\r\n3\r\n6\r\n18465\r\n28170\r\n4600002"
    },
    "unique_id": "1926_C_vjudge.10_0.00%",
    "test_passed": 0
}
```

- unique_id:  `{contest number}_{problem letter}_{username}_{pass rate}`

## Scripts

- **data_crawler.py**: Crawls code and test information from Codeforces.
- **get_prob_des.py**: Crawls problem descriptions from Codeforces.

### **Potential Anti-Scraping Mechanisms**

1.	**Cloudflare CAPTCHA**: Solve the CAPTCHA manually by logging in before running the script.

2.	**Excessive access, network issues**: Reload the webpage manually if prompted.

3.	**High frequency of submission access, “time rate limit”**: Wait 10 minutes, delete cookies, re-login, and change the IP.

## Issues

1. There are too **few samples** with a test passed rate close to 50% or 100%. Only 26 out of 172 problems have one or two matching code submission records.

2. Complex anti-scraping mechanisms and long waiting times result in **a relatively small dataset**.

3. Apart from counterexamples, **no other methods are currently implemented** to highlight differences between True and False code samples.

4. From point 1, it is clear that there are almost no subtle modifications in the code samples.