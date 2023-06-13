# import streamlit as st


# conn = st.experimental_connection('eiz_test', type='sql')

# # View the connection contents.
# conn

# a = conn.query('select id, companyName, email, credit, balance from accounts where id not in (1,284,317,513,911,2333,4832,1978,2677,3430,3793,3980,5474,5906,6572,6484,6681,6682,6684,6728,6734,6735) and credit > 0;',ttl=600)
# st.dataframe(a,hide_index=True)

import toml
import streamlit as st
import mysql.connector as connection
import pandas as pd
# Reading data
toml_data = toml.load(".streamlit\secrets.toml")
# saving each credential into a variable
HOST_NAME = toml_data['mysql']['host']
DATABASE = toml_data['mysql']['database']
PASSWORD = toml_data['mysql']['password']
USER = toml_data['mysql']['username']
PORT = toml_data['mysql']['port']

# Using the variables we read from secrets.toml
mydb = connection.connect(host=HOST_NAME, database=DATABASE, user=USER, passwd=PASSWORD, use_pure=True)

query = pd.read_sql('SELECT * FROM accounts limit 1;' , mydb)

st.dataframe(query,hide_index=True)
