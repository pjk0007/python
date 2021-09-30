import requests
from bs4 import BeautifulSoup as bs

INDEED_URL = "https://kr.indeed.com/취업?q=python&limit=50"


def get_pages():
    result = requests.get(f"{INDEED_URL}&start=9999999")
    soup = bs(result.text, "html.parser")
    pagination = soup.find("ul", {"class": "pagination-list"})
    last_page = int(pagination.find('b').text)

    return last_page


def extract_job(job):
    title = job.find("h2").find_all("span")[-1].string
    company_location = job.find(
        "div", {"class": "heading6 company_location tapItem-gutter"})
    company = company_location.find(
        "span", {"class": "companyName"})
    location = company_location.find(
        "div", {"class": "companyLocation"})

    if location:
        location = location.string
    else:
        location = None

    if company:
        company = company.string
    else:
        company = None

    job_id = job["data-jk"]

    return {'title': title,
            'company': company,
            'location': location,
            'link': f'https://kr.indeed.com/취업?jk={job_id}'}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"indeed : Scrapping page {page + 1}")
        result = requests.get(f"{INDEED_URL}&start={page*50}")
        soup = bs(result.text, "html.parser")
        results = soup.find_all("a", {"class": "tapItem"})

        for result in results:  # results:
            job = extract_job(result)
            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_pages()

    jobs = extract_jobs(last_page)

    return jobs
