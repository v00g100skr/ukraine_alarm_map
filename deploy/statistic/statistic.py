import json
import os
import asyncio
import logging
from aiomcache import Client
from peewee import *
import datetime

version = 1

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


loop_time = int(os.environ.get('LOOP_TIME', 1))
memcached_host = os.environ.get('MEMCACHED_HOST') or 'localhost'
db_name = os.environ.get('DB_NAME') or 'jaam'
db_user = os.environ.get('DB_USER') or 'user'
db_password = os.environ.get('DB_PASSWORD') or 'password'
db_host = os.environ.get('DB_HOST') or 'localhost'
db_port = os.environ.get('DB_PORT') or 3306


db = MySQLDatabase('mysql', user=db_user, password=db_password,
                   host=db_host, port=db_port)


class BaseModel(Model):
    class Meta:
        database = db


class Client(BaseModel):
    chip_id = CharField(max_length=32)
    firmware = CharField(max_length=32)
    created_at = DateTimeField(default=datetime.datetime.now)
    connected = BooleanField(default=True)
    changed_at = DateTimeField(default=datetime.datetime.now)


class Connection(BaseModel):
    chip_id = CharField(max_length=32)
    firmware = CharField(max_length=32)
    created_at = DateTimeField(default=datetime.datetime.now)
    connected = BooleanField(default=True)



async def statistic(mc, db):
    try:
        await asyncio.sleep(loop_time)
        alerts_cached = await mc.get(b"alerts")

        if alerts_cached:
            alerts_cached_data = json.loads(alerts_cached.decode('utf-8'))
        else:
            alerts_cached_data = {}

        logging.debug(alerts_cached_data)

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        await asyncio.sleep(loop_time)


async def main():
    mc = Client(memcached_host, 11211)
    db = MySQLDatabase('mysql', user=db_user, password=db_password,
                       host=db_host, port=db_port)
    # Connect to your Memcache server
    db.connect()
    db.execute_sql(f'CREATE DATABASE IF NOT EXISTS {db_name}')
    db.close()

    db = MySQLDatabase(db_name, user=db_user, password=db_password,
                       host=db_host, port=db_port)
    db.create_tables([Client, Connection], safe=True)
    while True:
        try:
            logging.debug("Task started")
            await statistic(mc, db)

        except asyncio.CancelledError:
            logging.info("Task canceled. Shutting down...")
            await mc.close()
            break

        except Exception as e:
            logging.error(f"Caught an exception: {e}")

        finally:
            logging.debug("Task completed")
            pass


if __name__ == "__main__":
    try:
        logging.debug("Start")
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.debug("KeyboardInterrupt")
        pass
