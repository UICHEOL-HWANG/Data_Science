import json
from typing import List, Dict, Any


class Parser:
    # 상권 데이터 추출용 함수
    def fetch_bizdata(self, data: str) -> List[Dict[str, Any]]:
        try:
            # JSON 파싱
            main_data = json.loads(data)

            # 데이터 구조 확인 및 'body'와 'items' 추출
            if 'body' in main_data and 'items' in main_data['body']:
                return main_data['body']['items']
            else:
                print('데이터가 없습니다. "body" 또는 "items" 키가 누락되었습니다.')
                return []

        except json.JSONDecodeError as e:
            print(f'JSON 파싱 오류: {e}')
            return []