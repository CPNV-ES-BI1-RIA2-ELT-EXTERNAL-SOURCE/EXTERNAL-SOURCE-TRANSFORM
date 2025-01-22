from app.services.data_transform_builder import DataTransformBuilder
from app.services.format_converter import FormatConverter
from app.services.job_manager import JobManager
from app.services.url_downloader import UrlDownloader


class DataTransformDirector:

    @staticmethod
    def transform_job_data(job_id: int, data_uri: str) -> None:
        if not JobManager.is_existing_job(job_id):
            data = DataTransformDirector._download_data(data_uri)
            data_transform_builder = DataTransformBuilder(data)
            transformed_data = data_transform_builder.build()
            JobManager.store_job(job_id, transformed_data)

    @staticmethod
    def download_job_data(job_id: int) -> dict:
        if JobManager.is_existing_job(job_id):
            return DataTransformDirector._load_job_data(job_id)
        else:
            raise Exception(f"Job {job_id} does not exist")

    @staticmethod
    def _download_data(path) -> dict:
        data = UrlDownloader.download(path)
        format_converter = FormatConverter()
        return format_converter.convert(data)

    @staticmethod
    def _load_job_data(job_id: int) -> dict:
        return JobManager.get_job(job_id)