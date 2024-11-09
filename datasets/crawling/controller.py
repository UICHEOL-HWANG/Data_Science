from crawl.crawler import Crawler
from crawl.parser import Parser

from dotenv import load_dotenv
from typing import List, Dict, Any
import os

import psycopg2
import pandas as pd
import xmltodict
import itertools

from sqlalchemy import create_engine



class Controller:
    # 클래스 변수 초기화
    service_key = None
    user_agent = None

    def __init__(self):
        load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
        self.base_url = os.getenv('BASE_URL')
        self.crawler = Crawler(self.base_url)
        self.parser = Parser()
        self.data_lst = []


    @classmethod
    def load_to_psycopg(cls):
        """ postgresql connetions"""
        cls.user = os.getenv('POSTGRES_USER')
        cls.password = os.getenv('POSTGRES_PASSWORD')
        cls.host = os.getenv('POSTGRES_HOST')
        cls.port = os.getenv('POSTGRES_PORT')
        cls.database = os.getenv('POSTGRES_DATABASE')

        return create_engine(
            f'postgresql://{cls.user}:{cls.password}@{cls.host}:{cls.port}/{cls.database}'
        )


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
        data_lst = self.data_lst
        param = self.insert_params(**kwargs) if param is None else param

        # 데이터 수집 및 파싱
        crawling = self.crawler.fetch_urls(urls, param=param)
        print(crawling)
        parsed_data = self.parser.fetch_tourist_data(crawling)
        print(parsed_data)

        data_lst.append(parsed_data)
        return data_lst


# 메인 실행 코드
if __name__ == "__main__":
    controller = Controller()
    engine = controller.load_to_psycopg()

    months = [f'2023{mth:02}' for mth in range(1, 13)]
    gender = ['M', 'F']
    ages = [x for x in range(10, 90, 10)]


    # 동적 파라미터 설정

    param_combinations = itertools.product(months, gender, ages)
    # 3중 루프 피하기 위해 사용
    for month, sex, age in param_combinations:
        params = controller.insert_params(
            YM=month,
            SEX_CD=sex,
            AGE_CD=age,
            PORT_CD='IA'
        )

        # 데이터 가져오기
        controller.fetch_data(urls=controller.base_url, **params)

    if controller.data_lst:
        data = pd.DataFrame(controller.data_lst)

        try:
            data.to_sql('tourist_domestic',
                con=engine,
                if_exists='append',
                schema='public',  # Update to the correct schema
                index=False
            )
            print(f"Data for {month}, {sex}, {age} saved successfully.")

        except Exception as e:
            print(f"Error saving data for {month}, {sex}, {age}: {e}")