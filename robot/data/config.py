import os

from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID').split(', ')
CHANNEL_ID = os.getenv('CHANNEL_ID', '-1001275637856').split(', ')
# print(CHANNEL_ID)

# postgres
DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')


DATABASE_CONFIG = {
    "connections": {
        "default": f"postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        # "default": "sqlite://db.sqlite3" # for sqlite database, should be install `tortoise-orm[aSQLite]``
    },
    "apps": {
        "models": {
            "models": ["utils.db.models",  "aerich.models"],  
            "default_connection": "default",
        }
    }
}
