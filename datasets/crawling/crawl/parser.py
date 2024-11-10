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

    def fetch_stats_tourist_data(self, data) -> List[Dict[str, Any]]:

        try:
            parse_data = xmltodict.parse(data)['response']['body']['items']['item']
            print(f'현재 {parse_data["natKorNm"]} 데이터 {parse_data["ym"]} 년어치 수집중 ..')
            return parse_data
        except KeyError as e:
            print(f'Parsing error - missing key {e}')
        except Exception as e:
            print(f'Unexpected error: {e}')

    def fetch_stats_detail_data(self, data) -> List[Dict[str, Any]]:
        try:
            parse_data = xmltodict.parse(data)['response']['body']['items']['item']
            print(f'현재 {parse_data["natKorNm"]}, 국가 데이터 중 {parse_data["ym"]} 년어치 {parse_data["age"]} 데이터 수집중 ..')
        except KeyError as e:
            print(f'Parsing error - missing key {e}')
        except Exception as e:
            print(f'Unexpected error: {e}')
