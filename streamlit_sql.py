# import streamlit as st
# from sqlalchemy import create_engine


# engine = create_engine(r'mysql+pymysql://viewuser:)5y)JHhqsFulugU!@master.ccub4ta9krao.ap-southeast-2.rds.amazonaws.com:3306/eiz_test')

# with engine.connect() as connection:
#     result = connection.execute('select id, companyName, email from accounts where id in (79,277,336,363,4904,911,2333,2677,5906,6682,6832)')
#     st.dataframe(result,hide_index=True)


import streamlit as st

conn = st.experimental_connection('eiz_test', type='sql')

# View the connection contents.
conn

a = conn.query('select id, companyName, email, credit, balance from accounts where id not in (1,284,317,513,911,2333,4832,1978,2677,3430,3793,3980,5474,5906,6572,6484,6681,6682,6684,6728,6734,6735) and credit > 0;',ttl=600)
st.dataframe(a,hide_index=True)