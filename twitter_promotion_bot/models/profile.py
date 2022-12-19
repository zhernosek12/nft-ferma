from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import requests
import json

class Profile:
    def __init__(self, prof_data, proj_data, callbacks):

        # create profile and connect to tool
        self.id = prof_data["id"]
        self.name = prof_data["name"]
        self.dolphin_id = prof_data["dolphin_id"]

        self.project_id = proj_data["id"]
        self.project_name = proj_data["name"]
        self.project_url = proj_data["url"]

        self.dolphin_connect = False
        self.port = 0
        self.wsEndpoint = ""

        self.chrome_driver = "D:\mypapa\FermaDev\ChromeDriver2\chromedriver-windows-x64.exe"
        self.driver = None
        self.callbacks = callbacks

    def connect(self):

        url = "http://localhost:3001/v1.0/browser_profiles/"+self.dolphin_id+"/start?automation=1"
        payload = { }
        headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)' }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)

        try:
            if data["success"] == True:
                self.dolphin_connect = True
                self.port = data["automation"]["port"]
                self.wsEndpoint = data["automation"]["wsEndpoint"]
                self.dolphin()
        except Exception as ex:
            print(ex)

    def dolphin(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:" + str(self.port) + str(self.wsEndpoint))

        self.driver = webdriver.Chrome(self.chrome_driver, chrome_options=chrome_options)
        self.driver.maximize_window()

        curr = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if handle != curr:
                self.driver.close()

        self.callbacks.connected(self, self.project_id, self.project_name, self.project_url)

    def dolphin_stop(self):
        url = "http://localhost:3001/v1.0/browser_profiles/"+self.dolphin_id+"/stop"
        payload = { }
        headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)' }

        requests.request("GET", url, headers=headers, data=payload)

        print("Stop dolphin.")
