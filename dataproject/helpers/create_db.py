import os
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

dbname = f'{os.getenv("DATABASE")}'
username = f'{os.getenv("DBUSERNAME")}'
password = f'{os.getenv("DBPASSWORD")}'
dbhost = f'{os.getenv("DBHOST")}'

DATABASE_URL = "postgresql://"+username+":" + \
    password+"@"+dbhost+":5432/"+dbname

engine = create_engine(DATABASE_URL, echo=False)


def main():
    if database_exists(engine.url):
        print("Database already exists")

    else:
        print("Database Not Present. Creating.....")
        # Create DB undata
        create_database(engine.url)

        print("Database Created.....")


if __name__ == '__main__':
    main()
