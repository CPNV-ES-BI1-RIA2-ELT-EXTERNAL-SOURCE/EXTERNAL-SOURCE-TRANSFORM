from app.services.data_transform_director import DataTransformDirector
from tests.data_example.transformated_data_example import get_transformated_data_example
from unittest.mock import patch
from tests.mocks.aws_provider_mock import AWSProviderMock


class TestTransform:

    @patch("app.services.cloud_provider_factory.CloudProviderFactory.get_cloud_provider")
    def test_transform_objects(self, mock_get_cloud_provider):
        # GIVEN
        awsProviderMock = AWSProviderMock()
        mock_get_cloud_provider.return_value = awsProviderMock

        response = DataTransformDirector().clean_station_departures(get_transformated_data_example())
        assert response == get_transformated_data_example()