from constants.urls import *


class SearchCriteria:
    def __init__(
        self,
        keyword: str,
        date_posted: str = None,
        job_type: str = None,
        remote_status: str = None,
        min_salary: str = None,
        job_id: str = None,
    ):
        self.keyword = keyword
        self.date_posted = date_posted
        self.job_type = job_type
        self.remote_status = remote_status
        self.min_salary = min_salary
        self.job_id = job_id


def get_job_search_url(search_criteria: SearchCriteria):
    keyword = search_criteria.keyword
    param_string = ""
    for key, value in search_criteria.__dict__.items():
        if key != "keyword":
            if value is not None:
                param_string += f"f_{value}&"

    return f"{SEARCH}{param_string}keywords={keyword.replace(' ', '%20')}"


def get_job_url_by_id(id: str):
    return f"{SEARCH}currentJobId={id}"


def next_page(url: str):
    next_page_url = url
    if JOB_NUMBER_START in url:
        job_num = int(url.split(JOB_NUMBER_START, 1)[1])
        next_page_url = f"{next_page_url.split(JOB_NUMBER_START)[0]}{JOB_NUMBER_START}{job_num + 25}"
    else:
        next_page_url += f"{JOB_NUMBER_START}25"
    return next_page_url
