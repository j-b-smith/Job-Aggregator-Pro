TOTAL_RESULTS = {"t-normal": "small", "jobs-search-results-list__text": "small"}
JOB_CARDS = {"jobs-search-results__list-item": "li"}
COMPANY_NAME = {"jobs-unified-top-card__company-name": "span"}
JOB_TITLE = {"jobs-unified-top-card__job-title": "h2"}
JOB_HEADER_INFO = {"jobs-unified-top-card__job-insight": "li"}
EASY_APPLY_BUTTON = {"Easy Apply": "span"}
JOB_DESCRIPTION = {"jobs-description-content__text": "div"}
COMPANY_LOGO = {"img[title]"}

def COMPANY_LOGO (company_name: str): 
    return {f'img[title="{company_name}"]'}