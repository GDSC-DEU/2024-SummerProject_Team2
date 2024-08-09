import pandas as pd
from sqlalchemy import create_engine

# CSV 파일을 DataFrame으로 읽기
df = pd.read_csv('./dailytrash_part2.csv')

# MySQL 데이터베이스 연결
engine = create_engine('mysql+pymysql://root:1234@113.198.230.24:318/gdsc')

# DataFrame을 MySQL 테이블로 저장
df.to_sql('dailytrash2', con=engine, if_exists='append', index=False)
