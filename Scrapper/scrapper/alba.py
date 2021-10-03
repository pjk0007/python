import requests
from bs4 import BeautifulSoup as bs


def get_pages(url):
    result = requests.get(f"{url}")
    soup = bs(result.text, "html.parser")
    total_span = soup.find("span", {"class": "total"})
    total = int(total_span.find("em").text.replace(',', ''))

    return (total // 29) + 1


def extract_job(job):
    title = job.find("a")["title"]
    company = job.find("dt").contents[0]
    location = job.find("dd", {"class": "local"}).text
    link = job.find("a")["href"]

    return {'title': title,
            'company': company,
            'location': location,
            'link': f'{link}'}


def extract_jobs(url, last_page):
    jobs = []
    for page in range(1, last_page + 1):
        print(f"alba : Scrapping page {page}")
        result = requests.get(f"{url}&Page={page}")
        soup = bs(result.text, "html.parser")
        results = soup.find_all("div", {"class": "booth"})

        for result in results:  # results:
            job = extract_job(result)
            jobs.append(job)

    return jobs


def get_jobs(word):
    url = f"https://www.albamon.com/search/Recruit?Keyword={word}&PageSize=29"
    last_page = get_pages(url)

    jobs = extract_jobs(url, last_page)
    return jobs
