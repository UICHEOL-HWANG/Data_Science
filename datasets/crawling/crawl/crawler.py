

import requests as req
from typing import Dict

class Crawler:
    def __init__(self, base_url: str) -> Dict:
        self.base_url = base_url
        self.session = req.Session()


    def fetch_data(self, url: str, param=None) -> str:
        response = self.session.get(url, params=param)
        response.raise_for_status()

        return response.text