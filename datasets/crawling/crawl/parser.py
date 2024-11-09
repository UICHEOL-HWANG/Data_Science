import json
import xmltodict
from typing import List, Dict, Any

class Parser:

    def fetch_tourist_data(self, data) -> List[Dict[str, Any]]:
        """관광 데이터를 파싱하고 리스트에 추가"""

        try:
            # XML 파싱
            main_data = xmltodict.parse(data)['response']['body']['items']['item']
            return main_data
        except KeyError as e:
            print(f"Parsing error - missing key {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

