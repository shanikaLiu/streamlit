import streamlit as st

conn = st.experimental_connection('eiz_test', type='sql')

# View the connection contents.
conn

a = conn.query('select id, companyName, email, credit, balance from accounts where id not in (1,284,317,513,911,2333,4832,1978,2677,3430,3793,3980,5474,5906,6572,6484,6681,6682,6684,6728,6734,6735) and credit > 0;',ttl=600)
st.dataframe(a,hide_index=True)