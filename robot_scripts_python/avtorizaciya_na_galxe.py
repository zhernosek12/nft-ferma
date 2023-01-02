import pytest
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from models.metamask import MetamaskSelenium


test_debuggerAddress = "127.0.0.1:58958/devtools/browser/47724229-b744-429f-b8b5-a0b0f7a2d278"
chrome_driver = "D:\mypapa\FermaDev\ChromeDriver2\chromedriver-windows-x64.exe"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option("debuggerAddress", test_debuggerAddress)

driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

metamaskSelenium = MetamaskSelenium(driver, "TrickSelfish3202")

# выполнение задач -->

def find_element_by_xpath_v2(driver, dom, sec=15):
    wait = WebDriverWait(driver, sec)
    return wait.until(EC.element_to_be_clickable((By.XPATH, dom)))

""" """

driver.get("https://galxe.com/")

driver.minimize_window()

driver.set_window_size(1370, 1010)

try:
    # после авторизации просит авторизоваться
    metamaskSelenium.connect_to_website()
except:
    pass

time.sleep(1)

driver.get("https://galxe.com/")

try:
    # кроме этого просит ещё и подключить потом
    metamaskSelenium.connect_to_website()
except:
    pass

time.sleep(1)

driver.get("https://galxe.com/accountSetting?tab=SocialLinlk")

time.sleep(1)

driver.get("https://galxe.com/twitterConnect")

time.sleep(1)

find_element_by_xpath_v2(driver, '//*[@id="app"]/div[1]/main/div/div/div/div[2]/div/button').click()

time.sleep(2)

driver.switch_to.window(driver.window_handles[1])

time.sleep(1)

find_element_by_xpath_v2(driver, "//span[contains(text(),'Tweet')]").click()

time.sleep(2)

find_element_by_xpath_v2(driver, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/a/span').click()

time.sleep(2)

tweet_url = driver.current_url

driver.close()

driver.switch_to.window(driver.window_handles[0])

driver.execute_script("window.scrollTo(0,10)")

time.sleep(1)

find_element_by_xpath_v2(driver, '//*[@id="app"]/div/main/div/div/div/div[3]/div/div[3]/input').send_keys(tweet_url)

time.sleep(1)

find_element_by_xpath_v2(driver, '//*[@id="app"]/div/main/div/div/div/div[3]/div/button').click()

time.sleep(5)

try:
    metamaskSelenium.sign_confirm()
except:
    pass

time.sleep(1)

driver.get(tweet_url)

#taskSuccess()

print("galaxy --> twitter connected!")
