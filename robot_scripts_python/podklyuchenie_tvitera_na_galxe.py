metamaskSelenium = MetamaskSelenium(driver, metamask_password)

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

metamaskSelenium.sign_confirm()

time.sleep(1)

driver.get(tweet_url)

print("galaxy --> twitter connected!")
