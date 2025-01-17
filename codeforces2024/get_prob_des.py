import time

from DrissionPage import WebPage, ChromiumOptions
from loguru import logger
from bs4 import BeautifulSoup
import html2text

base_path = "/Users/anna/Documents/project/HoarePrompt-data/codeforces2024/newdata/"
banned_list = [1938, 1939, 1940, 1947, 1952, 1953, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 2015, 2016, 2052]

def remove_extra_blank_lines(markdown_text):
    lines = markdown_text.splitlines()
    cleaned_lines = []
    for line in lines:
        if not line.strip():
            if cleaned_lines and not cleaned_lines[-1].strip():
                continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def convert_html_to_markdown(html_doc, number, name):
    soup = BeautifulSoup(html_doc, 'html.parser')

    for tag in soup.select(".MathJax_Preview, .MJX_Assistive_MathML, span.MathJax"):
        tag.decompose()

    for script_tag in soup.find_all("script", attrs={"type": "math/tex"}):
        if script_tag.string:
            script_tag.replace_with(script_tag.string + " ")
        else:
            script_tag.decompose()

    problem_statement_div = soup.find("div", class_="problem-statement")
    if problem_statement_div:
        direct_child_divs = problem_statement_div.find_all("div", recursive=False)
        if direct_child_divs[0]:
            direct_child_divs[0].decompose()

        if len(direct_child_divs) > 4:
            sample_tests = direct_child_divs[4].find("div", class_="sample-test", recursive=False)
            if sample_tests:
                tests = sample_tests.find_all("div", recursive=False)
                for item in tests:
                    title = item.find("div", class_="title", recursive=False)
                    if title:
                        title_name = title.find(string=True, recursive=False)
                        if title_name:
                            title.replace_with(title_name.strip())

    h2t = html2text.HTML2Text()
    markdown_text = h2t.handle(str(soup))
    markdown_text = remove_extra_blank_lines(markdown_text)

    output_file_h = base_path + str(number) + "/" + name + ".html"
    output_file_m = base_path + str(number) + "/" + name + ".md"

    with open(output_file_h, "w", encoding="utf-8") as f:
        f.write(html_doc)
    with open(output_file_m, "w", encoding="utf-8") as f:
        f.write(markdown_text)


def main(number):
    basic_url = "https://codeforces.com/contest/"
    browser.get(basic_url + str(number))
    time.sleep(2)
    logger.info("Successfully loaded the page.")

    td_elements = browser.eles('x://td[contains(@class, "id") and contains(@class, "left")]')

    if not td_elements:
        print("No matching <td> elements found.")
        logger.warning("No matching <td> elements found.")
    else:
        print(f"Found {len(td_elements)} <td> elements.")
        logger.info(f"Found {len(td_elements)} matching <td> elements.")

        problem_name = []
        for i, td in enumerate(td_elements, start=1):
            td_text = td.text.strip()
            problem_name.append(td_text)

        for name in problem_name:
            print(name)
            new_url = basic_url + str(number) + "/problem/" + name
            browser.get(new_url)
            time.sleep(1)
            problem_div = browser.ele('x://div[@class="problem-statement"]')
            if problem_div:
                convert_html_to_markdown(problem_div.html, number, name)
            else:
                print("no")

co = ChromiumOptions()
co.headless(True)
co.set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
co.set_argument("--no-sandbox")
browser = WebPage('d', chromium_options=co)
for i in range(2052, 2054):
    if i in banned_list:
        continue
    main(i)
    print(i)
browser.close()
