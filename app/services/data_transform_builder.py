import json
from datetime import datetime
from typing import Optional

from app.errors import UnableToProcessError


class DataTransformBuilder:
    def __init__(self, input: dict):
        self._input = input
        self._output = {}
        with open("mapping.json", "r") as file:
            self.mapping = json.load(file)

    def build(self) -> dict:
        self._output = self._transform(self._input, self.mapping)
        return self._output

    def _transform(self, data: dict, mapping: list) -> dict:
        result = {}
        for map_item in mapping:
            try:
                origin = map_item["origin"]
                destination = map_item["destination"]
                value = self._get_value(data, origin)

                if "method" in map_item:
                    for method in map_item["method"]:
                        value = getattr(self, method)(value)

                if "child" in map_item:
                    if map_item["childType"]:
                        if map_item["childType"] == "object":
                            for item in value:
                                item = self._transform(item, map_item["child"])
                        elif map_item["childType"] == "array":
                            transformed_list = []
                            for item in value:
                                transformed_list.append(self._transform(item, map_item["child"]))
                            value = transformed_list
                    else:
                        value = self._transform(value, map_item["child"])

                if "list" in map_item:
                    transformed_list = []
                    for item in value:
                        transformed_list.append(item[map_item["list"]])
                    value = transformed_list

                self._set_value(result, destination, value)
            except Exception as e:
                raise UnableToProcessError()
        return result

    def _set_value(self, data: dict, path: str, value):
        keys = path.split('/')
        for key in keys[:-1]:
            if key not in data:
                data[key] = {}
            data = data[key]
        data[keys[-1]] = value

    def _get_value(self, data: dict, path: str):
        keys = path.split('/')
        for key in keys:
            if isinstance(data, list):
                data = [item.get(key) for item in data if key in item]
                if len(data) == 1:
                    data = data[0]
            elif key in data:
                data = data[key]
            else:
                return None
        return data

    @staticmethod
    def extract_sector(value: str) -> str:
        #split all first digits
        for index, char in enumerate(value):
            if not char.isdigit():
                return value[index:]
        return value

    @staticmethod
    def extract_platform(value: str) -> Optional[str]:
        #remove all first digits
        for index, char in enumerate(value):
            if not char.isdigit():
                return value[:index]
        return None

    @staticmethod
    def convert_date_to_timestamp(value: str) -> int:
        return int(datetime.strptime(value, "%Y-%m-%d %H:%M:%S").timestamp())
