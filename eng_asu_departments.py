import bs4
import requests

def get_html_code(link):
    raw_page = requests.get(link)

    # parsing/formatting the html
    return bs4.BeautifulSoup(raw_page.content, "lxml")

def extract_departments():
    html = get_html_code("https://eng.asu.edu.eg/departments")
    all_h4_titles = html.find_all("h4")
    
    all_anchors = []
    for h4 in all_h4_titles:
        all_anchors.append(h4.find("a"))
    
    dep = []
    for a in all_anchors:
        dep.append(a.text.strip())
    
    return dep

print("Departments in ENG-ASU :")
for dep in extract_departments():
    print(dep)