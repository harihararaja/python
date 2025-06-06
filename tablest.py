import streamlit as st
import pymysql
import pandas as pd

# Page config
st.set_page_config(page_title="Full MySQL Database Viewer", layout="wide")
st.title(" Complete XAMPP MySQL Database: `polling_list`")

# Initialize connection variable
conn = None

# Function to connect to MySQL
def connect_to_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="polling_list",
        charset="utf8mb4"
    )

# Try to connect and display tables
try:
    conn = connect_to_db()
    cursor = conn.cursor()

    # Get all tables
    cursor.execute("SHOW TABLES")
    tables = [row[0] for row in cursor.fetchall()]

    if tables:
        st.success(f" Found {len(tables)} table(s) in the database.")
        for table_name in tables:
            st.subheader(f"📌 Table: `{table_name}`")
            try:
                df = pd.read_sql(f"SELECT * FROM `{table_name}`", conn)
                st.dataframe(df, use_container_width=True)
            except Exception as e:
                st.warning(f" Could not load table `{table_name}`: {e}")
    else:
        st.info("No tables found in the database.")

except Exception as e:
    st.error(f" Error: {e}")

finally:
    if conn:
        conn.close()
