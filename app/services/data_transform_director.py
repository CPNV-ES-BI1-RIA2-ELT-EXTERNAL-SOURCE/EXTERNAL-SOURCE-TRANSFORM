from app.services.data_transform_builder import DataTransformBuilder
from app.services.job_manager import JobManager
from app.services.url_downloader import UrlDownloader


class DataTransformDirector:

    @staticmethod
    def transform_job_data(job_id: int, data_uri: str) -> None:
        if not JobManager.is_existing_job(job_id):
            data = DataTransformDirector._download_data(data_uri)
            data_transform_builder = DataTransformBuilder(data)
            transformed_data = data_transform_builder.set_initial_station().set_departures().build()
            JobManager.store_job(job_id, transformed_data)

    @staticmethod
    def download_job_data(path: str) -> dict:
        if JobManager.is_existing_job(path):
            return DataTransformDirector._load_job_data(path)
        else:
            raise Exception(f"Job {path} does not exist")

    @staticmethod
    def _download_data(path) -> dict:
        return UrlDownloader().download(path).json()

    @staticmethod
    def _load_job_data(path) -> dict:
        return JobManager.get_job(path)