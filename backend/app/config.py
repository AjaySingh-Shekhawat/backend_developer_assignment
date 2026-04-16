import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KET = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
DATABASE_URL = os.getenv("mysql+pymysql://root:MySQL96%40101215@localhost:3306/backend_developer_db")