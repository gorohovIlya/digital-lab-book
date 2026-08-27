import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)
conn = psycopg2.connect(
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    database=os.environ["DB_NAME"],
    port=os.environ["DB_PORT"],
    password=os.environ["DB_PASSWORD"],
)

cursor = conn.cursor()