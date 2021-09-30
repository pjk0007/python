import requests
from bs4 import BeautifulSoup as bs

INDEED_URL = "https://www.albamon.com/search/Recruit?Keyword=개발자&PageSize=29"


def get_pages():
    result = requests.get(f"{INDEED_URL}")
    soup = bs(result.text, "html.parser")
    total_span = soup.find("span", {"class": "total"})
    total = int(total_span.find("em").text.replace(',', ''))

    return (total // 29) + 1


def extract_job(job):
    title = job.find("a")["title"]
    company = job.find("dt").contents[0]
    location = job.find("dd", {"class": "local"})
    link = job.find("a")["href"]

    return {'title': title,
            'company': company,
            'location': location,
            'link': f'{link}'}


def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page + 1):
        print(f"alba : Scrapping page {page}")
        result = requests.get(f"{INDEED_URL}&Page={page}")
        soup = bs(result.text, "html.parser")
        results = soup.find_all("div", {"class": "booth"})

        for result in results:  # results:
            job = extract_job(result)
            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_pages()

    jobs = extract_jobs(last_page)
    return jobs
