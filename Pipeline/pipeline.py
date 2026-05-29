import requests
import pandas as pd
import time
import mysql.connector 
import logging
import boto3

logging.basicConfig(
    filename='finance_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def fetch_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=os.getenv("API_KEY")"
    response = requests.get(url)
    print(f"{symbol} Status Code:", response.status_code)
    data = response.json()
    return data


def extract_time_series(data):
    time_series = data['Time Series (Daily)']
    return time_series


def convert_to_dataframe(time_series, symbol):
    
    df = pd.DataFrame(time_series).T
    df.reset_index(inplace=True)
    df.columns = [
    'stock_date',
    'open_price',
    'high_price',
    'low_price',
    'close_price',
    'volume']
    df['symbol'] = symbol

    return df

def clean_data(df):

    df['stock_date'] = pd.to_datetime(df['stock_date'])
    numeric_columns = [
    'open_price',
    'high_price',
    'low_price',
    'close_price',
    'volume']

    for col in numeric_columns:

        df[col] = pd.to_numeric(df[col])

    df = df.sort_values(by='stock_date')

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    df = df.drop_duplicates()

    df.reset_index(drop=True, inplace=True)

    return df

def insert_data(df):

    query = """
    INSERT INTO stock_data
    (
        stock_date,
        open_price,
        high_price,
        low_price,
        close_price,
        volume,
        symbol
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    inserted = 0
    duplicates = 0
    failed = 0

    for _, row in df.iterrows():

        values = (
            row['stock_date'].date(),
            row['open_price'],
            row['high_price'],
            row['low_price'],
            row['close_price'],
            row['volume'],
            row['symbol']
        )

        try:

            cursor.execute(query, values)

            inserted += 1

        except mysql.connector.IntegrityError:

            duplicates += 1

            logging.warning(
                f"Duplicate skipped: {row['symbol']} - {row['stock_date']}"
            )

        except Exception as e:

            failed += 1

            logging.error(f"Failed row insert: {e}")

    conn.commit()
    logging.info(f"Inserted rows: {inserted}")
    logging.info(f"Duplicate rows skipped: {duplicates}")
    logging.info(f"Failed rows: {failed}")
    print("Data inserted successfully")

def upload_to_s3():

    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name='ap-south-1'
    )

    s3.upload_file(
        'stock_data.csv',
        'finance-etl-sachith-2026',
        'raw-data/stock_data.csv'
    )

    print("File uploaded to S3 successfully")

    logging.info("CSV uploaded to S3 successfully")

def main():

    symbols = ["IBM", "NVDA","MSFT","TSLA"]

    all_dataframes = []
    for symbol in symbols:
        data = fetch_data(symbol)
        time_series = extract_time_series(data)
        df = convert_to_dataframe(time_series, symbol)
        all_dataframes.append(df)
        time.sleep(12)

    final_df = pd.concat(all_dataframes, ignore_index=True)
    print(final_df.head())
    final_df = clean_data(final_df)
    #insert_data(final_df)
    final_df.to_csv("stock_data.csv", index=False)
    print("CSV file created successfully")
    upload_to_s3()

try:

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="stocks_project"
    )

    cursor = conn.cursor()
    logging.info("MySQL connection successful")
    main()

except Exception as e:

    logging.error(f"Pipeline failed: {e}")
    print("Error occurred")
    print(e)

finally:

    try:
        conn.close()
        logging.info("MySQL connection closed")

    except:
        pass
