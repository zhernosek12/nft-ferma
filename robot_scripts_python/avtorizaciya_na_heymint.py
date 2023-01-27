driver.minimize_window()

driver.set_window_size(1370, 1010)

driver.set_window_position(100, 100, windowHandle='current')

metamaskSelenium = MetamaskSelenium(driver, metamask_password)

driver.get("https://heymint.xyz/user/login")

time.sleep(2)

find_element_by_xpath_v2(driver, "/html/body/div/div[1]/div[1]/div/div/button[2]").click()

time.sleep(2)

find_element_by_xpath_v2(driver, '//*[@id="allow"]').click()

time.sleep(2)

driver.get("https://heymint.xyz/user/wallets")

time.sleep(2)

find_element_by_xpath_v2(driver, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[2]/button[1]/div').click()

time.sleep(2)

find_element_by_xpath_v2(driver, '/html/body/div[3]/div/div/div/button[2]/div/p').click()

time.sleep(2)

metamaskSelenium.connect_to_website()

time.sleep(2)

find_element_by_xpath_v2(driver, '/html/body/div[3]/div/div/div/button[2]/div/p').click()

time.sleep(2)

metamaskSelenium.connect_to_website()

time.sleep(2)

find_element_by_xpath_v2(driver, '/html/body/div[3]/div/div/button[1]').click()

time.sleep(2)

metamaskSelenium.sign_confirm()
