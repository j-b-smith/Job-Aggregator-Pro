from constants.urls import *

def get_job_search_url(
        keyword: str,
        date_posted: str = None,
        job_type: str = None,
        remote_status: str = None,
        min_salary: str = None
):
    param_string = ''
    args = locals()
    args.pop("keyword")
    for value in args.values():
        if value is not None:
            param_string += f"f_{value}&"

    return f"{SEARCH}{param_string}keywords={keyword.replace(' ', '%20')}"