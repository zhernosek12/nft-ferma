from models.twitter import Twitter
from models.database import get_project, set_status_project

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# event mint
# Raffle Time --> время выбора победителя
# Mint Date --> время когда можно получить
#

class Premint:
    def __init__(self, profile, project_id, name, url):
        self.project_id = project_id
        self.profile = profile
        self.name = name
        self.url = url
        self.tasks = []

        self.wait = WebDriverWait(self.profile.driver, 10)

    def start(self):

        print("Go -->", self.url)
        self.profile.driver.get(self.url)

        time.sleep(2)

        print("parsing twitter tasks...")
        self.parsingTwitter()

        try:
            step_discord = self.profile.driver.find_element(By.ID, 'step-discord')
        except Exception as ex:
            pass

        self.exec()

    def parsingTwitter(self):

        #
        #
        #

        try:
            elem = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="step-twitter"]/div/div/div[3]/div[1]')))

            print("twitter links:", elem.text)

            if "Follow" in elem.text:
                links = elem.find_elements(By.TAG_NAME, "a")
                for link in links:
                    tw_link = link.get_attribute("href")
                    tw_text = link.text

                    print("tw_link", tw_link)

                    self.tasks.append({
                        "type": "FOLLOW",
                        "link": tw_link,
                        "text": tw_text
                    })

        except Exception as ex:
            print("No follow!")

        #
        #
        #

        try:
            elem = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="step-twitter"]/div/div/div[3]/div[2]')))

            if "Like" in elem.text:
                links = elem.find_elements(By.TAG_NAME, "a")
                for link in links:
                    tw_link = link.get_attribute("href")
                    tw_text = link.text

                    self.tasks.append({
                        "type": "RETWEET",
                        "link": tw_link,
                        "text": tw_text
                    })

        except Exception as ex:
            print("No retweet!")

    def exec(self):

        #
        twitter = Twitter(self.profile.driver)

        for task in self.tasks:

            if task["type"] == "FOLLOW":
                twitter.follow(task["link"])

            if task["type"] == "RETWEET":
                twitter.retweet(task["link"])

            #
            time.sleep(2)

        # tasks complete!!!
        # submit
        self.submit()

    def submit(self):
        try:
            self.profile.driver.get(self.url)
            time.sleep(2)

            submit = self.profile.driver.find_element(By.ID, "register-submit")
            self.profile.driver.execute_script("arguments[0].click();", submit)

        except Exception as ex:
            print("Submit error:", ex)

        time.sleep(10)
        self.checkRegistered()

    def checkRegistered(self):
        self.profile.driver.get(self.url)
        time.sleep(2)

        reg_form = self.profile.driver.find_element(By.ID, "register-form")
        reg_form_text = (reg_form.text).split("\n")
        reg_form_text_header = reg_form_text[0]

        if reg_form_text_header == "Registered":
            set_status_project(self.profile.id, self.project_id, "Registered")
        else:
            set_status_project(self.profile.id, self.project_id, "Error")

        self.finish()

    def finish(self):
        self.profile.driver.quit()
        self.profile.dolphin_stop()
