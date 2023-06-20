import pandas as pd
import streamlit as st

# 读取CSV文件
df = pd.read_csv('./test-files/test.csv')

# 在Streamlit应用程序中展示数据
st.dataframe(df)

from sqlalchemy import create_engine, text

db_type = 'mysql+pymysql'
db_name = 'eiz_test'
db_user = 'viewuser'
db_passwd = ')5y)JHhqsFulugU!'
db_host = 'master.ccub4ta9krao.ap-southeast-2.rds.amazonaws.com'
db_port = 3306

connect_args = {
                'connect_timeout': 60,
                'read_timeout': 90
                }

engine = create_engine(f'{db_type}://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}',connect_args = connect_args)

query = 'select id, email, sales from accounts where id in ( 79, 277, 285, 2333 )'
with engine.connect() as con:
    df1 = pd.read_sql_query(query,con)
# 在Streamlit应用程序中展示数据
st.dataframe(df1)