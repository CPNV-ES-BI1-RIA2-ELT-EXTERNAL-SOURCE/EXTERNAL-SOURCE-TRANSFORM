from app.services.cloud_provider import CloudProvider
from tests.data_example.json_object_example import get_json_object_example
from app.services.format_converter import FormatConverter

class AWSProviderMock(CloudProvider):
    def __init__(self):
        super().__init__()
        self.data = get_json_object_example()
        self.format_converter = FormatConverter()

    def download(self, path: str) -> dict:
        return self.format_converter.convert(self.data)

    def _connect(self):
        pass

    def _disconnect(self):
        pass