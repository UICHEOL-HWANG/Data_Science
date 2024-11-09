from crawl.crawler import Crawler
from crawl.parser import Parser

from dotenv import load_dotenv
from typing import List, Dict, Any
import os


class Controller:
    # 클래스 변수 초기화
    service_key = None
    user_agent = None

    def __init__(self):
        load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
        self.base_url = os.getenv('BASE_URL')
        self.crawler = Crawler(self.base_url)
        self.parser = Parser()

    @classmethod
    def load_service_key(cls):
        """API 키를 클래스 변수로 로드"""
        if cls.service_key is None:
            cls.service_key = os.getenv("serviceKey")
        return cls.service_key

    @staticmethod
    def insert_params(**kwargs) -> Dict[str, Any]:
        """동적 파라미터 생성"""
        params = {
            'serviceKey': Controller.load_service_key(),
        }
        params.update(kwargs)
        return params

    def fetch_data(self, urls: str, param: Dict=None, **kwargs) -> List[Dict[str, Any]]:
        """API 호출 및 데이터 파싱"""
        # 동적 파라미터 생성
        param = self.insert_params(**kwargs) if param is None else param

        # 데이터 수집 및 파싱
        raw_data = self.crawler.fetch_data(urls, param=param)
        return raw_data


# 메인 실행 코드
if __name__ == "__main__":
    controller = Controller()

    # 동적 파라미터 설정

    params = controller.insert_params(
        YM='202408',
        NAT_CD='112',
        ED_CD="E",
    )

    # 데이터 가져오기
    result = controller.fetch_data(urls=controller.base_url, **params)
    print(result)