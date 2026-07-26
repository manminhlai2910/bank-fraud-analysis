import os
import pandas as pd

df = pd.read_csv('Bank Fraud/bank.csv',low_memory=False)
df_sample = df.sample(n=500000, random_state=42)
df = df_sample.reset_index(drop=True)

df['timestamp'] = pd.to_datetime(df['timestamp'],format='mixed')

# print(df.isnull().sum())
# print(df[df['fraud_type'].isnull()]['is_fraud'].value_counts())

# print(df[df['fraud_type'].notnull()]['is_fraud'].value_counts())

df['fraud_type'] = df['fraud_type'].fillna('Not Applicable')

# df_sorted = df.sort_values(['sender_account', 'timestamp'])
# first_txn_per_account = df_sorted.groupby('sender_account').head(1)

# How many accounts total?
# print(f"Total unique accounts: {df['sender_account'].nunique()}")

# How many of those "first transactions" have a null time_since_last_transaction?
# print(f"First-transaction rows with null time_since_last: {first_txn_per_account['time_since_last_transaction'].isnull().sum()}")
# print(df[df['time_since_last_transaction'].isnull()]['is_fraud'].value_counts())

df['time_gap_missing'] = df['time_since_last_transaction'].isnull()

df['time_since_last_transaction'] = df['time_since_last_transaction'].fillna(-1)

# print(df.duplicated().sum())

df['transaction_hour'] = df['timestamp'].dt.hour
df['transaction_day_of_week'] = df['timestamp'].dt.day_name()
df['is_weekend'] = df['timestamp'].dt.dayofweek >= 5

# print(df.isnull().sum())


from sqlalchemy import create_engine,text

username = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
localhost = 5432
database = 'bank_db'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@localhost:{localhost}/{database}')

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("✅ Connection successful!")
        print(result.fetchone())
except Exception as e:
    print("❌ Connection failed.")
    print(f"Error: {e}")
df.to_sql('fraud', engine, if_exists='replace', index=False, chunksize=50000, method='multi')
print("Load complete.")