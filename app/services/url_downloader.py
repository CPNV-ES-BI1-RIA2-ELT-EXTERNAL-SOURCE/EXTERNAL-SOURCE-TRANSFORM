import requests

class UrlDownloader:

    @staticmethod
    def download(url: str):
        return requests.get(url).text