
import json
from time import sleep

import requests

from automations.zhipin import Zhipin
from models.job import Job


def exists_job(job_id: str) -> bool:
    url = f"http://127.0.0.1:8000/jobs/{job_id}"

    payload = {}
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            return False
        else:
            print(f"Failed to get job:{e}")
    return True


def create_job(job: Job):
    try:
        url = "http://127.0.0.1:8000/jobs/"
        payload =  json.dumps({
  "id": job.summary.id,
  "detail": job.detail,
  "posted_date": job.posted_date,
  "title": job.summary.name,
  "url": job.summary.url,
  "company": job.summary.company,
  "area": job.summary.area,
  "tags": job.summary.tags,
  "salary": job.summary.salary,
  "search_keywords": job.summary.language,
  "boss_name": job.boss.name,
  "boss_title": job.boss.title,
  "boss_active_state": job.boss.active_state
} ,ensure_ascii=False)
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to create job:{e}")


def main():
    zhipin = Zhipin("北京",True)
    zhipin.chat_input("https://www.zhipin.com/job_detail/9577992d204093ea0XF73d-5Flo~.html?securityId=OjIYLH-TsU9K1-01TGb32qbqAb4HoizOUpf1kozEaNBtIQe7wowWrKXjQvqvAJsDYKj7wN4-YwlxkJ7LLoCnZmeoY6MgdQER9vVq1a4TyrpjvighwZwH","python")
    sleep(10)
    # result = zhipin.search("python")
    # count: int = len(result)
    # print(f"Found {count} jobs")
    # add_jobs_count: int = 0
    # exists_job_count: int = 0
    # for job_summary in result:
    #     exist = exists_job(job_summary.id)
    #     if exist == False:
    #         job = zhipin.get_job(job_summary)
    #         if job.detail == None or job.detail == "":
    #             print(f"Job:{job_summary.id} detail is empty")
    #             continue
    #         create_job(job)
    #         add_jobs_count += 1
    #         print(f"Job:{job_summary.id} added")
    #     else:
    #         print(f"Job:{job_summary.id} already exists")
    #         exists_job_count += 1
    # print(f"Added {add_jobs_count} jobs,exist:{exists_job_count} jobs")


if __name__ == "__main__":
    main()
