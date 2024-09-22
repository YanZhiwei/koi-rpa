from automations.zhipin import Zhipin


def main():
    zhipin = Zhipin("北京")
    result = zhipin.search("python")
    count: int = len(result)
    print(f"Found {count} jobs")
    add_jobs_count: int = 0
    exists_job_count: int = 0
    for job_summary in result:
        exist = exists_job(job_summary.id)
        if exist == False:
            job = zhipin.get_job(job_summary)
            if job.detail == None or job.detail == "":
                print(f"Job:{job_summary.id} detail is empty")
                continue
            create_job(job)
            create_job_boss(job)
            add_jobs_count += 1
            print(f"Job:{job_summary.id} added")
        else:
            print(f"Job:{job_summary.id} already exists")
            exists_job_count += 1
    print(f"Added {add_jobs_count} jobs,exist:{exists_job_count} jobs")
