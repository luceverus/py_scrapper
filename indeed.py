import requests
from bs4 import BeautifulSoup

LIMIT = 5
URL = f'https://kr.indeed.com/취업?q=파이썬&limit={LIMIT}'


def extract_indeed_pages():
    html = requests.get(URL)

    soup = BeautifulSoup(html.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find('a')["title"]
    company = html.find("span", {"class": "company"})
    location = html.find("div", {"class": "recJobLoc"})['data-rc-loc']
    company_anchor = company.find('a')
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    return {'title': title, 'company': company, 'location': location}


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
        jobs.append(extract_job(result))
    return jobs
