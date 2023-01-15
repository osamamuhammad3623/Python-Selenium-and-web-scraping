import bs4
import requests

def get_html_code(link):
    raw_page = requests.get(link)

    # parsing/formatting the html
    return bs4.BeautifulSoup(raw_page.content, "lxml")

def extract_problems():
    soup = get_html_code(f"https://leetcode.com/problemset/all/")
    problem_rows = soup.find_all("div", {"role": "row"})

    problems = {}

    for row in problem_rows:
        problem_name = str() 
        problem_difficulty = str()

        # get problem name
        anchors = row.find_all("a")
        for a in anchors:
            if (a.text.strip() != ''):
                problem_name = a.text.strip()
        
        # get difficulty
        spans = row.find_all("span")
        for span in spans:
            span_text = span.text.strip()
            # if the text ends with %, then this is the acceptance percentage
            if (not span_text.endswith('%') and (span_text)):
                problem_difficulty = span_text
        
        problems[problem_name] = problem_difficulty

    return problems

all_problems = extract_problems()
for problem in all_problems:
    print(f"Problem: {problem}, difficulty: {all_problems[problem]}")

# note: first problem is not detected