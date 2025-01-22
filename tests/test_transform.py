from app.services.data_transform_director import DataTransformDirector
from app.services.job_manager import JobManager
from tests.data_example.initial_data_example import get_initial_data_example
from tests.data_example.transformated_data_example import get_transformated_data_example
from unittest.mock import patch, MagicMock


class TestTransform:

    def setup_method(self):
        JobManager.reset_jobs()

    @patch("app.services.data_transform_director.UrlDownloader.download")
    def test_data_transform_director_transform_data_success(self, mock_download):
        # GIVEN
        mock_response = MagicMock()
        mock_response.json.return_value = get_initial_data_example()
        mock_download.return_value = mock_response

        # WHEN
        DataTransformDirector.transform_job_data(1, "https://path/to/objects")

        # THEN
        assert JobManager.get_job(1) == get_transformated_data_example()