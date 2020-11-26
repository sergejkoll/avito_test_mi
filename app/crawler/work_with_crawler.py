import datetime
import threading
import configparser
from queue import Queue
from app.services import announcement_service
from app.utils import work_with_avito_api


class Counter:
    def __init__(self, id: int, update_time: float, text: str, region: str):
        self.id = id
        self.update_time = update_time
        self.text = text
        self.region = region


config = configparser.ConfigParser()
config.read("config.ini")

update = config["crawler"]["update_time"]
crawler_count = config["crawler"]["worker_count"]

q = Queue()


def add_count_in_queue(id: int, time: float, text: str, region: str):
    q.put(Counter(id, time + int(update), text, region))


def update_count():
    while True:
        counter = q.get()
        if datetime.datetime.now().timestamp() < counter.update_time:
            q.put(counter)
        else:
            new_count, timestamp = work_with_avito_api.get_count(counter.text, counter.region)
            announcement_service.add_counter(counter.id, new_count, timestamp)
            counter.update_time = datetime.datetime.now().timestamp() + int(update)
            q.put(counter)
            print(f"Updated, id: {counter.id}")


def start_crawler():
    counters = announcement_service.get_all_counters()
    for item in counters:
        q.put(Counter(item[0], item[2] + int(update), item[4], item[5]))

    for i in range(int(crawler_count)):
        t = threading.Thread(target=update_count)
        t.start()
