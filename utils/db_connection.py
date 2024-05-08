import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection parameters
dbname = "redash_chatbot_data"
user = "postgres"
password = "Adekunle_5880"
host = "localhost"  # or your PostgreSQL host address
port = "5432"  # default PostgreSQL port

# CSV file paths
chart_data = "/Users/expert/Desktop/10-Academy/week-3/redash-chatbot-project/data/Chart data.csv"



# Connect to PostgreSQL
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# Create SQLAlchemy engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

# Read CSV files into Pandas DataFrames
chart_df = pd.read_csv(chart_data)

# Write DataFrames to PostgreSQL tables
chart_df.to_sql('chart_df', engine, if_exists='replace', index=False)


# Commit and close connections
conn.commit()
conn.close()

print("Data has been successfully loaded into PostgreSQL tables.")