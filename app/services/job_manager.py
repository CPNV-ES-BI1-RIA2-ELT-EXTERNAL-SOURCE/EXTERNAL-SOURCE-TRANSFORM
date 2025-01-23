import os
import json

class JobManager:

    @staticmethod
    def store_job(job_id: int, job_data: dict):
        if not os.path.exists("jobs"):
            os.makedirs("jobs")
        if JobManager.count_jobs() >= 1000:
            JobManager.remove_oldest_job()
        file = open(f"jobs/{job_id}.json", "w")
        file.write(json.dumps(job_data, indent=4))
        file.close()

    @staticmethod
    def get_job(job_id: int) -> dict:
        if not JobManager.is_existing_job(job_id):
            raise Exception(f"Job {job_id} does not exist")
        file = open(f"jobs/{job_id}.json", "r")
        data = json.loads(file.read())
        file.close()
        return data

    @staticmethod
    def is_existing_job(job_id: int) -> bool:
        return os.path.exists(f"jobs/{job_id}.json")

    @staticmethod
    def delete_job(job_id: int):
        if not JobManager.is_existing_job(job_id):
            raise Exception(f"Job {job_id} does not exist")
        os.remove(f"jobs/{job_id}.json")

    @staticmethod
    def reset_jobs():
        if not os.path.exists("jobs"):
            os.makedirs("jobs")
        for file in os.listdir("jobs"):
            os.remove(f"jobs/{file}")

    @staticmethod
    def count_jobs() -> int:
        return len(os.listdir("jobs"))

    @staticmethod
    def remove_oldest_job():
        if JobManager.count_jobs() == 0:
            return
        jobs = os.listdir("jobs")
        oldest_job = min(jobs, key=lambda job: os.path.getctime(f"jobs/{job}"))
        os.remove(f"jobs/{oldest_job}")