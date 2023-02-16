import pip._vendor.requests as requests
from constants.urls import *
from constants.selectors import *
from url_builder import *
from decouple import config

from bs4 import BeautifulSoup, Tag

client = requests.Session()


def login_to_linked_in(client):
    LOGIN_URL = "https://www.linkedin.com/uas/login"
    content = BeautifulSoup(requests.get(LOGIN_URL).content, "html.parser")
    login_csrf_param = content.find("input", {"name": "loginCsrfParam"})["value"]
    body = {
        "session_key": config("LINKED_IN_EMAIL"),
        "session_password": config("LINKED_IN_PASSWORD"),
        "loginCsrfParam": login_csrf_param,
    }

    response = client.post(LOGIN_URL + "-submit", data=body)
    csrf_token = BeautifulSoup(response.content, "html.parser").find(
        "input", {"name": "csrfToken"}
    )["value"]
    print(f"Login Response Code: {response.status_code}")
    return csrf_token


def get_job_ids(content: BeautifulSoup) -> list[str]:
    separator = "urn:li:jobPosting:"
    id_elements = content.find_all("div", attrs={JOB_ID: True})
    return [o[JOB_ID].replace(separator, "") for o in id_elements]


def get_num_jobs(content: BeautifulSoup) -> int:
    return int(content.find("code", {"id": "totalResults"}).next)


def get_number_of_pages(content: BeautifulSoup) -> int:
    num_jobs = get_num_jobs(content=content)
    # print(f"Num Jobs: {num_jobs}")
    num_pages = num_jobs // 25
    # print(f"Num Pages: {num_pages}")
    if num_jobs % 25 != 0:
        num_pages += 1
    return num_pages


def get_page_content(url: str) -> BeautifulSoup:
    response = client.get(url)
    # print(f"Get Page Content Response: {response.status_code}")
    return BeautifulSoup(response.content, "html.parser")


def get_job_urls(search: SearchCriteria):
    url = get_job_search_url(search)
    content = get_page_content(url)
    num_pages = get_number_of_pages(content=content)
    job_ids = []
    job_urls = []
    for i in range(num_pages):
        job_ids += get_job_ids(content)
        print(f"Page {i} ID's: \n {job_ids}")
        if i != 0:
            url = next_page(url=url)
            content = get_page_content(url)

    for id in job_ids:
        job_urls.append(get_job_url_by_id(id))

    # Remove duiplicate URL's
    job_urls = list(set(job_urls))

    return job_urls


def search_jobs(search: SearchCriteria):
    urls = get_job_urls(search=search)
    return urls


urls = search_jobs(
    SearchCriteria(
        keyword="qa engineer",
        date_posted=PAST_WEEK,
        job_type=FULL_TIME,
        remote_status=REMOTE,
        min_salary=SALARY_100K,
    )
)

# print(urls)
# print(f"Length of URL array: {len(urls)}")
