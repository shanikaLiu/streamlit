# streamlit_app.py

import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.cache_resource to only run once.
# @st.cache_resource
# def init_connection():
#     return st.experimental_connection('mysql',type='sl')

# conn = init_connection()

# # Perform query.
# # Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=3600)
# def run_query(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         return cur.fetchall()

# rows = run_query("SELECT * from accounts limit 10;")

# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")

conn = st.experimental_connection('mysql',type='sql',ttl=3600)
df = conn.query("SELECT * from accounts limit 10;")
st.dataframe(df)