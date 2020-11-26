from app.models.database import database
from app.models.database import request_table
from app.models.database import counter_table
from app.models.database import engine


async def get_request_by_text_and_region(text: str, region: str):
    query = request_table.select().where((request_table.c.text == text) & (request_table.c.region == region))
    return await database.fetch_one(query)


async def create_object(obj_text: str, obj_region: str):
    query = request_table.insert().values(text=obj_text, region=obj_region)
    return await database.execute(query)


async def add_count(id: int, counter: int, timestamp: int):
    query = counter_table.insert().values(requestid=id, counter=counter, timestamp=timestamp)
    return await database.execute(query)


async def get_counters(id: int, start: int, end: int):
    query = counter_table.select().where((counter_table.c.requestid == id) &
                                         (counter_table.c.timestamp >= start) &
                                         (counter_table.c.timestamp <= end))
    return await database.fetch_all(query)


def get_all_counters():
    result_set = engine.execute("SELECT * FROM counter_table "
                                "JOIN request_table ON request_table.id = counter_table.requestId")
    return result_set


def add_counter(id: int, count: int, timestamp: int):
    result = engine.execute(f"INSERT INTO counter_table values ({id}, {count}, {timestamp})")
    return result
