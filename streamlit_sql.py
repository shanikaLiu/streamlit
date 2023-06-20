# from src.date import QueryTime

# import pandas as pd
# import streamlit as st
# import subprocess

# # 在 Streamlit 加载应用程序时执行 main.py
# def run_main_script():
#     subprocess.run(['python', 'main.py'])

# # Streamlit 应用程序的主要部分
# def main():
#     # 运行 main.py
#     run_main_script()

#     # 在这里添加 Streamlit 的代码逻辑
#     # ...
#     qt = QueryTime()
#     today_line = qt.formatted_today()['today_line']

#     read_path = f'data/{today_line}.csv'
#     df = pd.read_csv(read_path)

#     st.set_page_config(page_title="Super Freight Sales Dashboard",page_icon=":bar_chart:",layout="wide")


#     # ---- Sidebar ----

#     st.sidebar.write('**Use filters to select prospects** 👇')
#     unique_sales = sorted(df["sales"].fillna('NULL').unique())
#     unique_account_id = sorted(df["eiz_account_id"].astype(int).unique())
#     unique_email = sorted(df["email"].unique())
#     unique_company_name = sorted(df["companyName"].fillna('NULL').unique())


#     sales_checkbox = st.sidebar.checkbox('All Sales',help='Check this box to select all sales.')
#     if sales_checkbox:
#         selected_sales = st.sidebar.multiselect('Select Sales Name:',unique_sales,unique_sales)
#     else:
#         selected_sales = st.sidebar.multiselect('Select Sales Name:',unique_sales)


#     account_id_checkbox = st.sidebar.checkbox('All EIZ Account ID',help='Check this box to select all account ID.')
#     if account_id_checkbox:
#         selected_account_id = st.sidebar.multiselect('Select Account ID:',unique_account_id,unique_account_id)
#     else:
#         selected_account_id = st.sidebar.multiselect('Select Account ID:',unique_account_id)


#     email_checkbox = st.sidebar.checkbox('All Email Address',help='Check this box to select all email addresses.')
#     if email_checkbox:
#         selected_email = st.sidebar.multiselect('Select Email Address:',unique_email,unique_email)
#     else:
#         selected_email = st.sidebar.multiselect('Select Email Address:',unique_email)


#     company_name_checkbox = st.sidebar.checkbox('All Companies',help='Check this box to select all companies.')
#     if company_name_checkbox:
#         selected_company_name = st.sidebar.multiselect('Select Company:',unique_company_name,unique_company_name)
#     else:
#         selected_company_name = st.sidebar.multiselect('Select Company:',unique_company_name)


#     if len(selected_sales) > 0:
#         df_filtered = df[(df['sales'].fillna('NULL').isin(selected_sales))]
#         num_of_cust = str(df_filtered.shape[0])
#     else:
#         df_filtered = df
#         num_of_cust = str(df_filtered.shape[0])


#     if len(selected_account_id) > 0:
#         df_filtered = df[(df['eiz_account_id'].astype(int).isin(selected_account_id))]
#         num_of_cust = str(df_filtered.shape[0])
#     else:
#         df_filtered = df
#         num_of_cust = str(df_filtered.shape[0])


#     if len(selected_email) > 0:
#         df_filtered = df[(df['email'].isin(selected_email))]
#         num_of_cust = str(df_filtered.shape[0])
#     else:
#         df_filtered = df
#         num_of_cust = str(df_filtered.shape[0])


#     if len(selected_company_name) > 0:
#         df_filtered = df[(df['companyName'].fillna('NULL').isin(selected_company_name))]
#         num_of_cust = str(df_filtered.shape[0])
#     else:
#         df_filtered = df
#         num_of_cust = str(df_filtered.shape[0])


#     # ---- Main Page ----
#     st.title(":bar_chart: Super Freight Sales Dashboard")
#     st.markdown("##")   # 换行



#     # df_selection = df.query(
#     #     "Sales == @sales & @Account_ID ==@eiz_account_id & Email == @email & Company_Name == @companyName Num_of_Consignments == @numberOfconsignments Total_Spent == @total_spend & End_of_Week == @week_end"
#     # )

#     # Top KPI's
#     this_year_total_sales = int(12345678)
#     this_month_total_sales = int(123456)
#     this_week_total_sales = int(1234)
#     total_customers = int(123)
#     st.markdown("##")

#     # left_column_l1, middle_column1_l1, middle_column2_l1, right_column_l1 = st.columns(4)
#     # with left_column_l1:
#     #     st.subheader("This Year Total Sales:")
#     #     st.subheader(f"AU $ {this_year_total_sales:,}")
#     # with middle_column1_l1:
#     #     st.subheader("This Month Total Sales:")
#     #     st.subheader(f"AU $ {this_month_total_sales:,}")
#     # with middle_column2_l1:
#     #     st.subheader("This Week Total Sales:")
#     #     st.subheader(f"AU $ {this_week_total_sales:,}")

#     # with right_column_l1:
#     #     st.subheader("Total Customer:")
#     #     st.subheader(f" {total_customers:,}")

#     # this_year_target = int(18888888)
#     # this_week_target = int(199999)
#     # this_week_target = int(1999)
#     st.metric(label='Number of Prospects', value=num_of_cust)
#     st.dataframe(df_filtered,hide_index=True)


# if __name__ == '__main__':
#     main()


# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from accounts where id = 79;', ttl=600)

# Print results.
st.dataframe(df,hide_index=True)