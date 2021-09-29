import requests
from bs4 import BeautifulSoup as bs

indeed_result = requests.get(
    "https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit=50")

indeed_soup = bs(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all('a')

spans = []
for page in pages:
    spans.append(page.find("span"))
spans = spans[:-1]
print(spans)
