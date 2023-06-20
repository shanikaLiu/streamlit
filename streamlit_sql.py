import pandas as pd
import streamlit as st

# 读取CSV文件
df = pd.read_csv('./test-files/test.csv')

# 在Streamlit应用程序中展示数据
st.write(df)
