import pytest
from tests.data_example.initial_data_example import get_initial_data_example
from tests.data_example.json_object_example import get_json_object_example
from app.services.format_converter import FormatConverter
from app.errors.unknown_format_error import UnknownFormatError

# TODO NGY Be more explicit by mentioning the expected result (success -> my bad)
class TestFormatConverter:
    def test_format_converter_convert_json_success(self):
        # GIVEN
        data = get_json_object_example()
        converter = FormatConverter()
        # TODO NGY Validate the given (context)

        # WHEN
        result = converter.convert(data)

        # THEN
        assert result == get_initial_data_example()

    def test_format_converter_convert_unknown_format_failure(self):
        # GIVEN
        data = "InvalidFormat"
        converter = FormatConverter()

        # WHEN
        with pytest.raises(UnknownFormatError):
            converter.convert(data)