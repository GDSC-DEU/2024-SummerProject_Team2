import pandas as pd
from sqlalchemy import create_engine

# CSV 파일을 DataFrame으로 읽기
df = pd.read_csv('./battery.csv')

# MySQL 데이터베이스 연결
engine = create_engine('mysql+pymysql://root:@localhost:3306/gdsc')

# DataFrame을 MySQL 테이블로 저장
df.to_sql('battery', con=engine, if_exists='append', index=False)
