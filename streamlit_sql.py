import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd

# conn = st.experimental_connection('eiz_test', type='sql')

# # View the connection contents.
# conn

# a = conn.query('select id, companyName, email, credit, balance from accounts where id not in (1,284,317,513,911,2333,4832,1978,2677,3430,3793,3980,5474,5906,6572,6484,6681,6682,6684,6728,6734,6735) and credit > 0;',ttl=600)
# st.dataframe(a,hide_index=True)


engine = create_engine("mysql+mysqldb://viewuser:)5y)JHhqsFulugU!@master.ccub4ta9krao.ap-southeast-2.rds.amazonaws.com:3306/eiz_test")

query = 'select id, companyName, email, credit, balance from accounts where id not in (1,284,317,513,911,2333,4832,1978,2677,3430,3793,3980,5474,5906,6572,6484,6681,6682,6684,6728,6734,6735) and credit > 0;'

with engine.connect() as con:
    df = pd.read_sql_query(query,con)
st.dataframe(df,hide_index=True)
