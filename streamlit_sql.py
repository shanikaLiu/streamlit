import streamlit as st
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://eiz:Adgjl!2345@master.ccub4ta9krao.ap-southeast-2.rds.amazonaws.com:3306/eiz_test')

with engine.connect() as connection:
    result = connection.execute('select id, companyName, email from accounts where id in (79,277,336,363,911,2333,2677,5906,6682)')
    st.dataframe(result,hide_index=True)