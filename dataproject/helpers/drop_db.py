from sqlalchemy_utils import database_exists, drop_database
from create_db import engine


def main():
    if database_exists(engine.url):
        drop_database(engine.url)

    if not database_exists(engine.url):
        print("Database has been deleted.....")


if __name__ == '__main__':
    main()
