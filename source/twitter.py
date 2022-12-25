import requests
import time

from models.dolphin import Dolphin
from models.twitter import Twitter

# продвижение по аккаунту твиттера
# готовый скрипт, запускай да и все!

def request(method, datas):

    url = "http://checks.wordok.by/twitter/api.php?method=" + method
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'}

    response = requests.request("POST", url, headers=headers, data=datas)

    print(method, "--> send", datas)
    print("response -->", response.text)

# http://checks.wordok.by/twitter/router.php

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'}

class Callbacks:
    def result_followers(self, user_id, result):
        request("result_followers", {'user_id': str(user_id), 'result': ",".join(result)})


    def result_follow_and_scan_count(self, user_id, result):
        request("result_follow_and_scan_count", {'user_id': user_id,
                   'login': result[0],
                   'followers': result[1],
                   'following': result[2],
                   'follow': result[3],
                   'ban': result[4]})

    def result_scan_my_followers(self, user_id, result):
        request("result_scan_my_followers", {'user_id': str(user_id), 'result': ",".join(result)})

    def result_unfollow(self, user_id, login):
        request("result_unfollow", {'user_id': str(user_id), 'login': login})


dolphin = None
callbacks = Callbacks()
step = 0
max_steps = 1000

while True:

    # каждые 3 секунд получаем задачу
    time.sleep(3)

    response = requests.request("GET", "http://checks.wordok.by/twitter/router.php", headers=headers)

    for j in response.json():
        type = j["type"]
        user = j["user"]
        data = j["data"]

        # подключаемся к браузеру
        try:
            if dolphin is None:
                dolphin = Dolphin(user)
                dolphin.connect()
                time.sleep(3)
                #dolphin.get_driver().get("https://twitter.com/")
        except Exception as e:
            print("Error dolphin init!")
            print(e)
            break

        # ждем 5 секунд, после того как запустили
        time.sleep(5)

        if dolphin.isBrowserAlive() == False:
            print("Error connect dolphin!")
            time.sleep(5)
            break

        # подключаем модель твитера
        twitter = Twitter(dolphin.get_driver(), callbacks)

        if type == "GET_FOLLOWERS":
            # читаем фоловеров
            twitter.get_followers(data["login"], user["id"])

        if type == "FOLLOW_AND_SCAN_COUNT":
            # проверяем пользователя, и если что подписываемся
            result = twitter.follow_and_scan_count(data["login"], user["id"])
            # если мы в бане при подписке, значит отменим процесс.
            if result == True:
                print("ACCOUNT IS BAN!")
                break

        if type == "SCAN_MY_FOLLOW":
            # читаем фоловеров
            twitter.scan_my_followers(user["id"])

        if type == "UNFOLLOW":
            # отписываемся
            twitter.go_unfollow(data["login"], user["id"])

    # остановим задачу
    if dolphin is not None:
        dolphin.dolphin_stop()
        dolphin = None
        time.sleep(5)

    print("i don't sleep :)", step)

    step = step + 1
    if step > max_steps:
        break

#