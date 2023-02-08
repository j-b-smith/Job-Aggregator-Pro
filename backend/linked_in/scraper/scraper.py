from constants.urls import *
import pip._vendor.requests as requests
from url_builder import get_job_search_url
from decouple import config

from bs4 import BeautifulSoup

def get_jobs():
    url = get_job_search_url(
        keyword="QA Automation Engineer",
        date_posted=PAST_24_HOURS,
        job_type=FULL_TIME,
        remote_status=REMOTE,
        min_salary=SALARY_100K
    )
    response = requests.get(url, auth=(config("LINKED_IN_EMAIL"), config("LINKED_IN_PASSWORD")))
    content = BeautifulSoup(response.content, "html.parser")