import mongoengine

DATABASE_NAME = 'shopee-case-study-database'
DATABASE_HOST = '127.0.0.1'
PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''


def setup_mongodb_connection():
    mongoengine.connect(
        db=DATABASE_NAME,
        host=DATABASE_HOST,
        port=PORT,
        username=MONGO_USERNAME,
        password=MONGO_PASSWORD
    )
