import streamlit as st
import pandas as pd
import mysql.connector


st.title("Stock Market Dashboard")

conn = mysql.connector.connect(
    host="localhost",
    user=YOUR_USER,
    password=os.getenv("MYSQL_PASSWORD"),
    database="stocks_project"
)


query = "SELECT * FROM stock_data"

cursor = conn.cursor()

cursor.execute(query)

data = cursor.fetchall()

columns = [col[0] for col in cursor.description]

df = pd.DataFrame(data, columns=columns)

st.subheader("Stock Data")

st.dataframe(df)

symbols = df['symbol'].unique()

selected_symbol = st.multiselect(
    "Select Company",
    symbols
)



filtered_df = df[df['symbol'].isin(selected_symbol)]
latest_price = filtered_df['close_price'].iloc[-1]
highest_price = filtered_df['high_price'].max()
lowest_price = filtered_df['low_price'].min()

st.subheader(f"{selected_symbol} Closing Prices")

col1, col2, col3 = st.columns(3)
col1.metric("Latest Price", latest_price)
col2.metric("Highest Price", highest_price)
col3.metric("Lowest Price", lowest_price)


chart_data = filtered_df.pivot(
    index='stock_date',
    columns='symbol',
    values='close_price'
)

st.line_chart(chart_data)

st.subheader("Trading Volume")

volume_chart = filtered_df[
    ['stock_date', 'volume']
]
volume_chart = volume_chart.set_index('stock_date')
st.bar_chart(volume_chart)

query = """
SELECT symbol, MAX(close_price) AS highest_close
FROM stock_data
GROUP BY symbol
ORDER BY highest_close DESC
LIMIT 1
"""

cursor.execute(query)
result = cursor.fetchone()
top_symbol = result[0]
top_price = result[1]

st.metric(
    "Top Performing Stock",
    f"{top_symbol} : {round(top_price, 2)}"
)

conn.close()
