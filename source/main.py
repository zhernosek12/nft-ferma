# PYTHON Example
from random import randrange

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from models.database import get_project
from models.profile import Profile
from models.premint import Premint

import time


class Callbacks:
    def connected(self, profile, pj_id, pj_name, pj_url):
        premint = Premint(profile, pj_id, pj_name, pj_url)
        premint.start()

def T_800Activate():

    data = get_project()
    callbacks = Callbacks()

    if data["status"] == "NEW":
        p = Profile(data["profile"], data["project"], callbacks)
        p.connect()


# Количество выполнений, максимум 1000
steps = 1000

# Максимум 5 минут, минимум 20 сек задержка
min_time = 20
max_time = 3 * 60

for s in range(steps):

    # Активируем нашего робота-убийцу NFT
    T_800Activate()

    # прячемся под человека
    # поэтому действие будем ограничивать по времени
    time_sleep = randrange(min_time, max_time)

    # подождем, поспим пока.
    print("Sleep time", time_sleep, "sec.")

    time.sleep(time_sleep)


