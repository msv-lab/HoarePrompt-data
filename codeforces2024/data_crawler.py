import json
import os
import time
from DrissionPage import WebPage, ChromiumOptions
from loguru import logger

MAX_PAGE = 3

global base_url
file_path = "./test_js.json"
final_data = []
banned_list = [1938, 1939, 1940, 1947, 1952, 1953, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 2015, 2016, 2052]


def append_dict_to_json_list(new_dict):
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([new_dict], f, ensure_ascii=False, indent=4)
        print(f"create and add: {new_dict}")
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("JSON not a list.")
        except json.JSONDecodeError:
            data = []
        except ValueError as ve:
            print(f"error: {ve}")
            return
    data.append(new_dict)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"add dict: {new_dict}")


def get_correct_test_num(browser, sub_id):
    global base_url
    sub_url = base_url + "/submission/" + sub_id
    browser.get(sub_url, retry=3, interval=2, timeout=15)
    time.sleep(5)
    a_element = browser.ele('x://a[@class="click-to-view-tests" and text()="Click"]')
    if a_element:
        print(f"Found element: {a_element.text}, href: {a_element.attr('href')}")
        a_element.click()
        div_elements = browser.eles(
            'x://div[@class="roundbox borderTopRound" and @style="margin-top:2em;font-size:0.8em;"]')
        browser.back()
        return len(div_elements)
    else:
        print("Element not found.")
        browser.back()
        return 0


def create_data(browser, sub_id, task_id, flag, user_num, test_num, all_test_num, des):
    global base_url
    sub_url = base_url + "/submission/" + sub_id
    print(sub_url)
    browser.get(sub_url, retry=3, interval=2, timeout=15)
    time.sleep(5)
    print(browser.url)
    pre_tag = browser.ele('x://pre[@id="program-source-text"]')
    print(pre_tag)
    if pre_tag:
        single_line_text = pre_tag.text
        single_line_text.strip()
        if single_line_text == 'N/A':
            print("should wait")
            browser.wait(60)
            return "waiting"
        print("code in one line:\n")
        print(single_line_text)
    else:
        print("No pre text.")
        return None
    if flag:
        new_data = {
            "description": des,
            "task_name": task_id,
            "dataset": "codeforces2024",
            "model": "human",
            "generated_code": single_line_text,
            "correct": True,
            "task_id": task_id,
            "counterexample": None,
            "unique_id": task_id + "_" + user_num + "_100%",
            "test_passed": all_test_num
        }
        return new_data
    else:
        result = test_num / all_test_num
        percentage = result * 100
        formatted_percentage = f"{percentage:.2f}%"
        a_element = browser.ele('x://a[@class="click-to-view-tests" and text()="Click"]')
        if a_element:
            print(f"Found element: {a_element.text}, href: {a_element.attr('href')}")
            browser.run_js('arguments[0].click();', a_element)
            print("Triggered click event via JavaScript.")
            time.sleep(5)
            div_elements = browser.eles(
                'x://div[@class="roundbox borderTopRound" and @style="margin-top:2em;font-size:0.8em;"]')
            last_div = div_elements[-1]
            print("Found the last matching <div> element.")
            # print(last_div.html)
            input_div = last_div.ele('x:.//div[@class="file input-view"]//div[@class="text"]').text
            output_div = last_div.ele(
                'x:.//div[@class="file output-view"]//div[@class="text"]/pre[@class="output"]').text
            answer_div = last_div.ele(
                'x:.//div[@class="file answer-view"]//div[@class="text"]/pre[@class="answer"]').text
            new_data = {
                "description": des,
                "task_name": task_id,
                "dataset": "codeforces2024",
                "model": "human",
                "generated_code": single_line_text,
                "correct": False,
                "task_id": task_id,
                "counterexample": {
                    "input": input_div,
                    "output": output_div,
                    "expected": answer_div
                },
                "unique_id": task_id + "_" + user_num + "_" + formatted_percentage,
                "test_passed": test_num
            }
            return new_data
        else:
            print("Element not found.")
    return None


def get_code(browser, all_results, task_id, all_test_num, des):
    new_data_append = []
    print("get code")
    for key, value in all_results.items():
        print(f"{key}: {value}")
        ans = create_data(browser, value["submission_id"], task_id, value["correctness"], value["username"], value["test_number"], all_test_num, des)
        while ans == "waiting":
            ans = create_data(browser, value["submission_id"], task_id, value["correctness"], value["username"],
                              value["test_number"], all_test_num, des)
        new_data_append.append(ans)
    print("finish get code")
    append_dict_to_json_list(new_data_append)


def main(browser, contest_num):
    global base_url
    base_url = "https://codeforces.com/contest/" + str(contest_num)
    try:
        original_url = base_url + "/status"
        browser.get(original_url, retry=3, interval=2, timeout=15)

        completed_problems = []

        while True:
            problem_select = browser.ele('x://select[@id="frameProblemIndex"]')
            problem_options = problem_select.eles('x://option')

            for problem in problem_options:

                # choose a problem
                problem_value = problem.attr('value')
                if problem_value == "anyProblem" or problem_value in completed_problems:
                    continue
                problem.click()
                print(f"Selected Problem: {problem.text.strip()}")

                prob_data = {}
                test_total = 0

                # clear the participant name
                input_box = browser.ele('x://input[@id="participantSubstring"]')
                input_box.clear()
                input_box2 = browser.ele('x://input[@name="judgedTestCount"]')
                input_box2.clear()
                comparison_select = browser.ele('x://select[@id="comparisonType"]')
                equal_option = comparison_select.ele('x://option[@value="NOT_USED"]')
                equal_option.click()

                # choose the language
                python_option = browser.ele('x://select[@id="programTypeForInvoker"]/option[@value="python.3"]')
                python_option.click()
                print("Selected Language: Python 3")

                # -------------- step 1: find all users who get OK --------------
                happy_new_year_option = browser.ele(
                    'x://select[@id="verdictName"]/option[@value="OK"]')
                happy_new_year_option.click()
                print("Selected Verdict: Happy New Year!")
                # click the button to apply
                apply_button = browser.ele('x://input[@type="submit" and @value="Apply"]', timeout=3)
                apply_button.click()
                print("Form submitted.")
                browser.wait(5)
                # OK-users
                unique_users1 = set()
                # all the OK pages
                pagination_elements = browser.eles('x://div[@class="pagination"]//a[contains(@href, "page")]')
                if pagination_elements:
                    max_page = max(int(elem.text) for elem in pagination_elements if elem.text.isdigit())
                else:
                    max_page = 1
                print(f"Total pages found: {max_page}")
                # go through all the OK pages
                first_row = browser.ele(
                    'x://table[@class="status-frame-datatable"]/tbody/tr[not(contains(@class, "first-row"))]')
                if first_row and first_row.text == "No items":
                    completed_problems.append(problem_value)
                    print("completed_problems(no item):", completed_problems)
                    break
                for page in range(1, min(MAX_PAGE, max_page + 1)):
                    print(f"Processing page {page}...")
                    if max_page > 1:
                        page_url = f"{original_url}/page/{page}?order=BY_ARRIVED_DESC"
                        browser.get(page_url, retry=3, interval=2, timeout=15)
                    browser.wait(5)
                    user_elements = browser.eles(
                        'x://table[@class="status-frame-datatable"]//a[contains(@class, "rated-user")]')
                    try:
                        for user_element in user_elements:
                            username = user_element.text.strip()
                            unique_users1.add(username)
                    except Exception as e:
                        print("no user:", e)
                    if page == 1:
                        first_row = browser.ele(
                            'x://table[@class="status-frame-datatable"]/tbody/tr[not(contains(@class, "first-row"))]')
                        first_correct_id = first_row.attr('data-submission-id')
                        user_element = browser.ele(
                            'x://table[@class="status-frame-datatable"]//a[contains(@class, "rated-user")]')
                        username = user_element.text.strip()
                        test_total = get_correct_test_num(browser, first_correct_id)
                        prob_data.update({
                            str(contest_num) + "_" + first_correct_id:
                                {
                                    "username": username,
                                    "submission_id": first_correct_id,
                                    "test_number": test_total,
                                    "correctness": True
                                }
                        })
                        print("test total: " + str(test_total))
                # -------------- step 2: find all users who get Wrong --------------
                wrong_option = browser.ele(
                    'x://select[@id="verdictName"]/option[@value="WRONG_ANSWER"]')
                wrong_option.click()
                print("Selected Verdict: wrong")
                # click the button to apply
                apply_button = browser.ele('x://input[@type="submit" and @value="Apply"]', timeout=3)
                apply_button.click()
                print("Form submitted.")
                browser.wait(5)
                # wrong-users
                unique_users_2 = set()
                # all the wrong pages
                pagination_elements = browser.eles('x://div[@class="pagination"]//a[contains(@href, "page")]')
                if pagination_elements:
                    max_page = max(int(elem.text) for elem in pagination_elements if elem.text.isdigit())
                else:
                    max_page = 1
                print(f"Total pages found: {max_page}")
                # go through all the wrong pages
                for page in range(1, min(MAX_PAGE, max_page + 1)):
                    print(f"Processing page {page}...")
                    if max_page > 1:
                        page_url = f"{original_url}/page/{page}?order=BY_ARRIVED_DESC"
                        browser.get(page_url, retry=3, interval=2, timeout=15)
                    user_elements = browser.eles(
                        'x://table[@class="status-frame-datatable"]//a[contains(@class, "rated-user")]')
                    for user_element in user_elements:
                        username = user_element.text.strip()
                        unique_users_2.add(username)
                # the users with TF pairs
                unique_users = unique_users1 & unique_users_2
                print(f"Total unique users found: {len(unique_users)}")
                # step 3: choose with 50% and almost 100%
                browser.get(original_url, retry=3, interval=2, timeout=15)
                check_list = []
                if test_total == 1:
                    check_list.append(1)
                elif test_total == 2:
                    check_list.append(2)
                else:
                    check_list.append(int(test_total/2)+1)
                    check_list.append(test_total)
                print(check_list)
                # go thourgh check
                for check in check_list:
                    print(check)
                    new_unique = set()
                    input_box = browser.ele('x://input[@name="judgedTestCount"]')
                    input_box.clear()
                    input_box.input(str(check))
                    comparison_select = browser.ele('x://select[@id="comparisonType"]')
                    equal_option = comparison_select.ele('x://option[@value="EQUAL"]')
                    equal_option.click()
                    submit_button = browser.ele('x://input[@type="submit" and @value="Apply"]')
                    submit_button.click()
                    print(browser.url)
                    first_row = browser.ele(
                        'x://table[@class="status-frame-datatable"]/tbody/tr[not(contains(@class, "first-row"))]')
                    if first_row and first_row.text != "No items":
                        submission_id = first_row.attr('data-submission-id')
                        user_element = browser.ele(
                            'x://table[@class="status-frame-datatable"]//a[contains(@class, "rated-user")]')
                        username = user_element.text.strip()
                        print(submission_id, username)
                        prob_data.update({
                            str(contest_num) + "_" + submission_id:
                                {
                                    "username": username,
                                    "submission_id": submission_id,
                                    "test_number": check-1,
                                    "correctness": False
                                }
                        })
                print("finished")
                # go through all the users
                number_second_data = 0
                for username in unique_users:
                    print(username)
                    if number_second_data == 3:
                        break
                    browser.wait(5)
                    print(f"Processing user: {username}")
                    input_box = browser.ele('x://input[@id="participantSubstring"]')
                    if input_box:
                        input_box.clear()
                        input_box.input(username)

                        any_verdict_option = browser.ele(
                            'x://select[@id="verdictName"]/option[@value="anyVerdict"]')
                        any_verdict_option.click()
                        print("Selected Verdict: any Verdict")

                        input_box2 = browser.ele('x://input[@name="judgedTestCount"]')
                        input_box2.clear()

                        comparison_select = browser.ele('x://select[@id="comparisonType"]')
                        equal_option = comparison_select.ele('x://option[@value="NOT_USED"]')
                        equal_option.click()

                        submit_button = browser.ele('x://input[@type="submit" and @value="Apply"]')
                        if submit_button:
                            submit_button.click()
                            print(f"Submitted for user: {username}")
                            rows = browser.eles(
                                'x://table[@class="status-frame-datatable"]/tbody/tr[not(contains(@class, "first-row"))]')
                            ok_submission_id = None
                            # go through all the submissions of this user
                            for row in rows:
                                if not ok_submission_id: # find the first ok submission
                                    verdict_cell = row.ele('x:.//td[contains(@class, "status-verdict-cell")]')
                                    if verdict_cell and "Happy New Year!" in verdict_cell.text:
                                        ok_submission_id = row.attrs.get("data-submission-id")
                                        print(f"Found 'OK': submission_id={ok_submission_id}")
                                else:
                                    verdict_cell = row.ele('x:.//td[contains(@class, "status-verdict-cell")]')
                                    if verdict_cell and ("Wrong answer on test" in verdict_cell.text or "Wrong answer on pretest" in verdict_cell.text):
                                        wrong_submission_id = row.attrs.get("data-submission-id")
                                        wrong_submission_name = str(contest_num) + "_" + wrong_submission_id
                                        wrong_test_number = verdict_cell.ele('x:.//span[@class="verdict-format-judged"]').text
                                        print(f"Found 'Wrong answer on test': submission_id={wrong_submission_id}, test_number={wrong_test_number}")
                                        print(prob_data)
                                        try:
                                            if str(contest_num) + "_" + ok_submission_id not in prob_data and wrong_submission_name not in prob_data:
                                                prob_data.update({
                                                    str(contest_num) + "_" + ok_submission_id: {
                                                        "username": username,
                                                        "submission_id": ok_submission_id,
                                                        "test_number": test_total,
                                                        "correctness": True
                                                    }
                                                })
                                                prob_data.update({
                                                    wrong_submission_name: {
                                                        "username": username,
                                                        "submission_id": wrong_submission_id,
                                                        "test_number": int(wrong_test_number) - 1,
                                                        "correctness": False
                                                    }
                                                })
                                                print("Update successful!")
                                                number_second_data += 1
                                                print(number_second_data)
                                                break
                                        except Exception as e:
                                            print(f"Error during prob_data.update(): {e}")
                        else:
                            print(f"Submit button not found for user: {username}")
                    else:
                        print(f"Input box not found for user: {username}")

                print("\nResults:")
                print(prob_data)
                md_file_path = "/Users/anna/Documents/project/HoarePrompt-data/codeforces2024/newdata/" + str(contest_num) + "/" + problem_value + ".md"
                with open(md_file_path, "r", encoding="utf-8") as md_file:
                    description = md_file.read().strip()

                get_code(browser, prob_data, str(contest_num) + "_" + problem_value, test_total, description)

                completed_problems.append(problem_value)
                print("completed_problems:", completed_problems)

                browser.get(original_url)
                print("Returned to original page.")
                break

            else:
                print("All problems processed.")
                break
    except Exception as e:
        print("can go", e)


co = ChromiumOptions()
co.set_argument("--no-sandbox")
# co.set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

new_browser = WebPage('d', chromium_options=co)
for i in range(1974, 2054):
    if i in banned_list:
        continue
    main(new_browser, i)
new_browser.close()
