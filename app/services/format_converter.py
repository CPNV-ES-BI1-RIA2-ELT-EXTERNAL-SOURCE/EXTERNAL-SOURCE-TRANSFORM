import json
import re
from app.errors import UnknownFormatError

class FormatConverter:
    def convert(self, stream: str) -> dict:
        type = self._get_file_format_type(stream)
        if type == 'unknown':
            raise UnknownFormatError(f"Unknown format for stream: {stream}")
        return getattr(self, f"_convert_{type}")(stream)

    def _convert_json(self, stream: str) -> dict:
        return json.loads(stream)

    def _get_file_format_type(self, stream: str) -> str:
        if re.match(r'^\s*(\{(?:[^{}]|".*?")*\}|\[(?:[^\[\]]|".*?")*\])\s*$', stream, re.DOTALL):
            return 'json'
        return 'unknown'
