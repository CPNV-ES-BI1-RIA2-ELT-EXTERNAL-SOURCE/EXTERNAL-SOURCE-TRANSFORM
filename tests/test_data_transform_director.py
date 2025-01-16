from unittest.mock import patch
from app.services.data_transform_director import DataTransformDirector
from tests.data_example.transformated_data_example import get_transformated_data_example
from tests.mocks.aws_provider_mock import AWSProviderMock


class TestDataTransformDirector:

    @patch("app.services.cloud_provider_factory.CloudProviderFactory.get_cloud_provider")
    def test_data_transform_director_transform_data_success(self, mock_get_cloud_provider):
        # GIVEN
        awsProviderMock = AWSProviderMock()
        mock_get_cloud_provider.return_value = awsProviderMock

        # WHEN
        result = DataTransformDirector.clean_station_departures("aws://path/to/objects")

        # THEN
        assert result == get_transformated_data_example()