import json
from typing import List, Dict, Any, Tuple


class Parser:
    # 상권 데이터 추출용 함수
    def fetch_bizdata(self, data: str) -> List[Dict[str, Any]]:
        try:
            # JSON 파싱
            main_data = json.loads(data)['body']['items']
            print(main_data)
            # 데이터 구조 확인 및 'body'와 'items' 추출
            return main_data
        except Exception as e:
            print(f'{e}')
        except KeyError as e:
            print(f'{e}')
        except json.JSONDecodeError as e:
            print(f'JSON 파싱 오류: {e}')
            return []